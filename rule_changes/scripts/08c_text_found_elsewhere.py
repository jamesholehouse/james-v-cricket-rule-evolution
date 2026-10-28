"""
08c_text_found_elsewhere.py
Detects 'moved or re-segmented' text. For each event, every ADDED sentence is looked for (normalised: lower-case words
and numbers, punctuation ignored) anywhere in the whole OLD edition, and every REMOVED sentence anywhere in the whole NEW
edition. If (nearly) all of an event's added/removed text exists in the other edition, the event is a move or a
re-segmentation, not a change of rule.

Adds to rule_changes/data/events/<pair>.jsonl:
  found_elsewhere  fraction (0-1) of the event's added/removed record texts found verbatim in the other edition
  moved_text       True if found_elsewhere >= 0.9 and the event has at least one added/removed record

Usage (from the repo root):
    .venv/bin/python rule_changes/scripts/08c_text_found_elsewhere.py
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EV = ROOT / "rule_changes/data/events"
CH = ROOT / "rule_changes/data/changes"
TXT = ROOT / "data/datasets/rule_texts/processed"


def norm(s):
    s = (s or "").replace("’", "'").lower()
    s = re.sub(r"(\w)-\s*(\w)", r"\1\2", s)
    return " " + " ".join(re.findall(r"[a-z0-9]+", s)) + " "


def main():
    cache = {}

    def full(y):
        if y not in cache:
            cache[y] = norm((TXT / f"{y}_processed.txt").read_text(encoding="utf-8"))
        return cache[y]

    for p in sorted(EV.glob("*.jsonl"), key=lambda p: int(p.stem.split("_")[0])):
        a, b = p.stem.split("_")
        recs = {}
        for l in open(CH / f"{p.stem}.jsonl", encoding="utf-8"):
            r = json.loads(l)
            recs[r["change_id"]] = r
        old_full, new_full = full(a), full(b)
        events = [json.loads(l) for l in open(p, encoding="utf-8")]
        for e in events:
            tested = found = 0
            for c in e["change_ids"]:
                r = recs[c]
                if r["op"] in ("add", "move") and r.get("new_text"):
                    t = norm(r["new_text"])
                    if len(t) > 12:
                        tested += 1
                        found += t in old_full
                if r["op"] in ("remove",) and r.get("old_text"):
                    t = norm(r["old_text"])
                    if len(t) > 12:
                        tested += 1
                        found += t in new_full
            e["found_elsewhere"] = round(found / tested, 2) if tested else None
            e["moved_text"] = bool(tested and found / tested >= 0.9)
        with open(p, "w", encoding="utf-8") as f:
            for e in events:
                f.write(json.dumps(e, ensure_ascii=False) + "\n")
        if int(a) >= 1947:
            n = sum(e["moved_text"] for e in events if e["triage"] == "label" and e["text_diff_class"] == "substantive")
            print(p.stem, "substantive events whose added/removed text exists elsewhere:", n)


if __name__ == "__main__":
    main()
