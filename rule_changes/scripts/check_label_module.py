"""Validate a hand-label module WITHOUT writing any project file.
Usage: .venv/bin/python rule_changes/scripts/check_label_module.py rule_changes/labels/q1830_1835.py
Checks: every event id exists in data/events/<PAIR>.jsonl, no duplicates, and the builder's check() (taxonomy, basis, source ids,
rationale/evidence rules) passes. Prints events of the pair that this module does not label."""
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "rule_changes/labels"))
spec = importlib.util.spec_from_file_location("b", ROOT / "rule_changes/scripts/08_build_labels.py")
b = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)
path = Path(sys.argv[1])
s2 = importlib.util.spec_from_file_location(path.stem, path)
m = importlib.util.module_from_spec(s2)
s2.loader.exec_module(m)
evs = {json.loads(l)["event_id"][-4:]: json.loads(l) for l in open(ROOT / f"rule_changes/data/events/{m.PAIR}.jsonl")}
seen, bad = set(), 0
for l in m.LABELS:
    try:
        assert l["event"] in evs, f"no such event {l['event']}"
        assert l["event"] not in seen, f"duplicate {l['event']}"
        seen.add(l["event"])
        b.check(l, evs[l["event"]])
    except AssertionError as x:
        bad += 1
        print("PROBLEM:", x)
need = [k for k, e in evs.items() if e.get("text_diff_class") not in ("format_only", "numbering_only", "minor_wording", "ocr_noise")]
print(f"{path.name}: {len(m.LABELS)} labels, {bad} problems; events needing a hand label but not in this module: {sorted(set(need) - seen)}")
