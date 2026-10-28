"""Labels for events surfaced by the second-pass classifier fixes (authored against the pipeline output of that run)."""
from _h import make
PAIR = "2008_2010"
L, LABELS = make(PAIR)
ST, UN, NC = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE"
L("E103", "Law 6 (The bat): 'Grades B and C' becomes 'Types B and C' and a comma is added.", ST, "terminology", "medium", "inferred", "Grades are renamed Types in the 4th edition (see the first-pass label for the Appendix E rename).", ["S01"], date="2000 Code 4th edition, effective 1 October 2010 (S01).")
