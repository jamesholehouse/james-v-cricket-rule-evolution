"""
08b_classify_text_diff.py
Mechanical classification of what an event's text difference amounts to, so human/Claude labelling effort goes to
real changes. Compares the event's concatenated OLD and NEW text after normalisation (lower-case word/number tokens
only, punctuation, quote marks, hyphenation and cross-reference numbers removed):

  format_only     token sequences identical  -> punctuation / quotes / hyphenation / sentence re-splitting / OCR layout
  numbering_only  identical apart from stray list numbers ('2.')
  minor_wording   <= 3 changed tokens, none of them modal/negation/number words (e.g. 'wicket' -> 'pitch')
  substantive     anything else (additions/removals/rewrites or modal/numeric changes)

Whole-Law/section additions and removals and relocations are always 'substantive'/'relocation' (not text-compared).
Adds `text_diff_class` and `changed_tokens` to rule_changes/data/events/<pair>.jsonl.

Usage (from the repo root):
    .venv/bin/python rule_changes/scripts/08b_classify_text_diff.py
"""
import difflib
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).parent))
from _textclass import classify  # noqa: E402

EV = ROOT / "rule_changes/data/events"
CH = ROOT / "rule_changes/data/changes"


def main():
    tot = Counter()
    for p in sorted(EV.glob("*.jsonl"), key=lambda p: int(p.stem.split("_")[0])):
        recs = {}
        for l in open(CH / f"{p.stem}.jsonl", encoding="utf-8"):
            r = json.loads(l)
            recs[r["change_id"]] = r
        events = [json.loads(l) for l in open(p, encoding="utf-8")]
        for e in events:
            if e["event_type"] in ("new_law", "law_removed", "relocation"):
                e["text_diff_class"], e["changed_tokens"] = ("relocation" if e["event_type"] == "relocation" else "substantive"), []
            else:
                rs = [recs[c] for c in e["change_ids"]]
                old = " ".join(r.get("old_text") or "" for r in rs)
                new = " ".join(r.get("new_text") or "" for r in rs)
                e["text_diff_class"], e["changed_tokens"] = classify(old, new)
            tot[(p.stem, e["text_diff_class"])] += 1
        with open(p, "w", encoding="utf-8") as f:
            for e in events:
                f.write(json.dumps(e, ensure_ascii=False) + "\n")
    classes = ["format_only", "numbering_only", "minor_wording", "substantive", "relocation"]
    print("pair".ljust(11), *[c[:9].ljust(9) for c in classes])
    for pair in sorted({k[0] for k in tot}, key=lambda s: int(s.split("_")[0])):
        if int(pair.split("_")[0]) >= 1947:
            print(pair.ljust(11), *[str(tot.get((pair, c), 0)).ljust(9) for c in classes])


if __name__ == "__main__":
    main()
