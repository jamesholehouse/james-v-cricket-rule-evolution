"""
07_audit_numeric_cues.py
Integrity check on numeric changes. The processed texts were produced by OCR + an AI clean-up pass; where the
OCR was illegible the clean-up can invent a plausible number (found: 1947 ball size "9 to 9 1/8 inches" appears
nowhere in the raw OCR or in the real Law, which says 8 13/16 to 9). A "change" built on such a number is an
artefact, not a rule change.

For every event with a numeric difference, each value that appears only in the NEW text (added) or only in the OLD
text (removed) is checked against
  raw   the raw OCR text of that edition (data/datasets/rule_texts/raw/<year>_raw.txt)
  ref   an independent transcription where we have one:
        1947/1952/1962/1968 -> ACS 1947-code transcriptions (1st, 2nd, 4th edition)
        1980               -> ACS 1980 Code
        2010               -> MCC text of the 2000 Code 4th edition (2010)
Verdict per event: 'supported' (every changed value found in raw or ref), 'suspect' (a changed value found in
neither the raw OCR nor the reference), 'unchecked' (no numeric difference).

Outputs: adds `numeric_audit` to rule_changes/data/events/<pair>.jsonl and writes
         rule_changes/data/events/numeric_audit_summary.csv

Usage (from the repo root):
    .venv/bin/python rule_changes/scripts/07_audit_numeric_cues.py
"""
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EVENTS = ROOT / "rule_changes/data/events"
CHANGES = ROOT / "rule_changes/data/changes"
RAW = ROOT / "data/datasets/rule_texts/raw"
EVT = ROOT / "rule_changes/data/evidence/text"

from _numvals import values  # noqa: E402


def corpus_values(path):
    return set(values(Path(path).read_text(encoding="utf-8", errors="ignore"))) if Path(path).exists() else set()


def raw_values(year):
    """Raw OCR numbers for an edition (1939 is split over two files)."""
    names = [f"{year}_raw.txt"] if (RAW / f"{year}_raw.txt").exists() else [f"{year}a_raw.txt", f"{year}b_raw.txt"]
    s = set()
    for n in names:
        s |= corpus_values(RAW / n)
    return s


def ref_for(year):
    if year in (1947, 1952, 1962, 1968):
        fs = [EVT / "acs_1947.txt", EVT / "acs_1947_second_edition.txt", EVT / "acs_1947_fourth_edition.txt"]
    elif year == 1980:
        fs = [EVT / "acs_1980.txt"]
    elif year == 2010:
        fs = [EVT / "thapos_2000code.txt"]
    else:
        return None
    s = set()
    for f in fs:
        s |= corpus_values(f)
    return s


def audit_event(ev, recs, raw_vals, ref_vals_new, ref_vals_old):
    old = " ".join(r.get("old_text") or "" for r in recs)
    new = " ".join(r.get("new_text") or "" for r in recs)
    vo, vn = values(old), values(new)
    added = sorted({v for v in vn if v not in vo})
    removed = sorted({v for v in vo if v not in vn})
    if not added and not removed:
        return dict(verdict="unchecked", added=[], removed=[], unsupported=[])
    bad = []
    for side, vs, raw, ref in (("added", added, raw_vals[1], ref_vals_new), ("removed", removed, raw_vals[0], ref_vals_old)):
        for v in vs:
            weak = float(v).is_integer() and v <= 30          # small integers occur somewhere in any edition's OCR: no evidence
            if (v in raw and not weak) or (ref and v in ref):
                continue
            if weak and not ref:
                continue                                      # cannot be verified; neither supported nor suspect
            bad.append(dict(side=side, value=v))
    return dict(verdict="suspect" if bad else "supported", added=added, removed=removed, unsupported=bad)


def main():
    rows = []
    for p in sorted(EVENTS.glob("*.jsonl"), key=lambda p: int(p.stem.split("_")[0])):
        a, b = (int(x) for x in p.stem.split("_"))
        recs = {}
        for l in open(CHANGES / f"{p.stem}.jsonl", encoding="utf-8"):
            r = json.loads(l)
            recs[r["change_id"]] = r
        raw_a = raw_values(a)
        raw_b = raw_values(b)
        ref_a, ref_b = ref_for(a), ref_for(b)
        events = [json.loads(l) for l in open(p, encoding="utf-8")]
        for e in events:
            if e["event_type"] in ("new_law", "law_removed", "relocation"):
                e["numeric_audit"] = dict(verdict="unchecked", added=[], removed=[], unsupported=[])
            else:
                e["numeric_audit"] = audit_event(e, [recs[c] for c in e["change_ids"]], (raw_a, raw_b), ref_b, ref_a)
            v = e["numeric_audit"]["verdict"]
            rows.append(dict(pair=p.stem, event_id=e["event_id"], verdict=v, event_type=e["event_type"],
                             law=e.get("law_title"), unsupported=json.dumps(e["numeric_audit"]["unsupported"]),
                             ref_available=int(bool(ref_a or ref_b))))
        with open(p, "w", encoding="utf-8") as f:
            for e in events:
                f.write(json.dumps(e, ensure_ascii=False) + "\n")
    with open(EVENTS / "numeric_audit_summary.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    from collections import Counter
    print(Counter(r["verdict"] for r in rows))
    by = Counter((r["pair"], r["verdict"]) for r in rows if r["verdict"] != "unchecked")
    for pair in sorted({k[0] for k in by}, key=lambda s: int(s.split("_")[0])):
        print(pair, "supported", by.get((pair, "supported"), 0), "suspect", by.get((pair, "suspect"), 0))


if __name__ == "__main__":
    main()
