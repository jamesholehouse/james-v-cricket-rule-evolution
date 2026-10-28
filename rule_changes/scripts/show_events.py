"""Print the events of an edition pair with their old/new text, for hand labelling.
Usage: .venv/bin/python rule_changes/scripts/show_events.py 1830_1835 [--unlabelled] [--max-records 6] [--chars 300]
Event ids are those of the current pipeline output (labels/q<pair>.py must use them). Read-only."""
import csv
import json
import sys
from pathlib import Path

R = Path(__file__).resolve().parents[1] / "data"
args = [a for a in sys.argv[1:] if not a.startswith("--")]
flags = sys.argv[1:]
maxrec = int(flags[flags.index("--max-records") + 1]) if "--max-records" in flags else 6
chars = int(flags[flags.index("--chars") + 1]) if "--chars" in flags else 300
pair = args[0]
unl = {(r["pair"], r["event"]) for r in csv.DictReader(open(R / "categories/unlabelled_events.csv"))}
recs = {json.loads(l)["change_id"]: json.loads(l) for l in open(R / f"changes/{pair}.jsonl", encoding="utf-8")}
for l in open(R / f"events/{pair}.jsonl", encoding="utf-8"):
    e = json.loads(l)
    k = e["event_id"][-4:]
    if "--unlabelled" in flags and (pair, k) not in unl:
        continue
    print(f"=== {pair} {k} {e['event_type']} Law {e['law_from']}->{e['law_to']} {e['law_title'][:30]} n={e['n_records']} cls={e.get('text_diff_class')} audit={e['numeric_audit']['verdict']} changed={e.get('changed_tokens', [])[:8]}")
    for cid in e["change_ids"][:maxrec]:
        c = recs[cid]
        print(f"  [{c['op']}] {cid[-4:]} OLD: {(c.get('old_text') or '')[:chars]}")
        print(f"            NEW: {(c.get('new_text') or '')[:chars]}")
    if e["n_records"] > maxrec:
        print(f"  ... +{e['n_records'] - maxrec} more records (use --max-records)")
