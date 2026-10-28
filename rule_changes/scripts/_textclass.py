"""Token-level classification of the difference between two texts (shared by 02, 06 and 08b).

classify(old, new) -> (cls, changed_tokens) with cls one of
  format_only     token sequences identical (punctuation, quotes, hyphenation, number notation, cross-reference numbers ignored)
  numbering_only  identical apart from a single-digit list marker at the very start or end of the text ('2.')
  xref_change     wording identical but a cross-referenced Law/clause number differs ('Law 18.11' -> 'Law 18.12')
  ocr_noise       identical once OCR garbage is ignored (a rare token paired with a near-identical token: 'docs'/'does', 'froi'/'from')
  minor_wording   <= 3 changed words, none modal/negation/quantifier/number word
  substantive     anything else
"""
import difflib
import re
from collections import Counter
from functools import lru_cache
from pathlib import Path

from _numvals import NUM, REFS, UNI, WORDS, _SUP


def ref_sig(text):
    """Numbers inside Law/clause cross-references, in order (toks() strips these, so a changed citation is otherwise invisible)."""
    return [n for m in REFS.finditer(text or "") for n in re.findall(r"\d+(?:\.\d+)*", m.group(0))]

KEEP = {"shall", "may", "must", "not", "no", "should", "will", "can", "cannot", "never", "any", "all", "only", "either",
        "neither", "unless", "except", "provided", "if", "when", "whether", "both", "each", "every", "other", "than", "least",
        "more", "less", "before", "after", "until", "without", "unless"} | set(WORDS)


def _val(m):
    g = m.groupdict()
    if g.get("mixed"):
        v = float(g["mixed"]) + (int(g["mn"]) / int(g["md"]) if int(g["md"]) else 0)
    elif g.get("wu"):
        v = float(g["wu"]) + UNI[g["u"]]
    elif g.get("fn"):
        v = int(g["fn"]) / int(g["fd"]) if int(g["fd"]) else 0.0
    elif g.get("dec"):
        v = float(g["dec"])
    elif g.get("u2"):
        v = UNI[g["u2"]]
    else:
        return " " + g["w"].lower() + " "
    return f" #{round(v, 3):g} "


def toks(text):
    t = re.sub(r"(\d)([⁰¹²³⁴-⁹]+)", r"\1 \2", text or "")
    t = t.translate(_SUP)
    t = REFS.sub(" ", t)
    t = t.replace("’", "'").lower()
    t = re.sub(r"(\w)-\s*(\w)", r"\1\2", t)  # hyphenation: one-day == oneday
    t = NUM.sub(_val, t)
    # list labels such as (b) or (iv) are layout, not wording; 'm' (metres) and 'a'/'i' as words are kept out of the filter
    return [x for x in re.findall(r"#[\d.]+|[a-z]+", t) if not re.fullmatch(r"[b-h]|ii|iii|iv|vi{0,3}|ix|x", x)]


STOP = {"the", "a", "an", "of", "to", "in", "and", "or", "he", "his", "it", "is", "be", "by", "that", "this", "which", "as", "at", "on", "for", "are", "was", "has", "have", "him", "they", "their", "its", "shall", "from", "with", "she", "her", "above", "below", "also", "then", "so", "i", "s"}
RARE = 15   # OCR garbage: a token seen at most this often, 25x rarer than a near-identical partner with the same first letter


@lru_cache(maxsize=1)
def _freq():
    d = Path(__file__).resolve().parents[2] / "data/datasets/rule_texts/processed"
    c = Counter()
    for f in d.glob("*_processed.txt"):
        c.update(toks(f.read_text(encoding="utf-8", errors="ignore")))
    return c


def _noise_pair(x, y):
    """x, y differ; is one of them OCR garbage for the other (rare token, near-identical spelling)?"""
    if x.startswith("#") or y.startswith("#"):
        return False
    f = _freq()
    rare, other = (x, y) if f[x] <= 15 and f[x] * 25 < f[y] else (y, x) if f[y] <= 15 and f[y] * 25 < f[x] else (None, None)
    if rare is None or len(rare) < 3 or rare[0] != other[0] or (len(rare) > len(other) and rare.startswith(other)):
        return False                                  # real word swaps (hat/bat, caught/bought) change the first letter
    return difflib.SequenceMatcher(None, rare, other).ratio() >= 0.75


def _classify(old_text, new_text):
    a, b = toks(old_text), toks(new_text)
    if a == b:
        return "format_only", []
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    changed, only_edge_digits, noise, content_indel = [], True, 0, 0
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        if tag == "replace" and (i2 - i1) == (j2 - j1) and all(_noise_pair(x, y) for x, y in zip(a[i1:i2], b[j1:j2])):
            noise += i2 - i1
            continue
        seg = a[i1:i2] + b[j1:j2]
        if tag == "replace" and any((x.endswith(y) or y.endswith(x)) and abs(len(x) - len(y)) >= 3 and min(len(x), len(y)) >= 4 and x not in STOP and y not in STOP for x, y in zip(a[i1:i2], b[j1:j2])):
            content_indel += 2                     # 'striker' -> 'non-striker'
        if tag == "replace" and any(difflib.SequenceMatcher(None, x, y).ratio() < 0.8 and x not in STOP and y not in STOP and not {x, y} <= {'in', 'out', 'on', 'off'} and not x.startswith("#") and not y.startswith("#")
                                    for x, y in zip(a[i1:i2], b[j1:j2])):
            content_indel += 2                     # a real word swap (captains->umpires, leg->off), not a spelling variant
        if tag in ("insert", "delete"):
            content_indel += sum(1 for t in seg if t not in STOP and not t.startswith("#"))
        if tag == "replace" and any(x in ("in", "out", "on", "off") and y in ("in", "out", "on", "off") for x, y in zip(a[i1:i2], b[j1:j2])):
            content_indel += 2
        changed += seg
        edge = (i1 == 0 or i2 == len(a)) and (j1 == 0 or j2 == len(b))
        if not (all(t.startswith("#") and len(t) == 2 for t in seg) and edge):
            only_edge_digits = False
    if not changed and noise:
        return "ocr_noise", []
    if only_edge_digits:
        return "numbering_only", changed
    nonlist = [t for t in changed if not (t.startswith("#") and len(t) == 2 and False)]
    if len(nonlist) <= 3 and not any(t in KEEP or t.startswith("#") for t in nonlist) and content_indel < 1:
        return "minor_wording", nonlist
    return "substantive", nonlist[:30]


def classify(old_text, new_text):
    cls, ch = _classify(old_text, new_text)
    if cls in ("format_only", "ocr_noise", "numbering_only", "minor_wording") and ref_sig(old_text) != ref_sig(new_text):
        return "xref_change", ch
    return cls, ch


def is_substantive(old_text, new_text):
    return classify(old_text, new_text)[0] == "substantive"
