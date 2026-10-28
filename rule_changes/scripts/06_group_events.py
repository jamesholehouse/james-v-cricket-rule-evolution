"""
06_group_events.py
Group the candidate change records of each edition pair into change EVENTS: one event = one coherent edit to one
Law (adjacent clauses of the same Law, or one whole Law added/removed, or one block of clauses moved).
Events are the unit that gets a category and evidence (07_*), not the individual sentence records.

Mechanical event types (no causes are inferred here):
  numeric_change   a number or number-word in the rule changed (e.g. five -> six, 15 -> 10)
  new_provision    clauses added, nothing removed/modified
  removed_provision clauses removed, nothing added/modified
  revision         existing clauses substantially rewritten (similarity < REWORD_SIM) or a mixture
  rewording        only light rewording (similarity >= REWORD_SIM) and no numeric cue
  new_law / law_removed   a whole Law (or section) added / removed
  relocation       clauses moved between Laws/sections unchanged
Events of type 'rewording' are kept but flagged triage='wording_only' (not queued for labelling).

Inputs : rule_changes/data/changes/<a>_<b>.jsonl, rule_changes/data/law_identity/law_nodes.csv
Output : rule_changes/data/events/<a>_<b>.jsonl

Usage (from the repo root):
    .venv/bin/python rule_changes/scripts/06_group_events.py              # all pairs
    .venv/bin/python rule_changes/scripts/06_group_events.py 1992_2000
"""
import csv
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHANGES = ROOT / "rule_changes/data/changes"
EVENTS = ROOT / "rule_changes/data/events"
LAW_NODES = ROOT / "rule_changes/data/law_identity/law_nodes.csv"
GAP = 3             # clause positions apart that still count as the same event
REWORD_SIM = 0.85   # modifies at least this similar (and without numeric cues) are wording-only
DIGEST = 700        # characters of old/new text kept in the event digest


def load_canon():
    m = {}
    for r in csv.DictReader(open(LAW_NODES)):
        m[(int(r["edition"]), r["section"], r["law_no"])] = (r["canonical_id"], r["title"])
    return m


def pos(c):
    u = c.get("unit_to")
    if u is None:
        u = c.get("unit_from")
    return -1 if u is None else u


def classify(recs):
    ops = Counter(c["op"] for c in recs)
    has_cue = any(c.get("cue_added") or c.get("cue_removed") for c in recs)
    mods = [c for c in recs if c["op"] == "modify"]
    mean_sim = sum(c.get("similarity", 0) for c in mods) / len(mods) if mods else None
    if any(c.get("whole_law") or c.get("whole_section") for c in recs):
        return "new_law" if ops.get("add") else "law_removed"
    if set(ops) == {"move"} and not has_cue:
        return "relocation"
    if has_cue:
        return "numeric_change"
    if set(ops) == {"add"}:
        return "new_provision"
    if set(ops) == {"remove"}:
        return "removed_provision"
    if set(ops) == {"modify"} and mean_sim is not None and mean_sim >= REWORD_SIM:
        return "rewording"
    return "revision"


def digest(recs, side):
    key = "old_text" if side == "old" else "new_text"
    parts = [c[key] for c in recs if c.get(key)]
    t = " ".join(parts)
    return t[:DIGEST] + (" ..." if len(t) > DIGEST else "")


def group_pair(a, b, canon):
    recs = [json.loads(l) for l in open(CHANGES / f"{a}_{b}.jsonl", encoding="utf-8")]
    sub = [c for c in recs if c.get("substantive")]
    buckets = defaultdict(list)
    for c in sub:
        if c.get("whole_law") or c.get("whole_section"):
            buckets[("whole", c["change_id"])].append(c)
            continue
        if c["op"] == "move":
            key = ("move", c.get("section_from"), c.get("law_from"), c.get("section"), c.get("law_to"))
        else:
            sec = c.get("section", "main")
            ln = c.get("law_to") if c.get("law_to") is not None else c.get("law_from")
            cid = canon.get((int(b), sec, ln) if c.get("law_to") is not None else (int(a), sec, ln), (None, ""))[0]
            key = ("law", sec, cid or f"?{ln}")
        buckets[key].append(c)
    events = []
    for key, rs in buckets.items():
        rs.sort(key=pos)
        clusters, cur = [], [rs[0]]
        for c in rs[1:]:
            if pos(c) - pos(cur[-1]) <= GAP or key[0] != "law":
                cur.append(c)
            else:
                clusters.append(cur)
                cur = [c]
        clusters.append(cur)
        for cl in clusters:
            events.append(cl)
    out = []
    for cl in sorted(events, key=lambda cl: (str(cl[0].get("section")), str(cl[0].get("law_to") or cl[0].get("law_from")), pos(cl[0]))):
        etype = classify(cl)
        c0 = cl[0]
        sec = c0.get("section", "main")
        ln_to, ln_from = c0.get("law_to"), c0.get("law_from")
        cid, title = canon.get((int(b), sec, ln_to), (None, "")) if ln_to is not None else (None, "")
        if cid is None and ln_from is not None:
            cid, title = canon.get((int(a), sec, ln_from), (None, ""))
        mods = [c for c in cl if c["op"] == "modify"]
        out.append(dict(
            event_id=f"{a}_{b}_E{len(out) + 1:03d}", edition_from=int(a), edition_to=int(b), section=sec,
            canonical_law=cid, law_title=(c0.get("title_to") or c0.get("title_from") or title or ""),
            law_from=ln_from, law_to=ln_to, event_type=etype,
            triage="wording_only" if etype == "rewording" else "label",
            n_records=len(cl), ops=dict(Counter(c["op"] for c in cl)),
            mean_similarity=round(sum(c.get("similarity", 0) for c in mods) / len(mods), 3) if mods else None,
            cue_removed=sorted({t for c in cl for t in c.get("cue_removed", [])}),
            cue_added=sorted({t for c in cl for t in c.get("cue_added", [])}),
            chars_old=sum(len(c.get("old_text") or "") for c in cl), chars_new=sum(len(c.get("new_text") or "") for c in cl),
            depth_to=min((c.get("depth_to", 1) for c in cl if c.get("depth_to")), default=None),
            granularity=sorted({c.get("granularity") for c in cl}),
            old_digest=digest(cl, "old"), new_digest=digest(cl, "new"),
            change_ids=[c["change_id"] for c in cl]))
    return out, len(recs), len(sub)


def main(pairs):
    EVENTS.mkdir(parents=True, exist_ok=True)
    canon = load_canon()
    tot = Counter()
    for p in pairs:
        a, b = p.split("_")
        ev, n, nsub = group_pair(a, b, canon)
        with open(EVENTS / f"{p}.jsonl", "w", encoding="utf-8") as f:
            for e in ev:
                f.write(json.dumps(e, ensure_ascii=False) + "\n")
        c = Counter(e["event_type"] for e in ev)
        q = sum(e["triage"] == "label" for e in ev)
        tot.update(c)
        print(f"{p}: {n} records / {nsub} substantive -> {len(ev)} events ({q} to label)  {dict(c)}")
    print("TOTAL", dict(tot))


if __name__ == "__main__":
    pairs = sys.argv[1:] or sorted((p.stem for p in CHANGES.glob("*.jsonl")), key=lambda s: int(s.split("_")[0]))
    main(pairs)
