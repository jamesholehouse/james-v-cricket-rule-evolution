"""
08_build_labels.py
Assemble the post-1947 event labels: hand-written labels (rule_changes/labels/*.py) + mechanical labels for events
whose text differs only in format/numbering/trivial wording (08b). Validates every label against the taxonomy and the
source registry, then writes rule_changes/data/categories/post1947_event_labels.csv and a coverage report.

Rules enforced ("no claim without evidence"):
  * every label other than UNCATEGORISED needs a rationale and at least one registered source id;
  * UNCATEGORISED must have basis 'none';
  * NOT_A_CHANGE labels must have basis 'derived';
  * evidence ids must exist in data/evidence/sources.csv; category/subtype must exist in schema/taxonomy_v0.json.

Usage (from the repo root):
    .venv/bin/python rule_changes/scripts/08_build_labels.py
"""
import csv
import re
import hashlib
import importlib.util
import json
import sys
from collections import Counter

from rapidfuzz import fuzz
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "rule_changes/labels"))
TAX = json.load(open(ROOT / "rule_changes/schema/taxonomy_v0.json"))
CATS = TAX["categories"]
BASIS = set(TAX["basis_values"])
SOURCES = {r["id"] for f_ in [ROOT / "rule_changes/data/evidence/sources.csv", *sorted((ROOT / "rule_changes/data/evidence").glob("new_sources_*.csv"))] for r in csv.DictReader(open(f_))}
OUT = ROOT / "rule_changes/data/categories/event_labels_all.csv"
OUT_POST = ROOT / "rule_changes/data/categories/post1947_event_labels.csv"
FIRST_YEAR = 1744


KEYFILE = ROOT / "rule_changes/labels/keys.json"
OVERRIDES = ROOT / "rule_changes/labels/overrides.json"
VERDICTS = ROOT / "rule_changes/data/review/verdicts.jsonl"


def load_verdicts():
    """Human verdicts written by review_app/server.py (append-only; the last record per event wins)."""
    v = {}
    if VERDICTS.exists():
        for l in open(VERDICTS, encoding="utf-8"):
            if l.strip():
                r = json.loads(l)
                v[r["event_id"]] = r
    return v


VERD = load_verdicts()


def load_overrides():
    """Verification-driven corrections applied to a resolved label (hand or mechanical) after the fact, keyed by event id and guarded by the
    event's content signature so they cannot attach to a different event after a pipeline change. See labels/overrides.json."""
    return {o["event_id"]: o for o in json.load(open(OVERRIDES))} if OVERRIDES.exists() else {}


def apply_override(l, e, ov, problems):
    o = ov.get(e["event_id"])
    if not o:
        return l
    if o["sig"] != sig(e):
        problems.append(f"{e['event_id']}: override skipped (event content changed since it was written)")
        return l
    l = dict(l)
    for k, v in o.get("set", {}).items():
        l[k] = v
    for k, v in o.get("append", {}).items():
        l[k] = (l[k] + " " if l.get(k) else "") + v
    for k, (a, b) in o.get("replace", {}).items():
        assert a in l[k], (e["event_id"], k, a[:40])
        l[k] = l[k].replace(a, b)
    l["notes"] = (l["notes"] + " " if l["notes"] else "") + "Corrected after verification: " + o.get("why", "")
    return l



def rec_hash(r):
    return hashlib.md5(f"{r['op']}|{r.get('law_from')}|{r.get('law_to')}|{r.get('old_text')}|{r.get('new_text')}".encode()).hexdigest()[:10]


def sig(e):
    """Stable content signature of an event (kept for the CSV; resolution uses record overlap, see resolve())."""
    s = f"{e['edition_from']}|{e['edition_to']}|{e['law_from']}|{e['law_to']}|{e['old_digest'][:300]}|{e['new_digest'][:300]}"
    return hashlib.md5(s.encode()).hexdigest()[:12]


def load_events(pair):
    recs = {}
    for l in open(ROOT / f"rule_changes/data/changes/{pair}.jsonl", encoding="utf-8"):
        r = json.loads(l)
        recs[r["change_id"]] = r
    evs = []
    for l in open(ROOT / f"rule_changes/data/events/{pair}.jsonl", encoding="utf-8"):
        e = json.loads(l)
        e["_hashes"] = [rec_hash(recs[c]) for c in e["change_ids"]]
        evs.append(e)
    return evs


def dg(e):
    return re.sub(r"[^a-z0-9 ]", " ", (e["old_digest"][:300] + " || " + e["new_digest"][:300]).lower())


def resolve(labels, evs, keys, pair):
    """Attach each hand label to the event that holds most of the change records the label was written for.
    Labels are authored against event ids of some pipeline run; after the pipeline changes ids shift, but the
    records (op|old|new) persist, so the label follows its records. Returns {event_id: label}, problems."""
    by_id = {e["event_id"][-4:]: e for e in evs}
    out, problems, claimed = {}, [], {}
    for l in labels:
        # p* modules are keyed 'pair:Exxx' (ids of the pipeline run they were written against); n* modules, written
        # against a later run, are keyed 'pair:n:Exxx' so the two id spaces cannot collide
        f_ = l.get("_file", "p")
        k = f"{pair}:{l['event']}" if f_.startswith("p") else f"{pair}:{re.match(r'[nq][a-z]?', f_).group(0)}:{l['event']}"
        if k not in keys:  # authored against the current pipeline output: record its keys now
            e = by_id.get(l["event"])
            if e is None:
                problems.append(f"{k}: no such event and no saved keys")
                continue
            keys[k] = dict(records=e["_hashes"], law_from=e["law_from"], law_to=e["law_to"], section=e["section"],
                           digest=dg(e))
        old = set(keys[k]["records"])
        best, bo = None, 0.0
        for e in evs:
            if e["section"] != keys[k]["section"] and e["law_to"] != keys[k]["law_to"] and e["law_from"] != keys[k]["law_from"]:
                continue
            ov = len(old & set(e["_hashes"])) / max(1, len(old))
            if ov > bo:
                best, bo = e, ov
        if (best is None or bo < 0.5) and keys[k].get("digest"):
            # fallback: the records changed text (e.g. sentence re-splitting) - match on the event digest in the same Law
            fb, fs = None, 0.0
            for e in evs:
                if keys[k]["law_to"] != e["law_to"] and keys[k]["law_from"] != e["law_from"]:
                    continue
                sc = fuzz.token_sort_ratio(keys[k]["digest"], dg(e))
                if sc > fs:
                    fb, fs = e, sc
            if fb is not None and fs >= 75:
                best, bo = fb, 0.5 + (fs - 75) / 100
        if best is None or bo < 0.5:
            problems.append(f"{k}: label's records not found in any current event (best overlap {bo:.2f})")
            continue
        eid = best["event_id"]
        if eid in claimed:
            # two hand labels now belong to one event (the pipeline merged what they were written for): keep both
            (obo, ok), (ol, _) = claimed[eid], out[eid]
            l["_ref"] = f"{l.get('_file', '?')}:{l['event']}"
            a, b = ((ol, ok), (l, k)) if (real(ol), not is_semantic(ol), obo) >= (real(l), not is_semantic(l), bo) else ((l, k), (ol, ok))
            out[eid] = (merge_labels(a[0], b[0], a[1], b[1]), max(bo, obo))
            claimed[eid] = (max(bo, obo), a[1] + "+" + b[1])
            problems.append(f"{ok if k == b[1] else k} and {k if k == b[1] else ok}: merged into event {eid} (both labels kept)")
            continue
        claimed[eid] = (bo, k)
        l["_ref"] = f"{l.get('_file', '?')}:{l['event']}"
        out[eid] = (l, bo)
    return out, problems


def is_semantic(l):
    """Wording-level rows that need not change what the Law requires (user definition, 2026-10-27): SEMANTIC_WORDING, plain wording/terminology rewrites, gender-neutral drafting."""
    return (l["category"] == "SEMANTIC_WORDING" or l["subtype"] in ("wording_only", "terminology")
            or (l["category"] == "EXTERNAL_FORCE" and l["subtype"] == "legal_social" and "gender-neutral" in l["rationale"]))


def is_scope(l):
    """Qualifier/scope rewordings that may widen or narrow what a rule applies to: kept SEMANTIC_WORDING but counted as substantive (user decision)."""
    return l["category"] == "SEMANTIC_WORDING" and l["subtype"] == "qualifier_scope"


EDITION_RE = re.compile(r"printer.s variant|different printing|wrong printing|misdated|edition artefact|source-edition|Baxter|Wright & Co|pocket reprint|Toronto|unofficial booklet", re.I)


def edition_issue(l):
    return l["subtype"] == "edition_artefact" or l["category"] in ("NOT_A_CHANGE", "SEMANTIC_WORDING") and bool(EDITION_RE.search(l["rationale"] + " " + l["what_changed"] + " " + l["notes"] + " " + l["date_evidence"]))


def real(l):
    """A label that asserts a real rule change outranks one that says wording-only / not a change when two share an event."""
    return not (l["category"] == "NOT_A_CHANGE" or l["subtype"] == "wording_only")


def merge_labels(a, b, ka, kb):
    """Combine two hand labels that now describe one event. a is the primary (more informative category)."""
    m = dict(a)
    m["_ref"] = a.get("_ref", ka) + "+" + b.get("_ref", kb)
    m["what_changed"] = a["what_changed"] + " ALSO (merged event, " + kb + "): " + b["what_changed"]
    m["rationale"] = a["rationale"] + (" ALSO (" + kb + "): " + b["rationale"] if b["rationale"] and real(b) else "")
    m["evidence"] = list(dict.fromkeys(list(a["evidence"]) + list(b["evidence"])))
    if not a["secondary_category"] and b["category"] != a["category"]:
        m["secondary_category"], m["secondary_subtype"] = b["category"], b["subtype"]
    m["notes"] = (a["notes"] + " " if a["notes"] else "") + f"Merged labels {ka} + {kb} (the pipeline now groups their records into one event)."
    m["date_evidence"] = a["date_evidence"] or b["date_evidence"]
    if (a["category"], a["subtype"]) != (b["category"], b["subtype"]):
        m["notes"] += f" Second label: {b['category']}/{b['subtype']} ({b.get('basis')}, {b.get('confidence')})."
    if b.get("integrity") == "suspect":
        m["integrity"] = "suspect"
    return m


def check(l, e):
    if l["category"] == "NOT_A_CHANGE" and l["subtype"] == "":
        l["subtype"] = "edition_artefact"   # blank NOT_A_CHANGE subtype was used by labellers for unreliable-edition artefacts
    c, s = l["category"], l["subtype"]
    assert c in CATS, f"{l['pair']} {l['event']}: bad category {c}"
    assert s == "" or s in CATS[c]["subtypes"], f"{l['pair']} {l['event']}: subtype {s} not in {c}"
    if l["secondary_category"]:
        assert l["secondary_category"] in CATS, l
        assert l["secondary_subtype"] in ("",) + tuple(CATS[l["secondary_category"]]["subtypes"]), f"{l['pair']} {l['event']}: secondary subtype {l['secondary_subtype']}"
    assert l["basis"] in BASIS, f"{l['pair']} {l['event']}: basis {l['basis']}"
    for sid in l["evidence"]:
        assert sid in SOURCES, f"{l['pair']} {l['event']}: unknown source {sid}"
    if c == "UNCATEGORISED":
        assert l["basis"] == "none", f"{l['pair']} {l['event']}: UNCATEGORISED needs basis none"
    elif c == "NOT_A_CHANGE":
        assert l["basis"] == "derived", f"{l['pair']} {l['event']}: NOT_A_CHANGE needs basis derived"
    else:
        assert l["rationale"] and l["evidence"], f"{l['pair']} {l['event']}: label needs rationale and evidence"


def mechanical(e, pair):
    cls = e["text_diff_class"]
    if cls in ("format_only", "numbering_only"):
        return dict(pair=pair, event=e["event_id"][-4:], what_changed="No change of wording: text differs only in punctuation, quote marks, hyphenation, list numbers or sentence splitting.",
                    category="NOT_A_CHANGE", subtype="format_artefact", confidence="high", basis="derived",
                    rationale="Token-level comparison of old and new wording (lower-cased words and numbers only) finds them identical" + (" apart from stray list numbers." if cls == "numbering_only" else "."),
                    evidence=["S18"], secondary_category="", secondary_subtype="", date_evidence="", integrity="ok", notes="mechanical label (08b)")
    if cls == "ocr_noise":
        return dict(pair=pair, event=e["event_id"][-4:], what_changed="No change of wording: the two texts differ only in OCR garbage (e.g. 'docs' for 'does', 'froi' for 'from').",
                    category="NOT_A_CHANGE", subtype="ocr_noise", confidence="high", basis="derived",
                    rationale="Token-level comparison finds identical wording once rare mis-recognised tokens, each paired with a near-identical frequent word, are ignored.",
                    evidence=["S18"], secondary_category="", secondary_subtype="", date_evidence="", integrity="ok", notes="mechanical label (08b)")
    if cls == "minor_wording":
        return dict(pair=pair, event=e["event_id"][-4:], what_changed=f"Minor wording change only (changed words: {', '.join(e['changed_tokens'])}).",
                    category="STRUCTURAL", subtype="wording_only", confidence="medium", basis="derived",
                    rationale="Token-level comparison finds at most three changed words, none of them a modal, negation or number word; the rule is unchanged in effect.",
                    evidence=["S18"], secondary_category="", secondary_subtype="", date_evidence="", integrity="ok", notes="mechanical label (08b); not hand-checked")
    return None


def main():
    handlabels = {}
    for f in sorted((ROOT / "rule_changes/labels").glob("[pnq]*.py")):
        spec = importlib.util.spec_from_file_location(f.stem, f)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        handlabels.setdefault(m.PAIR, [])
        for l in m.LABELS:
            assert not any(x["event"] == l["event"] for x in handlabels[m.PAIR] if x.get("_file") == f.stem), f"duplicate label {m.PAIR}:{l['event']}"
            l["_file"] = f.stem
            handlabels[m.PAIR].append(l)
    keys = json.load(open(KEYFILE)) if KEYFILE.exists() else {}
    OV = load_overrides()
    rows, missing, problems = [], [], []
    for p in sorted((ROOT / "rule_changes/data/events").glob("*.jsonl"), key=lambda p: int(p.stem.split("_")[0])):
        if int(p.stem.split("_")[0]) < FIRST_YEAR:
            continue
        pair = p.stem
        evs = load_events(pair)
        # a label module may hold both legacy (p*) and new (n*) labels; later files override earlier ones for the same event
        resolved, probs = resolve(handlabels.get(pair, []), evs, keys, pair)
        problems += probs
        for e in evs:
            l, ov = resolved.get(e["event_id"], (None, None))
            if l is None:
                l = mechanical(e, pair)
                if l is None:
                    missing.append((pair, e["event_id"][-4:], e["event_type"], e["law_title"][:25], e["text_diff_class"], e["triage"]))
                    continue
            l = apply_override(l, e, OV, problems)
            check(l, e)
            rows.append(dict(event_id=e["event_id"], sig=sig(e), pair=pair, section=e["section"], canonical_law=e["canonical_law"],
                             law_title=e["law_title"], law_from=e["law_from"], law_to=e["law_to"], event_type=e["event_type"],
                             n_records=e["n_records"], numeric_audit=e["numeric_audit"]["verdict"],
                             what_changed=l["what_changed"], category=l["category"], subtype=l["subtype"],
                             secondary_category=l["secondary_category"], secondary_subtype=l["secondary_subtype"],
                             confidence=l["confidence"], basis=l["basis"], rationale=l["rationale"],
                             evidence=";".join(l["evidence"]), date_evidence=l["date_evidence"], integrity=l["integrity"],
                             notes=l["notes"], label_ref=l.get("_ref", "mechanical"), semantic_only=int(is_semantic(l)), scope_change=int(is_scope(l)), source_edition_issue=int(edition_issue(l)), substantive_change=int((not is_semantic(l) or is_scope(l)) and l["category"] != "NOT_A_CHANGE"), review_status=VERD.get(e["event_id"],{}).get("status","unreviewed"), reviewer_notes=VERD.get(e["event_id"],{}).get("note",""), taxonomy_version=TAX["version"]))
    json.dump(keys, open(KEYFILE, "w"), indent=0, sort_keys=True)
    if rows:
        with open(OUT, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0]))
            w.writeheader()
            w.writerows(rows)
        with open(OUT_POST, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0]))
            w.writeheader()
            w.writerows(r for r in rows if int(r["pair"].split("_")[0]) >= 1947)
    c = Counter(r["category"] for r in rows)
    print(f"{len(rows)} labelled, {len(missing)} events without a label; {dict(c)}")
    print("without a label by pair:", dict(Counter(m[0] for m in missing)))
    if problems:
        print("LABEL RESOLUTION NOTES (merged = two hand labels now share one event, both kept; not found = the label's event no longer exists after pipeline fixes):")
        for x in problems:
            print("  ", x)
    with open(ROOT / "rule_changes/data/categories/unlabelled_events.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["pair", "event", "event_type", "law_title", "text_diff_class", "triage"])
        w.writerows(missing)


if __name__ == "__main__":
    main()
