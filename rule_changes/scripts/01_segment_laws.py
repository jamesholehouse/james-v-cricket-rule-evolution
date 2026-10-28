"""
01_segment_laws.py
Segment each edition's processed text into Laws and within-Law units, writing one
JSONL of nodes per edition. Pilot coverage: editions whose Laws are introduced by
a sequential "N.", "N.-" or "N.--" marker (1884-1939); other eras need their own rules.

Node fields:
  edition, section (main | appendix name), law_no (as printed, str), law_title (str, may be ''),
  unit_idx, kind (body | note | sub), label (e.g. '1st', '(a)', ''), text, text_norm

Usage (from the repo root):
    .venv/bin/python rule_changes/scripts/01_segment_laws.py 1884 1890 1892 1896 1900 1932 1939
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TEXT_DIR = ROOT / "data/datasets/rule_texts/processed"
OUT_DIR = ROOT / "rule_changes/data/nodes"

# Headings that open an appendix-style section with its own 1..n numbering.
SECTION_HEADS = {
    "ONE DAY MATCHES": "ONE DAY MATCHES",
    "ONE-DAY MATCHES": "ONE DAY MATCHES",
    "SINGLE WICKET": "SINGLE WICKET",
    "THE BATSMAN": "THE BATSMAN",
    "THE BOWLER": "THE BOWLER",
    "THE BOWLERS": "THE BOWLER",
    "THE BOUNDARY": "THE BOUNDARY",
    "UMPIRES": "UMPIRES",
    "NOTES FOR SCORERS AND UMPIRES": "NOTES FOR SCORERS AND UMPIRES",
    "INSTRUCTIONS TO UMPIRES": "INSTRUCTIONS TO UMPIRES",
}

LAW_MARK = re.compile(r"^(\d{1,2})([a-zA-Z]?)(?:\s*\.\s*[—–\-]*\s*|\s+)(?=[A-Za-z\"“(‘'])")
INLINE_TITLE_MARK = re.compile(r"^(?P<title>[A-Z][A-Za-z'\u2019 ]{2,30}?)\s+(?P<n>\d{1,2})(?P<l>[a-zA-Z]?)\s*\.\s*[\u2014\u2013\-]+\s*(?=\S)")
NOTE_HEAD = re.compile(r"^(?:NOTES?\b.*|Notes?\b.*|\(See also[^)]*\))\s*$")
CLAUSE_MARK = re.compile(r"(?:(?<=\s)|^)(1st|2nd|3rd|4th)\s*[—–\-,.]?\s")


def norm(s: str) -> str:
    """Normalised comparison key: unify quotes/dashes/case/whitespace, drop line-wrap hyphens."""
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = re.sub(r"[—–]", "-", s)
    s = re.sub(r"(\w)-\s*\n\s*(\w)", r"\1\2", s)
    s = re.sub(r"\s+", " ", s).strip().lower()
    return s


def is_title_line(line: str) -> bool:
    t = line.strip().strip("\u201c\u201d\"").rstrip(".").strip("\u201c\u201d\"").strip()
    if not t or len(t) > 60 or re.search(r"\d", t):
        return False
    letters = [c for c in t if c.isalpha()]
    return bool(letters) and (t.isupper() or t.istitle())


SMALL = {"of", "and", "the", "to", "a", "in", "on", "for", "or", "at", "by", "off", "no", "from", "with"}


def is_heading_text(s: str) -> bool:
    """Short title-like fragment (e.g. 'Appointment of Umpires.', 'NOTES.', 'Either batsman is out\u2014')."""
    t = s.strip().strip("\u201c\u201d\"").strip()
    core = t.rstrip(".:\u2014\u2013- ").strip()
    if re.match(r"^(Notes?|NOTES?)( on Laws?)?\b[^.]{0,30}$", core):
        return True
    if not core or len(core) > 48 or re.search(r"\d", core):
        return False
    words = re.findall(r"[A-Za-z']+", core)
    if not words:
        return False
    if core.isupper():
        return True
    if re.match(r"^(Notes?|Note on Laws?)\b", core):
        return True
    caps = [w for w in words if w[0].isupper() or w.lower() in SMALL]
    if len(caps) == len(words) and len(words) <= 6:
        return True
    # lead-in to a list of clauses, e.g. "Either batsman is out\u2014"
    return t.endswith(("\u2014", ":", ":\u2014")) and len(words) <= 8 and "," not in t


def split_sentences(text: str):
    """Split a Law body into units: sentences, additionally breaking at 1st/2nd clause markers."""
    text = re.sub(r"(\w)-\s*\n\s*(\w)", r"\1\2", text)
    text = re.sub(r"\s*\n\s*", " ", text).strip()
    text = CLAUSE_MARK.sub(lambda m: "\u0001" + m.group(1) + " ", text)
    parts = []
    for chunk in text.split("\u0001"):
        chunk = chunk.strip()
        if not chunk:
            continue
        # sentence split: period/semicolon-colon not followed by lowercase; avoid 'Law 3.' abbreviations
        sub = re.split(r"(?<=[.!?”\"\)])\s+(?=[A-Z\"“(])|(?<=[.!?”\"\)])\s+(?=\([a-z]\)\s)", chunk)
        parts.extend(s.strip() for s in sub if s.strip())
    return parts


def segment(year: int):
    raw = (TEXT_DIR / f"{year}_processed.txt").read_text(encoding="utf-8")
    lines = [re.sub(r"^\s*I\s*\.\s*([\u2014\u2013-])", r"1.\1", ln) for ln in raw.splitlines()]  # OCR reads "1." as "I."
    nodes, section, expected = [], "main", 1
    cur = None  # current Law dict
    pending_title = ""

    def flush():
        nonlocal cur
        if cur is None:
            return
        body_lines, note_lines, in_note = [], [], False
        for ln in cur["lines"]:
            if NOTE_HEAD.match(ln.strip()) and not ln.strip().startswith("(a)"):
                in_note = True
                note_lines.append(ln)
                continue
            (note_lines if in_note else body_lines).append(ln)
        idx = 0
        for kind, blk in (("body", body_lines), ("note", note_lines)):
            blob = "\n".join(blk).strip()
            if not blob:
                continue
            for s in split_sentences(blob):
                lab = re.match(r"^\(([a-zA-Z])\)\s+", s)
                label = lab.group(1).lower() if lab else ""
                if lab:
                    s = s[lab.end():]
                k = "heading" if is_heading_text(s) else ("xref" if re.match(r"^\(See\b", s) else kind)
                nodes.append(dict(edition=year, section=cur["section"], law_no=cur["no"], law_title=cur["title"],
                                  unit_idx=idx, kind=k, label=label, text=s, text_norm=norm(s)))
                idx += 1
        cur = None

    last_letter = ""
    for i, ln in enumerate(lines):
        stripped = ln.strip()
        head = SECTION_HEADS.get(stripped.rstrip(".").upper())
        if head and expected >= 45 and section == "main" or (head and section != "main" and head != section and expected > 1):
            flush()
            section, expected, pending_title, last_letter = head, 1, "", ""
            continue
        m = LAW_MARK.match(stripped)
        im = INLINE_TITLE_MARK.match(stripped) if not m else None
        if m or im:
            if im:
                n, letter = int(im.group("n")), im.group("l")
                end, inline_title = im.end(), im.group("title")
            else:
                n, letter = int(m.group(1)), m.group(2)
                end, inline_title = m.end(), ""
            letter = letter.lower()
            ok_new = expected <= n <= expected + 2 and (not letter or letter == "a")
            ok_letter = letter and n == expected - 1 and letter > last_letter and cur is not None
            if ok_new or ok_letter:
                flush()
                no = f"{n}{letter}"
                cur = dict(no=no, title=inline_title or pending_title, section=section, lines=[stripped[end:]])
                pending_title = ""
                if ok_new:
                    expected = n + 1
                last_letter = letter
                continue
        if is_title_line(stripped) and (i + 1 < len(lines)) and not NOTE_HEAD.match(stripped):
            nxt = next((l.strip() for l in lines[i + 1:i + 4] if l.strip()), "")
            nm = LAW_MARK.match(nxt)
            if nm and expected <= int(nm.group(1)) <= expected + 2:
                pending_title = stripped.strip("\u201c\u201d\"").rstrip(".").strip("\u201c\u201d\"")
                continue
        if cur is not None:
            cur["lines"].append(ln)
    flush()
    return nodes


def main(years):
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for y in years:
        nodes = segment(int(y))
        with open(OUT_DIR / f"{y}.jsonl", "w", encoding="utf-8") as f:
            for n in nodes:
                f.write(json.dumps(n, ensure_ascii=False) + "\n")
        laws = {(n["section"], n["law_no"]) for n in nodes}
        main_laws = sorted(int(re.sub(r"\D", "", ln)) for s, ln in laws if s == "main")
        print(f"{y}: {len(nodes)} units, {len(laws)} laws (main 1..{main_laws[-1] if main_laws else '-'}); sections:",
              sorted({s for s, _ in laws}))


if __name__ == "__main__":
    main(sys.argv[1:] or ["1884", "1890", "1892", "1896", "1900", "1932", "1939"])
