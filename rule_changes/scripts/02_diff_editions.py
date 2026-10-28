"""
02_diff_editions.py
Deterministic diff of consecutive editions -> candidate change records (no categories yet).

Pipeline per pair (A -> B):
  1. Law alignment: order-preserving weighted alignment of A's and B's main-code Laws by text
     similarity (so renumbering is detected by content, not by number).
  2. Unit alignment inside each matched Law pair: same alignment on sentences/clauses.
  3. Leftover (unmatched) units across the whole pair are re-matched globally to catch moves
     between Laws.
  4. Emit change records: add | remove | modify | move | renumber (Law number/title change only).

Inputs : rule_changes/data/nodes/<year>.jsonl  (from 01_segment_laws.py)
Outputs: rule_changes/data/alignments/<a>_<b>.json  (Law alignment + per-pair quality stats)
         rule_changes/data/changes/<a>_<b>.jsonl    (change records)

Usage (from the repo root):
    .venv/bin/python rule_changes/scripts/02_diff_editions.py 1884:1890 1890:1892 1932:1939
"""
import difflib
import json
import re
import sys
from collections import OrderedDict
from pathlib import Path

from rapidfuzz import fuzz

ROOT = Path(__file__).resolve().parents[2]
NODES = ROOT / "rule_changes/data/nodes"
ALIGN = ROOT / "rule_changes/data/alignments"
CHANGES = ROOT / "rule_changes/data/changes"

LAW_MATCH_MIN = 0.45   # whole-Law text similarity needed to call two Laws "the same Law"
UNIT_MATCH_MIN = 0.55  # unit similarity needed to call two units "the same rule, reworded"
MOVE_MATCH_MIN = 0.80  # leftover units matched across Laws must be this similar
TRIVIAL_MIN = 0.97     # modify with similarity >= this and no numeric change = wording-only

NUMBER_WORDS = ("one two three four five six seven eight nine ten eleven twelve fifteen twenty thirty forty "
                "fifty sixty seventy eighty ninety hundred half quarter first second third fourth fifth sixth once twice").split()


def load(year):
    laws = OrderedDict()
    for line in open(NODES / f"{year}.jsonl", encoding="utf-8"):
        n = json.loads(line)
        laws.setdefault((n["section"], n["law_no"]), dict(section=n["section"], no=n["law_no"],
                                                          title=n["law_title"], units=[]))["units"].append(n)
    return list(laws.values())


def sim(a, b):
    if not a or not b:
        return 0.0
    return max(fuzz.ratio(a, b), fuzz.token_sort_ratio(a, b) * 0.97) / 100.0


def align(xs, ys, key, threshold, simf=None):
    """Order-preserving alignment maximising total similarity over pairs scoring >= threshold."""
    n, m = len(xs), len(ys)
    S = [[0.0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            S[i][j] = simf(xs[i], ys[j]) if simf else sim(key(xs[i]), key(ys[j]))
    D = [[0.0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            best = max(D[i - 1][j], D[i][j - 1])
            if S[i - 1][j - 1] >= threshold:
                best = max(best, D[i - 1][j - 1] + S[i - 1][j - 1])
            D[i][j] = best
    i, j, pairs = n, m, []
    while i > 0 and j > 0:
        if S[i - 1][j - 1] >= threshold and abs(D[i][j] - (D[i - 1][j - 1] + S[i - 1][j - 1])) < 1e-9:
            pairs.append((i - 1, j - 1, S[i - 1][j - 1]))
            i, j = i - 1, j - 1
        elif D[i - 1][j] >= D[i][j - 1]:
            i -= 1
        else:
            j -= 1
    pairs.reverse()
    return pairs


def norm_(s):
    return re.sub(r"\s+", " ", s.replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"')).strip().lower()


def title_key(t):
    return re.sub(r"[^a-z ]", "", (t or "").lower()).replace("the ", "").strip()


def assign_laws(Am, Bm, threshold):
    """Optimal 1:1 Law matching by content, helped by title/number agreement (not order-preserving: Laws were
    reordered in 1947, 1980, 2000...). Weak content-only matches are refused so merged/dropped Laws stay unmatched."""
    import numpy as np
    from scipy.optimize import linear_sum_assignment
    n, m = len(Am), len(Bm)
    S = np.zeros((n, m))
    W = np.zeros((n, m))
    for i, la in enumerate(Am):
        for j, lb in enumerate(Bm):
            c = law_sim(la, lb) - (0.05 if la["no"] == lb["no"] else 0.0)  # content-only part
            ta, tb = title_key(la["title"]), title_key(lb["title"])
            t_eq = bool(ta and tb and (ta == tb or fuzz.ratio(ta, tb) >= 85))
            n_eq = la["no"] == lb["no"]
            ok = c >= 0.60 or (t_eq and c >= 0.35) or (n_eq and c >= 0.50)
            S[i, j] = c
            W[i, j] = (c + 0.30 * t_eq + 0.05 * n_eq) if ok else 0.0
    rows, cols = linear_sum_assignment(-W)
    return sorted((int(i), int(j), float(S[i, j])) for i, j in zip(rows, cols) if W[i, j] > 0)


def law_text(law):
    return " ".join(u["text_norm"] for u in law["units"])


def law_sim(la, lb):
    """Law similarity robust to Notes being added/removed: compare rule bodies and the opening statement."""
    ba = " ".join(u["text_norm"] for u in la["units"] if u["kind"] == "body")
    bb = " ".join(u["text_norm"] for u in lb["units"] if u["kind"] == "body")
    s_body = sim(ba, bb)
    fa = next((u["text_norm"] for u in la["units"] if u["kind"] == "body"), "")
    fb = next((u["text_norm"] for u in lb["units"] if u["kind"] == "body"), "")
    s_first = sim(fa, fb)
    s_all = sim(law_text(la), law_text(lb))
    bonus = 0.05 if la["no"] == lb["no"] else 0.0
    return min(1.0, max(s_body, 0.9 * s_first, s_all) + bonus)


ITEM = r"\(?[A-Z]?\d+(?:\.\d+)*[a-z]?\)?(?:\s*\([^)]{0,60}\))?"
REF_NUM = re.compile(r"(?:Laws?|Notes?|paragraphs?|clauses?|Appendix|sub-?clauses?|see)\s*" + ITEM +
                     r"(?:\s*(?:,|and|&|or|to)\s*" + ITEM + r")*", re.I)
CLAUSE_REF = re.compile(r"\b\d{1,2}(?:\.\d{1,2}){1,4}\b(?!\s*(?:metres?|m\b|yards?|inch|inches|ounces?|oz|cm|mm|g\b|grams?|per cent|%))")


def cues(old, new):
    """Value-level numeric cues: numbers (incl. fractions, decimals, number words) present in only one text."""
    from _numvals import values
    a, b = values(old), values(new)
    fmt = lambda v: f"{v:g}"
    return [fmt(v) for v in sorted(set(a) - set(b))], [fmt(v) for v in sorted(set(b) - set(a))]


def word_diff(old, new):
    sm = difflib.SequenceMatcher(None, old.split(), new.split(), autojunk=False)
    out = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag != "equal":
            out.append(dict(op=tag, old=" ".join(old.split()[i1:i2]), new=" ".join(new.split()[j1:j2])))
    return out


def granularity(unit, law_is_whole):
    if law_is_whole:
        return "law"
    return {"note": "note", "xref": "cross-reference"}.get(unit["kind"], "clause")


PURE_XREF = re.compile(r"^\(\s*See\b[^)]*\)\.?$", re.I)


_CUR = {}


def subst_modify(oa, ob, cues_removed, cues_added):
    """A modified unit is substantive unless token-level comparison shows only format/numbering/trivial wording differences."""
    from _textclass import classify
    if cues_removed or cues_added:
        return True
    cls = classify(oa["text"], ob["text"])[0]
    # a changed cross-reference counts, except under the 2017 Code where every reference was renumbered with the Laws
    return cls == "substantive" or (cls == "xref_change" and _CUR.get("b") != "2017")


def unit_fields(u):
    return dict(path=u.get("path", ""), depth=u.get("depth", 1))


def diff_sections(a, b, A, B):
    _CUR["b"] = str(b)
    """Core of the diff for one edition pair. Returns (changes, stats, law_alignment)."""
    changes = []

    def rec(**kw):
        kw.update(edition_from=int(a), edition_to=int(b))
        kw["change_id"] = f"{a}_{b}_{len(changes) + 1:04d}"
        changes.append(kw)

    for L in A + B:  # headings/labels are not rules: keep them out of the unit diff
        L["units"] = [u for u in L["units"] if u["kind"] != "heading"]
    secs = list(OrderedDict.fromkeys([l["section"] for l in A] + [l["section"] for l in B]))
    left_old, left_new, alignment = [], [], []
    whole_old, whole_new = set(), set()
    law_total = [0, 0, 0]
    for sec in secs:
        Am = [l for l in A if l["section"] == sec]
        Bm = [l for l in B if l["section"] == sec]
        if not Am or not Bm:
            side, units = ("added", Bm) if not Am else ("removed", Am)
            for l in units:
                (left_new if not Am else left_old).extend((l, u) for u in l["units"])
            txt = " ".join(u["text"] for l in units for u in l["units"])
            rec(op="add" if not Am else "remove", granularity="section", section=sec, whole_section=True,
                law_from=None if not Am else "*", law_to="*" if not Am else None,
                old_text=None if not Am else txt, new_text=txt if not Am else None, substantive=True)
            (whole_new if not Am else whole_old).update(id(l) for l in units)
            continue
        collapsed = (len(Am) == 1) != (len(Bm) == 1)
        if collapsed:
            def merge(Ls):
                units, k = [], 0
                for l in Ls:
                    for u in l["units"]:
                        units.append(dict(u, unit_idx=k, law_no="0"))
                        k += 1
                return [dict(section=sec, no="0", title="", units=units)]
            Am, Bm = merge(Am), merge(Bm)
        law_pairs = assign_laws(Am, Bm, LAW_MATCH_MIN)
        matchedA = {i for i, _, _ in law_pairs}
        matchedB = {j for _, j, _ in law_pairs}
        law_total[0] += len(law_pairs)
        law_total[1] += len(Am) - len(law_pairs)
        law_total[2] += len(Bm) - len(law_pairs)
        for i, j, s_ in law_pairs:
            la, lb = Am[i], Bm[j]
            alignment.append(dict(section=sec, from_no=la["no"], to_no=lb["no"], similarity=round(s_, 3),
                                  from_title=la["title"], to_title=lb["title"], collapsed=collapsed))
            if la["no"] != lb["no"] or (la["title"] and lb["title"] and la["title"].lower() != lb["title"].lower()):
                rec(op="renumber", granularity="law", section=sec, law_from=la["no"], law_to=lb["no"],
                    title_from=la["title"], title_to=lb["title"], law_similarity=round(s_, 3),
                    old_text=None, new_text=None, substantive=False)
            up = align(la["units"], lb["units"], lambda u: u["text_norm"], UNIT_MATCH_MIN)
            ua = {x for x, _, _ in up}
            ub = {y for _, y, _ in up}
            for x, y, us in up:
                oa, ob = la["units"][x], lb["units"][y]
                if oa["text_norm"] == ob["text_norm"]:
                    continue
                removed, added = cues(oa["text"], ob["text"])
                rec(op="modify", granularity=granularity(ob, False), section=sec, law_from=la["no"], law_to=lb["no"],
                    title_to=lb["title"], kind=ob["kind"], unit_from=oa["unit_idx"], unit_to=ob["unit_idx"],
                    path_from=oa.get("path", ""), path_to=ob.get("path", ""), depth_to=ob.get("depth", 1),
                    similarity=round(us, 3), old_text=oa["text"], new_text=ob["text"], cue_removed=removed,
                    cue_added=added, word_diff=word_diff(oa["text"], ob["text"]),
                    substantive=subst_modify(oa, ob, removed, added))
            lo = [u for k, u in enumerate(la["units"]) if k not in ua]
            ln_ = [u for k, u in enumerate(lb["units"]) if k not in ub]
            while lo and ln_:  # unordered 1:1 re-match inside the Law
                best, bi, bj = 0.0, None, None
                for x, oa in enumerate(lo):
                    for y, ob in enumerate(ln_):
                        sc = sim(oa["text_norm"], ob["text_norm"])
                        if sc > best:
                            best, bi, bj = sc, x, y
                if best < UNIT_MATCH_MIN:
                    break
                oa, ob = lo.pop(bi), ln_.pop(bj)
                removed, added = cues(oa["text"], ob["text"])
                rec(op="modify", granularity=granularity(ob, False), section=sec, law_from=la["no"], law_to=lb["no"],
                    title_to=lb["title"], kind=ob["kind"], unit_from=oa["unit_idx"], unit_to=ob["unit_idx"],
                    path_from=oa.get("path", ""), path_to=ob.get("path", ""), depth_to=ob.get("depth", 1),
                    similarity=round(best, 3), old_text=oa["text"], new_text=ob["text"], cue_removed=removed,
                    cue_added=added, word_diff=word_diff(oa["text"], ob["text"]), reordered=True,
                    substantive=subst_modify(oa, ob, removed, added))
            if lo and ln_:  # re-segmentation: leftovers read as one block on each side
                to, tn = " ".join(u["text"] for u in lo), " ".join(u["text"] for u in ln_)
                sc = sim(norm_(to), norm_(tn))
                if sc >= 0.5:
                    removed, added = cues(to, tn)
                    rec(op="modify", granularity="clause", section=sec, law_from=la["no"], law_to=lb["no"],
                        title_to=lb["title"], kind=ln_[0]["kind"], unit_from=lo[0]["unit_idx"],
                        unit_to=ln_[0]["unit_idx"], path_to=ln_[0].get("path", ""), depth_to=ln_[0].get("depth", 1),
                        similarity=round(sc, 3), old_text=to, new_text=tn, cue_removed=removed, cue_added=added,
                        word_diff=word_diff(to, tn), resegmented=True,
                        substantive=subst_modify({"text": to}, {"text": tn}, removed, added))
                    lo, ln_ = [], []
            left_old += [(la, u) for u in lo]
            left_new += [(lb, u) for u in ln_]
        for i, la in enumerate(Am):
            if i not in matchedA:
                left_old += [(la, u) for u in la["units"]]
                whole_old.add(id(la))
                rec(op="remove", granularity="law", section=sec, law_from=la["no"], law_to=None, title_from=la["title"],
                    old_text=" ".join(u["text"] for u in la["units"]), new_text=None, n_units=len(la["units"]),
                    substantive=True, whole_law=True)
        for j, lb in enumerate(Bm):
            if j not in matchedB:
                left_new += [(lb, u) for u in lb["units"]]
                whole_new.add(id(lb))
                rec(op="add", granularity="law", section=sec, law_from=None, law_to=lb["no"], title_to=lb["title"],
                    old_text=None, new_text=" ".join(u["text"] for u in lb["units"]), n_units=len(lb["units"]),
                    substantive=True, whole_law=True)

    # global move detection among leftovers (units inside wholly added/removed Laws/sections are reported
    # once at Law/section level, but may still be recognised as moves)
    used_new = set()
    for lo, uo in left_old:
        best, bj = 0.0, None
        for k, (ln, un) in enumerate(left_new):
            if k in used_new:
                continue
            s_ = sim(uo["text_norm"], un["text_norm"])
            if s_ > best:
                best, bj = s_, k
        if bj is not None and best >= MOVE_MATCH_MIN:
            used_new.add(bj)
            ln, un = left_new[bj]
            mv_removed, mv_added = cues(uo["text"], un["text"])
            rec(op="move", cue_removed=mv_removed, cue_added=mv_added, granularity=granularity(un, False), section=un["section"], section_from=uo["section"],
                law_from=lo["no"], law_to=ln["no"], title_from=lo["title"], title_to=ln["title"],
                unit_from=uo["unit_idx"], unit_to=un["unit_idx"], path_from=uo.get("path", ""),
                path_to=un.get("path", ""), depth_to=un.get("depth", 1), similarity=round(best, 3),
                old_text=uo["text"], new_text=un["text"], substantive=True)
        elif id(lo) not in whole_old:
            rec(op="remove", granularity=granularity(uo, False), section=lo["section"], law_from=lo["no"], law_to=None,
                title_from=lo["title"], kind=uo["kind"], unit_from=uo["unit_idx"], path_from=uo.get("path", ""),
                old_text=uo["text"], new_text=None, substantive=not (uo["kind"] == "xref" and PURE_XREF.match(uo["text"])))
    for k, (ln, un) in enumerate(left_new):
        if k not in used_new and id(ln) not in whole_new:
            rec(op="add", granularity=granularity(un, False), section=ln["section"], law_from=None, law_to=ln["no"],
                title_to=ln["title"], kind=un["kind"], unit_to=un["unit_idx"], path_to=un.get("path", ""),
                depth_to=un.get("depth", 1), old_text=None, new_text=un["text"],
                substantive=not (un["kind"] == "xref" and PURE_XREF.match(un["text"])))
    ops = ("add", "remove", "modify", "move", "renumber")
    stats = dict(edition_from=int(a), edition_to=int(b), laws_from=sum(1 for l in A), laws_to=sum(1 for l in B),
                 laws_matched=law_total[0], laws_removed=law_total[1], laws_added=law_total[2], n_changes=len(changes),
                 by_op={op: sum(c["op"] == op for c in changes) for op in ops},
                 n_substantive=sum(bool(c.get("substantive")) for c in changes),
                 text_mass_from=sum(len(u["text"]) for l in A for u in l["units"]),
                 text_mass_to=sum(len(u["text"]) for l in B for u in l["units"]))
    return changes, stats, alignment


def main(pairs):
    ALIGN.mkdir(parents=True, exist_ok=True)
    CHANGES.mkdir(parents=True, exist_ok=True)
    for pr in pairs:
        a, b = pr.split(":")
        changes, stats, alignment = diff_sections(a, b, load(a), load(b))
        json.dump(dict(stats=stats, law_alignment=alignment), open(ALIGN / f"{a}_{b}.json", "w"), indent=1,
                  ensure_ascii=False)
        with open(CHANGES / f"{a}_{b}.jsonl", "w", encoding="utf-8") as f:
            for c in changes:
                f.write(json.dumps(c, ensure_ascii=False) + "\n")
        print(a, "->", b, {k: v for k, v in stats.items() if k not in ("edition_from", "edition_to")})


def all_pairs():
    years = sorted(int(p.stem) for p in NODES.glob("*.jsonl"))
    return [f"{x}:{y}" for x, y in zip(years, years[1:])]


if __name__ == "__main__":
    main(sys.argv[1:] or all_pairs())
