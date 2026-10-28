"""
Local review server for the rule-change labels. Standard library only.

    .venv/bin/python rule_changes/review_app/server.py [--port 8765]

Reads data/categories/event_labels_all.csv, data/events, data/changes, data/evidence/sources.csv.
Writes ONLY data/review/verdicts.jsonl (append-only; last record per event wins).
Run scripts/08_build_labels.py afterwards to fold verdicts into review_status / reviewer_notes.
"""
import argparse
import csv
import json
import re
import sys
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

csv.field_size_limit(sys.maxsize)
HERE = Path(__file__).resolve().parent
D = HERE.parents[0] / "data"
VERDICTS = D / "review/verdicts.jsonl"
STATUSES = ("confirmed", "edited", "rejected", "needs_research")


def load():
    labels = list(csv.DictReader(open(D / "categories/event_labels_all.csv", encoding="utf-8")))
    sources = {r["id"]: r for r in csv.DictReader(open(D / "evidence/sources.csv", encoding="utf-8"))}
    gold = {r["serial"]: r for r in csv.DictReader(open(D / "gold/raitkerr_chronology.csv", encoding="utf-8"))} \
        if (D / "gold/raitkerr_chronology.csv").exists() else {}
    # Law-level RENUMBERING rows are not pipeline events; they come from the final dataset (09_build_datasets.py).
    ren = [r for r in csv.DictReader(open(D / "final/substantive_changes.csv", encoding="utf-8")) if r["category"] == "RENUMBERING"]
    labels += ren
    labels.sort(key=lambda r: (int(r["pair"].split("_")[0]), r["event_id"]))
    return labels, sources, gold


def verdicts():
    v = {}
    if VERDICTS.exists():
        for l in open(VERDICTS, encoding="utf-8"):
            if l.strip():
                r = json.loads(l)
                v[r["event_id"]] = r
    return v


LABELS, SOURCES, GOLD = load()
BY_ID = {r["event_id"]: r for r in LABELS}
_cache = {}


def pair_data(pair):
    if pair not in _cache:
        ev = {}
        for l in open(D / "events" / f"{pair}.jsonl", encoding="utf-8"):
            e = json.loads(l)
            ev[e["event_id"]] = e
        ch = {}
        for l in open(D / "changes" / f"{pair}.jsonl", encoding="utf-8"):
            c = json.loads(l)
            ch[c["change_id"]] = c
        _cache[pair] = (ev, ch)
    return _cache[pair]


def summary(r, v):
    vd = v.get(r["event_id"])
    return dict(event_id=r["event_id"], pair=r["pair"], law=r["law_title"] or r["canonical_law"], law_from=r["law_from"], law_to=r["law_to"],
                category=r["category"], subtype=r["subtype"], confidence=r["confidence"], basis=r["basis"], n=r["n_records"],
                what=r["what_changed"][:140], semantic=r["semantic_only"], scope=r["scope_change"], edition_issue=r["source_edition_issue"],
                substantive=r["substantive_change"], integrity=r["integrity"], status=vd["status"] if vd else "unreviewed")


def renumber_change_ids():
    out = {}
    for r in csv.DictReader(open(D / "final/changes_all_records_labelled.csv", encoding="utf-8")):
        if r["label_level"] == "law_renumbering":
            out[r["event_id"]] = r["change_id"]
    return out


REN_CHANGE = renumber_change_ids()


def detail(eid):
    r = BY_ID[eid]
    ev, ch = pair_data(r["pair"])
    if eid in REN_CHANGE:
        recs = [ch[REN_CHANGE[eid]]]
    else:
        e = ev[eid]
        recs = [ch[c] for c in e["change_ids"] if c in ch]
    recs.sort(key=lambda c: (c.get("unit_to") or 0, c["change_id"]))
    srcs = [dict(SOURCES[s], id=s) if s in SOURCES else dict(id=s, title="(unregistered)") for s in r["evidence"].split(";") if s]
    text = r["rationale"] + " " + r["what_changed"] + " " + r["notes"]
    serials = sorted({m for m in re.findall(r"serials?\s+((?:\d+[a-z]?(?:\s*(?:,|and|&|-)\s*)?)+)", text, re.I) for m in re.findall(r"\d+[a-z]?", m)}, key=lambda x: int(re.match(r"\d+", x).group()))
    gold = [GOLD[s] for s in serials if s in GOLD][:8]
    return dict(label=r, records=[{k: c.get(k) for k in ("change_id", "op", "granularity", "section", "law_from", "law_to", "old_text", "new_text", "similarity")} for c in recs],
                sources=srcs, gold=gold, verdict=verdicts().get(eid))


class H(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def send(self, code, body, ctype="application/json"):
        b = body if isinstance(body, bytes) else json.dumps(body).encode()
        self.send_response(code)
        self.send_header("Content-Type", ctype + "; charset=utf-8")
        self.send_header("Content-Length", str(len(b)))
        self.end_headers()
        self.wfile.write(b)

    def do_GET(self):
        u = urlparse(self.path)
        q = {k: v[0] for k, v in parse_qs(u.query).items()}
        if u.path == "/":
            return self.send(200, (HERE / "index.html").read_bytes(), "text/html")
        if u.path == "/api/events":
            v = verdicts()
            rows = [summary(r, v) for r in LABELS]
            need = q.get("q", "").lower()
            out = []
            for s, r in zip(rows, LABELS):
                if q.get("pair") and s["pair"] != q["pair"]: continue
                if q.get("category") and s["category"] != q["category"]: continue
                if q.get("status") and s["status"] != q["status"]: continue
                if q.get("basis") and s["basis"] != q["basis"]: continue
                if q.get("confidence") and s["confidence"] != q["confidence"]: continue
                if q.get("substantive") == "1" and s["substantive"] != "1": continue
                if q.get("suspect") == "1" and s["integrity"] != "suspect": continue
                if need and need not in (r["what_changed"] + r["rationale"] + r["law_title"] + r["event_id"]).lower(): continue
                out.append(s)
            stats = {"total": len(rows), "by_status": {}}
            for s in rows:
                stats["by_status"][s["status"]] = stats["by_status"].get(s["status"], 0) + 1
            return self.send(200, dict(events=out, stats=stats))
        if u.path == "/api/meta":
            return self.send(200, dict(pairs=sorted({r["pair"] for r in LABELS}, key=lambda p: int(p.split("_")[0])),
                                       categories=sorted({r["category"] for r in LABELS}), statuses=("unreviewed",) + STATUSES))
        if u.path == "/api/event":
            if q.get("id") not in BY_ID:
                return self.send(404, {"error": "no such event"})
            return self.send(200, detail(q["id"]))
        self.send(404, {"error": "not found"})

    def do_POST(self):
        if urlparse(self.path).path != "/api/verdict":
            return self.send(404, {"error": "not found"})
        d = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))))
        if d.get("event_id") not in BY_ID or d.get("status") not in STATUSES + ("unreviewed",):
            return self.send(400, {"error": "bad event_id or status"})
        rec = dict(event_id=d["event_id"], status=d["status"], note=d.get("note", ""), proposed_category=d.get("proposed_category", ""),
                   proposed_subtype=d.get("proposed_subtype", ""), sig=BY_ID[d["event_id"]]["sig"], time=time.strftime("%Y-%m-%dT%H:%M:%S"))
        VERDICTS.parent.mkdir(parents=True, exist_ok=True)
        with open(VERDICTS, "a", encoding="utf-8") as f:
            f.write(json.dumps(rec) + "\n")
        self.send(200, rec)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8765)
    a = ap.parse_args()
    print(f"Review UI: http://127.0.0.1:{a.port}  ({len(LABELS)} events; verdicts -> {VERDICTS})")
    ThreadingHTTPServer(("127.0.0.1", a.port), H).serve_forever()
