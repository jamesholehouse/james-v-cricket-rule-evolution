"""
08a_acs_presence.py
For events in the 1947-1992 pairs, test whether the event's OLD and NEW wording is found in independent ACS
transcriptions (1947 Code 1st / 2nd / 4th editions; 1980 Code). Adds `acs_presence` to the event files:
best fuzzy-containment score (0-100) of the first 300 characters of old/new digest against each transcription.

Usage (from the repo root):
    .venv/bin/python rule_changes/scripts/08a_acs_presence.py
"""
import json
import re
from pathlib import Path

from rapidfuzz import fuzz

ROOT = Path(__file__).resolve().parents[2]
EV = ROOT / "rule_changes/data/events"
TXT = ROOT / "rule_changes/data/evidence/text"
CORP = {"acs1947": "acs_1947.txt", "acs1947_2nd": "acs_1947_second_edition.txt", "acs1947_4th": "acs_1947_fourth_edition.txt",
        "acs1980": "acs_1980.txt"}
PAIRS = ["1947_1952", "1952_1962", "1962_1968", "1968_1980", "1980_1992"]


def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = re.sub(r"[—–]", "-", s)
    s = re.sub(r"[^a-z0-9%/ ]", " ", s.lower())
    return re.sub(r"\s+", " ", s).strip()


def main():
    corp = {k: norm((TXT / f).read_text()) for k, f in CORP.items()}
    for pair in PAIRS:
        p = EV / f"{pair}.jsonl"
        events = [json.loads(l) for l in open(p, encoding="utf-8")]
        for e in events:
            pres = {}
            for side in ("old", "new"):
                t = norm(e[f"{side}_digest"])[:300]
                if len(t) < 25:
                    pres[side] = None
                    continue
                pres[side] = {k: int(fuzz.partial_ratio(t, c)) for k, c in corp.items()}
            e["acs_presence"] = pres
        with open(p, "w", encoding="utf-8") as f:
            for e in events:
                f.write(json.dumps(e, ensure_ascii=False) + "\n")
        print(pair, len(events), "events annotated")


if __name__ == "__main__":
    main()
