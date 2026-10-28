"""
01b_segment_eras.py
Segmenters for the editions that 01_segment_laws.py (sequential "N.-" Laws, 1828/1835-1939) does not cover.

Era dispatch:
  headed    1755-1823, 1830, 1820 : unnumbered Laws introduced by a heading ("THE BALL", "The Bat", ...)
  flat      1752                  : no structure at all -> one pseudo-Law of sentences
  postwar   1947-1968             : "(A)" sections, CAPS Law titles, "N.-" per Law, "NOTES" blocks restarting at 1
  modern    1980-2010             : "LAW n TITLE", "k. Subtitle", "(a)", "(i)" nesting
  decimal   2017, 2019            : "LAW n TITLE", "n.m", "n.m.k" decimal clause numbers

Output is written by the same node schema as 01_segment_laws.py, with two extra fields:
  path   clause path where the edition numbers its clauses (e.g. '3(a)(ii)', '1.3.1'), else ''
  depth  nesting depth below the Law (1 = Law-level text, 2 = sub-clause/note, ...)

Usage (from the repo root):
    .venv/bin/python rule_changes/scripts/01b_segment_eras.py            # all non-pilot editions
    .venv/bin/python rule_changes/scripts/01b_segment_eras.py 1947 2019  # selected editions
"""
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TEXT_DIR = ROOT / "data/datasets/rule_texts/processed"
OUT_DIR = ROOT / "rule_changes/data/nodes"

_spec = importlib.util.spec_from_file_location("seg01", Path(__file__).with_name("01_segment_laws.py"))
seg01 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(seg01)
norm, split_sentences, is_heading_text = seg01.norm, seg01.split_sentences, seg01.is_heading_text

ERA = {}
for y in (1752,):
    ERA[y] = "flat"
for y in (1755, 1774, 1785, 1786, 1788, 1803, 1806, 1809, 1816, 1820, 1823, 1830):
    ERA[y] = "headed"
for y in (1828, 1835, 1857, 1884, 1890, 1892, 1896, 1900, 1902, 1906, 1908, 1910, 1911, 1913, 1914, 1918, 1920,
          1923, 1932, 1939):
    ERA[y] = "numbered"  # handled by 01_segment_laws.py
for y in (1947, 1952, 1962, 1968):
    ERA[y] = "postwar"
for y in (1980, 1992, 2000, 2008, 2010):
    ERA[y] = "modern"
for y in (2017, 2019):
    ERA[y] = "decimal"

HEAD_VOCAB = re.compile(
    r"^(?:THE\s+)?(BALL|BAT|STUMPS|BOWLING[\s-]*CREASE|POPPING[\s-]*CREASE|WICKETS?|WICKET[\s-]*KEEPERS?|BOWLERS?|"
    r"STRIKER(?:\s+IS\s+OUT)?|UMPIRES?|PARTY(?:\s+WHICH\s+GOES(?:\s+FROM\s+HOME)?)?|BETS|SINGLE\s+WICKET|"
    r"LAWS?\s+FOR\s+[A-Z\s]+|NOT\s+OUT|NUMBER\s+OF\s+PLAYERS|CHOICE\s+OF\s+GROUND|"
    r"DOUBLE\s+WICKET)\s*[.,]?\s*$", re.I)
INLINE_HEAD = re.compile(
    r"^(THE\s+(?:BALL|BAT|STUMPS|BOWLING\s+CREASE|POPPING\s+CREASE))\s+(?=must\b|Must\b|MUST\b)", re.I)
JUNK = re.compile(r"^(?:-?\s*\d{1,3}\s*-?|THE|CRICKET\.?|L\s?A\s?W\s?S|LAWS|FINIS\.?|THE END\.?|\[\s*\d+\s*\])$", re.I)


def mk(year, section, no, title, idx, kind, text, label="", path="", depth=1):
    return dict(edition=year, section=section, law_no=str(no), law_title=title, unit_idx=idx, kind=kind,
                label=label, text=text, text_norm=norm(text), path=path, depth=depth)


def emit(nodes, year, section, no, title, blocks):
    """blocks: list of (kind, path, depth, label, text) -> nodes with sentence-level units."""
    idx = 0
    for kind, path, depth, label, blob in blocks:
        blob = blob.strip()
        if not blob:
            continue
        for s in split_sentences(blob):
            lab = re.match(r"^\(([a-zA-Z]{1,4})\)\s+", s)
            lbl = label or (lab.group(1).lower() if lab else "")
            if lab:
                s = s[lab.end():]
            k = "heading" if is_heading_text(s) else ("xref" if re.match(r"^\(See\b", s) else kind)
            nodes.append(mk(year, section, no, title, idx, k, s, lbl, path, depth))
            idx += 1


# --------------------------------------------------------------------------- flat / headed
def seg_flat(year, lines):
    blob = "\n".join(lines)
    nodes = []
    emit(nodes, year, "main", "0", "", [("body", "", 1, "", blob)])
    return nodes


def seg_headed(year, lines):
    nodes, cur, laws = [], None, []
    seq = 0
    for ln in lines:
        t = ln.strip()
        if not t:
            if cur is not None:
                cur["lines"].append("")
            continue
        if JUNK.match(t):
            continue
        m = INLINE_HEAD.match(t)
        if HEAD_VOCAB.match(t) or (year == 1830 and re.match(r"^[A-Z][A-Za-z ]{2,26}[.,]$", t) and len(t.split()) <= 4):
            seq += 1
            cur = dict(no=str(seq), title=re.sub(r"[.,]$", "", t).strip(), lines=[])
            laws.append(cur)
        elif m:
            seq += 1
            cur = dict(no=str(seq), title=m.group(1).strip(), lines=[t[m.end():]])
            laws.append(cur)
        else:
            if cur is None:
                seq += 1
                cur = dict(no=str(seq), title="", lines=[])
                laws.append(cur)
            cur["lines"].append(t)
    for L in laws:
        emit(nodes, year, "main", L["no"], L["title"], [("body", "", 1, "", "\n".join(L["lines"]))])
    return nodes


# --------------------------------------------------------------------------- postwar (1947-1968)
SEC_HEAD = re.compile(r"^\(([A-F])\)\s*[—–-]+\s*(.*)$")
PW_MARK = re.compile(r"^(\d{1,2})\s*[.,]?\s*[—–-]+\s*(.*)$")
PW_NOTE = re.compile(r"^NOTES?\.?\s*\W*$", re.I)
CAPS_TITLE = re.compile(r"^[A-Z][A-Z ,'’&-]{2,60}\.?$")


def seg_postwar(year, lines):
    nodes, section_letter = [], ""
    laws = []
    cur = None
    law_no, in_notes, last_note, pending_title = 0, False, 0, ""
    for ln in lines:
        t = ln.strip()
        if not t or JUNK.match(t):
            continue
        sm = SEC_HEAD.match(t)
        if sm:
            section_letter = sm.group(1)
            pending_title, in_notes = "", False
            continue
        if PW_NOTE.match(t):
            in_notes, last_note = True, 0
            if cur is not None:
                cur["blocks"].append(["note", "", 2, "", ""])
            continue
        if CAPS_TITLE.match(t) and not PW_MARK.match(t):
            pending_title = (pending_title + " " + t.rstrip(".")).strip() if pending_title else t.rstrip(".")
            in_notes = False
            continue
        m = PW_MARK.match(t)
        if m:
            n, rest = int(m.group(1)), m.group(2)
            new_law = False
            if n == law_no + 1 and (not in_notes or pending_title or n != last_note + 1):
                new_law = True
            elif pending_title and law_no < n <= law_no + 3:
                new_law = True  # a Law number the OCR dropped
            if new_law:
                law_no, in_notes, last_note = n, False, 0
                cur = dict(no=str(n), title=pending_title, section=section_letter, blocks=[["body", str(n), 1, "", rest]])
                laws.append(cur)
                pending_title = ""
            elif cur is not None:
                if in_notes:
                    last_note = n
                    cur["blocks"].append(["note", f"N{n}", 2, "", rest])
                else:
                    cur["blocks"].append(["body", str(n), 1, "", rest])
            continue
        if cur is not None:
            cur["blocks"][-1][4] += "\n" + t
        else:
            pass
    for L in laws:
        emit(nodes, year, "main", L["no"], L["title"], [tuple(b) for b in L["blocks"]])
    return nodes


# --------------------------------------------------------------------------- modern (1980-2010) and decimal (2017-2019)
LAW_HEAD = re.compile(r"^LAW\s+(\d{1,2})\b\s*(.*)$")
APPX = re.compile(r"^APPENDIX\s+([A-Z])\b\s*(.*)$")
ROMAN = r"(?:i|ii|iii|iv|v|vi|vii|viii|ix|x|xi|xii|xiii|xiv|xv)"
M_NUM = re.compile(r"^(\d{1,2})\.\s+(\S.*)$")
M_ALPHA = re.compile(r"^\(([a-h])\)\s+(.*)$")
M_ROMAN = re.compile(rf"^\(({ROMAN})\)\s+(.*)$")
D_NUM = re.compile(r"^(\d{1,2}(?:\.\d{1,2}){1,4})\s+(\S.*)$")


def seg_laws_generic(year, lines, decimal):
    nodes, laws = [], []
    section, cur = "PREAMBLE", None
    sec_lines = []
    appendix_name = None

    def start_law(no, title, sec):
        nonlocal cur
        cur = dict(no=no, title=title, section=sec, blocks=[], titling=True)
        laws.append(cur)

    start_law("0", "", "PREAMBLE")
    cur_sub = cur_alpha = cur_roman = ""
    for ln in lines:
        t = ln.strip()
        if not t or re.match(r"^\d{1,3}$", t):
            continue
        am = APPX.match(t)
        if am:
            appendix_name = f"APPENDIX {am.group(1)}"
            start_law(am.group(1), am.group(2).strip(), "APPENDIX")
            cur["titling"] = False
            cur_sub = cur_alpha = cur_roman = ""
            continue
        lm = LAW_HEAD.match(t)
        if lm and not (cur is not None and cur["section"] == "APPENDIX" and False):
            start_law(lm.group(1), lm.group(2).strip(), "main")
            cur_sub = cur_alpha = cur_roman = ""
            continue
        if cur is None:
            continue
        # multi-line CAPS titles directly after "LAW n"
        if cur["titling"] and cur["section"] == "main" and t.isupper() and not D_NUM.match(t) and not M_NUM.match(t):
            cur["title"] = (cur["title"] + " " + t).strip()
            continue
        cur["titling"] = False
        if t.upper() in ("NOTES", "NOTE"):
            cur["blocks"].append(["note", "", 2, "", ""])
            continue
        if decimal and cur["section"] == "main":
            dm = D_NUM.match(t)
            if dm:
                path, rest = dm.group(1), dm.group(2)
                first = int(path.split(".")[0])
                if cur["no"].isdigit() and int(cur["no"]) < first <= int(cur["no"]) + 2 and first <= 42:
                    start_law(str(first), "", "main")  # LAW heading missing in the source text
                    cur["titling"] = False
                cur["blocks"].append(["body", path, path.count(".") + 0, "", rest])
                continue
        elif cur["section"] == "main" or cur["section"] == "PREAMBLE":
            nm, am_, rm = M_NUM.match(t), M_ALPHA.match(t), M_ROMAN.match(t)
            if nm and (cur["section"] != "main" or int(nm.group(1)) <= 30):
                cur_sub, cur_alpha, cur_roman = nm.group(1), "", ""
                cur["blocks"].append(["body", cur_sub, 1, "", nm.group(2)])
                continue
            if rm and (cur_alpha or True) and rm.group(1) not in ("i", "v", "x") or (rm and cur_alpha):
                cur_roman = rm.group(1)
                cur["blocks"].append(["body", f"{cur_sub}({cur_alpha})({cur_roman})", 3, "", rm.group(2)])
                continue
            if am_:
                cur_alpha, cur_roman = am_.group(1), ""
                cur["blocks"].append(["body", f"{cur_sub}({cur_alpha})", 2, "", am_.group(2)])
                continue
        if not cur["blocks"]:
            cur["blocks"].append(["body", "", 1, "", t])
        else:
            cur["blocks"][-1][4] += "\n" + t
    for L in laws:
        sec = L["section"]
        no = L["no"]
        emit(nodes, year, sec, no, L["title"], [tuple(b) for b in L["blocks"]])
    return nodes


def segment(year):
    era = ERA[year]
    lines = (TEXT_DIR / f"{year}_processed.txt").read_text(encoding="utf-8").splitlines()
    if era == "flat":
        return seg_flat(year, lines)
    if era == "headed":
        return seg_headed(year, lines)
    if era == "postwar":
        return seg_postwar(year, lines)
    if era == "modern":
        return seg_laws_generic(year, lines, decimal=False)
    if era == "decimal":
        return seg_laws_generic(year, lines, decimal=True)
    raise ValueError(f"{year}: era {era} handled by 01_segment_laws.py")


def main(years):
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for y in years:
        y = int(y)
        if ERA[y] == "numbered":
            continue
        nodes = segment(y)
        with open(OUT_DIR / f"{y}.jsonl", "w", encoding="utf-8") as f:
            for n in nodes:
                f.write(json.dumps(n, ensure_ascii=False) + "\n")
        laws = {(n["section"], n["law_no"]) for n in nodes}
        mains = sorted(int(n) for s, n in laws if s == "main" and n.isdigit())
        print(f"{y} [{ERA[y]}]: {len(nodes)} units, {len(laws)} laws/blocks; main Laws {mains[0] if mains else '-'}..{mains[-1] if mains else '-'} "
              f"({len(mains)}); sections {sorted({s for s, _ in laws})}")


if __name__ == "__main__":
    main(sys.argv[1:] or [y for y, e in sorted(ERA.items()) if e != "numbered"])
