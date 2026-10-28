"""
04_build_law_table.py
Build the Law identity table: which numbered Law in each edition is "the same Law" as which in the others.

Method: chain the Law-to-Law alignments of consecutive editions (02_diff_editions.py output) with a
union-find, so a Law keeps one canonical id across renumbering. Matches are content-based, so a Law whose
number changed (Caught = 22/35/32/33 ...) stays one row; Laws that are created, dropped, merged or split show
up as rows that start/stop or as conflicts.

Outputs (rule_changes/data/law_identity/):
  law_nodes.csv       one row per (edition, section, Law): canonical_id, number, title, #units, #chars
  law_pivot.csv       rows = canonical Laws (main code), columns = editions, cell = Law number as printed
  law_pivot.md        same, markdown, with a label per row
  law_lineage.csv     per canonical Law: first/last edition, number history, all titles seen, renumber events

Usage (from the repo root):
    .venv/bin/python rule_changes/scripts/04_build_law_table.py
"""
import csv
import json
import re
from collections import Counter, OrderedDict, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NODES = ROOT / "rule_changes/data/nodes"
ALIGN = ROOT / "rule_changes/data/alignments"
OUT = ROOT / "rule_changes/data/law_identity"


def load_laws():
    laws = OrderedDict()
    for p in sorted(NODES.glob("*.jsonl"), key=lambda p: int(p.stem)):
        y = int(p.stem)
        for line in open(p, encoding="utf-8"):
            n = json.loads(line)
            k = (y, n["section"], n["law_no"])
            d = laws.setdefault(k, dict(edition=y, section=n["section"], law_no=n["law_no"], title=n["law_title"],
                                        units=0, chars=0))
            d["units"] += 1
            d["chars"] += len(n["text"])
            if not d["title"] and n["law_title"]:
                d["title"] = n["law_title"]
    return laws


class UF:
    def __init__(self):
        self.p = {}

    def find(self, x):
        self.p.setdefault(x, x)
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        self.p[self.find(a)] = self.find(b)


def clean_title(t):
    return re.sub(r"\s+", " ", t.replace("“", "").replace("”", "")).strip(" .;:,").title() if t else ""


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    laws = load_laws()
    years = sorted({k[0] for k in laws})
    uf = UF()
    for k in laws:
        uf.find(k)
    for p in ALIGN.glob("*.json"):
        a, b = (int(x) for x in p.stem.split("_"))
        for m in json.load(open(p))["law_alignment"]:
            if m.get("collapsed"):
                continue
            ka, kb = (a, m["section"], m["from_no"]), (b, m["section"], m["to_no"])
            if ka in laws and kb in laws:
                uf.union(ka, kb)

    comps = defaultdict(list)
    for k in laws:
        comps[uf.find(k)].append(k)
    ordered = sorted(comps.values(), key=lambda ks: (min(k[0] for k in ks), ks[0][1] != "main",
                                                      min(int(re.sub(r"\D", "", k[2]) or 0) for k in ks)))
    cid = {}
    rows, lineage = [], []
    for i, ks in enumerate(ordered, 1):
        ks = sorted(ks)
        sec = ks[0][1]
        canon = f"{'L' if sec == 'main' else sec[:3].upper()}{i:03d}"
        titles = Counter(clean_title(laws[k]["title"]) for k in ks if laws[k]["title"])
        label = titles.most_common(1)[0][0] if titles else ""
        per_ed = Counter(k[0] for k in ks)
        conflict = any(v > 1 for v in per_ed.values())
        for k in ks:
            cid[k] = canon
            rows.append(dict(canonical_id=canon, edition=k[0], section=k[1], law_no=k[2], title=laws[k]["title"],
                             units=laws[k]["units"], chars=laws[k]["chars"]))
        nums = [(k[0], k[2]) for k in ks]
        hist, prev = [], None
        for y, n in nums:
            if n != prev:
                hist.append(f"{y}:{n}")
                prev = n
        lineage.append(dict(canonical_id=canon, section=sec, label=label, first_edition=ks[0][0],
                            last_edition=ks[-1][0], n_editions=len(per_ed), number_history=" ".join(hist),
                            n_renumberings=len(hist) - 1, titles_seen=" | ".join(sorted(titles)),
                            conflict=int(conflict)))

    with open(OUT / "law_nodes.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(sorted(rows, key=lambda r: (r["canonical_id"], r["edition"])))
    with open(OUT / "law_lineage.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(lineage[0]))
        w.writeheader()
        w.writerows(lineage)

    main_lines = [l for l in lineage if l["section"] == "main"]
    by = defaultdict(dict)
    for r in rows:
        if r["section"] == "main":
            by[r["canonical_id"]].setdefault(r["edition"], r["law_no"])
    with open(OUT / "law_pivot.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["canonical_id", "label"] + years)
        for l in main_lines:
            w.writerow([l["canonical_id"], l["label"]] + [by[l["canonical_id"]].get(y, "") for y in years])
    with open(OUT / "law_pivot.md", "w") as f:
        f.write("| id | label | " + " | ".join(map(str, years)) + " |\n")
        f.write("|" + "---|" * (len(years) + 2) + "\n")
        for l in main_lines:
            f.write(f"| {l['canonical_id']} | {l['label']} | "
                    + " | ".join(by[l["canonical_id"]].get(y, "") for y in years) + " |\n")
    print(f"{len(main_lines)} canonical main Laws over {len(years)} editions; "
          f"{sum(l['conflict'] for l in lineage)} conflicts; "
          f"{sum(l['n_renumberings'] > 0 for l in main_lines)} Laws renumbered at least once; "
          f"{sum(1 for l in main_lines if l['n_editions'] == len(years))} Laws present in all editions")


if __name__ == "__main__":
    main()
