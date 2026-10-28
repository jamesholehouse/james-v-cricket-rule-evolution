"""
09_build_datasets.py
Build the two final datasets (rule_changes/data/final/):

  1. changes_all_records_labelled.csv   EVERY change record of every edition pair (1744-2019), each with its own label row.
     Records inside an event inherit the event's hand/mechanical label (label_level = event); records that the grouping step left
     out of every event (format, OCR noise, minor wording, cross-reference-only changes) get a mechanical record-level label from
     the token classifier (label_level = record_mechanical).
  2. substantive_changes.csv            one row per EVENT whose label is a substantive (non-semantic, non-artefact) change:
     substantive_change = 1 in event_labels_all.csv (not NOT_A_CHANGE, not SEMANTIC_WORDING, not a plain wording/terminology rewrite,
     not gender-neutral drafting).

Semantic-only rows (SEMANTIC_WORDING, wording_only, terminology, gender-neutral drafting) are kept in dataset 1 and flagged
semantic_only = 1 so wording information is never lost, but are excluded from dataset 2.

Run after run_pipeline.sh and 08_build_labels.py:  .venv/bin/python rule_changes/scripts/09_build_datasets.py
"""
import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "rule_changes/scripts"))
from _textclass import classify  # noqa: E402

D = ROOT / "rule_changes/data"
OUT = D / "final"
LABELS = D / "categories/event_labels_all.csv"

PURE_XREF = re.compile(r"^\(\s*See\b[^)]*\)\.?$", re.I)
MECH = {   # classifier class -> (category, subtype, semantic_only)
    "format_only": ("NOT_A_CHANGE", "format_artefact", 0),
    "numbering_only": ("NOT_A_CHANGE", "format_artefact", 0),
    "ocr_noise": ("NOT_A_CHANGE", "ocr_noise", 0),
    "minor_wording": ("STRUCTURAL", "wording_only", 1),
    "xref_change": ("STRUCTURAL", "consequential", 0),
}


def record_label(c):
    if c["op"] == "renumber":
        return "NOT_A_CHANGE", "format_artefact", "high", "derived", "Law/clause renumbering only (no text change).", 0
    if c["op"] == "modify":
        cls = classify(c.get("old_text") or "", c.get("new_text") or "")[0]
        if cls in MECH:
            cat, sub, sem = MECH[cls]
            return cat, sub, "medium", "derived", f"Token-level classifier: {cls}.", sem
        return "UNCATEGORISED", "no_cause_stated", "low", "none", "Substantive-looking record outside every event: needs a hand label.", 0
    txt = (c.get("old_text") or c.get("new_text") or "").strip()
    if c["op"] in ("add", "remove") and PURE_XREF.match(txt):
        return "STRUCTURAL", "consequential", "medium", "derived", f"Cross-reference pointer {c['op']}ed ('{txt[:60]}'); no rule text added or removed.", 0
    return "UNCATEGORISED", "no_cause_stated", "low", "none", f"{c['op']} record outside every event: needs a hand label.", 0


def main():
    OUT.mkdir(exist_ok=True)
    lab = {r["event_id"]: r for r in csv.DictReader(open(LABELS))}
    cols = ["pair", "change_id", "op", "section", "law_from", "law_to", "granularity", "old_text", "new_text", "event_id", "label_level",
            "category", "subtype", "confidence", "basis", "what_changed_or_reason", "evidence", "semantic_only", "scope_change", "source_edition_issue", "substantive_change",
            "needs_hand_label"]
    n = Counter()
    with open(OUT / "changes_all_records_labelled.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for p in sorted((D / "changes").glob("*.jsonl"), key=lambda p: int(p.stem.split("_")[0])):
            ev_of = {}
            for l in open(D / "events" / p.name, encoding="utf-8"):
                e = json.loads(l)
                for cid in e["change_ids"]:
                    ev_of[cid] = e["event_id"]
            for l in open(p, encoding="utf-8"):
                c = json.loads(l)
                base = dict(pair=p.stem, change_id=c["change_id"], op=c["op"], section=c.get("section", ""), law_from=c.get("law_from"),
                            law_to=c.get("law_to"), granularity=c.get("granularity", ""), old_text=c.get("old_text") or "",
                            new_text=c.get("new_text") or "", event_id=ev_of.get(c["change_id"], ""))
                el = lab.get(base["event_id"])
                if el:
                    row = dict(base, label_level="event", category=el["category"], subtype=el["subtype"], confidence=el["confidence"],
                               basis=el["basis"], what_changed_or_reason=el["what_changed"], evidence=el["evidence"],
                               semantic_only=el["semantic_only"], scope_change=el["scope_change"], source_edition_issue=el["source_edition_issue"], substantive_change=el["substantive_change"], needs_hand_label=0)
                else:
                    cat, sub, conf, basis, why, sem = record_label(c)
                    hand = int(cat == "UNCATEGORISED")
                    row = dict(base, label_level="event_unlabelled" if base["event_id"] else "record_mechanical", category=cat, subtype=sub,
                               confidence=conf, basis=basis, what_changed_or_reason=why, evidence="S18" if not hand else "",
                               semantic_only=sem, scope_change=0, source_edition_issue=0, substantive_change=int(cat not in ("NOT_A_CHANGE", "STRUCTURAL") and not sem and not hand),
                               needs_hand_label=hand)
                w.writerow(row)
                n[(row["label_level"], row["needs_hand_label"])] += 1
    rows = [r for r in csv.DictReader(open(LABELS))]
    sub = [r for r in rows if r["substantive_change"] == "1"]
    with open(OUT / "substantive_changes.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(sub)
    print("dataset 1 (all records):", dict(n))
    print(f"dataset 2 (substantive events): {len(sub)} of {len(rows)} labelled events; by category {dict(Counter(r['category'] for r in sub))}")


if __name__ == "__main__":
    main()
