#!/bin/bash
# Rebuild data/gold/raitkerr_chronology.csv from the hand-transcribed part files (order matters: part1 truncates, 2-3 append).
cd "$(dirname "$0")" && ../../.venv/bin/python _gold_part1.py && ../../.venv/bin/python _gold_part2.py && ../../.venv/bin/python _gold_part3.py && ../../.venv/bin/python _gold_finalise.py
