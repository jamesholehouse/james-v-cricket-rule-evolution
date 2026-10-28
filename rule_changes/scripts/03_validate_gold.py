"""
03_validate_gold.py
Pilot recall check: does the deterministic diff (02) contain a change record corresponding to each
Rait Kerr entry that falls inside a pilot edition pair?

The mapping Rait Kerr serial -> (edition pair, expected op(s), regex on new/old text) was written by hand
by reading each gold entry; it is deliberately conservative (a hit means a record shows the described change).

Usage (from the repo root):
    .venv/bin/python rule_changes/scripts/03_validate_gold.py
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHANGES = ROOT / "rule_changes/data/changes"

# (serial, date, pair, which text to search, regex, note)
GOLD = [
    (108, "1889", "1884_1890", "new", r"overs of five balls|five balls have been bowled", "over 4 -> 5 balls"),
    (109, "1889", "1884_1890", "new", r"as often as he pleases", "bowler may change ends freely"),
    (110, "1889", "1884_1890", "new", r"declare", "declaration allowed on last day"),
    (111, "1894", "1892_1896", "new", r"120 runs", "follow-on limit raised to 120 (3-day)"),
    (112, "1899", "1900_1902", "new", r"lodge", "ball dead if it lodges in clothing  [edition lag: absent from 1900 text, present 1902]"),
    (113, "1899", "1896_1900", "new", r"either umpire|any umpire", "either umpire may call no ball"),
    (114, "1900", "1896_1900", "new", r"follow their innings.*150|150 runs", "follow-on optional / limits 150-100-75"),
    (115, "1900", "1900_1902", "new", r"luncheon", "declaration after lunch on day 2 of 3-day match  [edition lag]"),
    (116, "1900", "1896_1900", "new", r"six balls", "over 5 -> 6 balls"),
    (127, "1936", "1932_1939", "new", r"five runs|5 runs", "5-run penalty in addition to runs made"),
    (128, "1937", "1932_1939", "new", r"off[- ]?side|pitch(ed|ing)? (on|outside)", "LBW extended to off-side pitching"),
]


def main():
    cache, hits = {}, 0
    for serial, date, pair, side, rx, note in GOLD:
        if pair not in cache:
            cache[pair] = [json.loads(l) for l in open(CHANGES / f"{pair}.jsonl", encoding="utf-8")]
        found = [c for c in cache[pair]
                 if c.get("substantive") and re.search(rx, (c.get("new_text") or "") + " " + (c.get("old_text") or ""), re.I)]
        ok = bool(found)
        hits += ok
        ids = ", ".join(f"{c['change_id'][-4:]}:{c['op']}:L{c.get('law_to') or c.get('law_from')}" for c in found[:4])
        print(f"{'HIT ' if ok else 'MISS'} #{serial:<4} {date} {pair}  {note:<48} {ids}")
    print(f"\nrecall {hits}/{len(GOLD)}")


if __name__ == "__main__":
    main()
