#!/bin/bash
# Rebuild everything downstream of the processed texts. Run from anywhere. Labels (08_*) are keyed by content
# signature, so re-running the pipeline does not orphan them.
set -e
cd "$(dirname "$0")/../.."
PY=.venv/bin/python
$PY rule_changes/scripts/01_segment_laws.py 1828 1835 1857 1884 1890 1892 1896 1900 1902 1906 1908 1910 1911 1913 1914 1918 1920 1923 1932 1939 > /dev/null
$PY rule_changes/scripts/01b_segment_eras.py > /dev/null
$PY rule_changes/scripts/02_diff_editions.py > /dev/null
$PY rule_changes/scripts/04_build_law_table.py
$PY rule_changes/scripts/06_group_events.py | tail -1
$PY rule_changes/scripts/07_audit_numeric_cues.py | head -1
$PY rule_changes/scripts/08a_acs_presence.py > /dev/null
$PY rule_changes/scripts/08b_classify_text_diff.py > /dev/null
$PY rule_changes/scripts/08c_text_found_elsewhere.py > /dev/null
$PY rule_changes/scripts/03_validate_gold.py | tail -1
