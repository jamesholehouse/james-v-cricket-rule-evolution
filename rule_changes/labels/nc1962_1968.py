"""Labels for events surfaced by the cross-reference-change class."""
from _h import make
ST, UN, NC = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE"
D19 = "MCC 2017 Code 2nd edition, in force 1 April 2019 (S04)."
PAIR = "1962_1968"
L, LABELS = make(PAIR)
L("E005", "Law 17 (luncheon interval): the cross-reference '(but see Law 10, Note 3)' becomes '(but see Law 10, Note 2)'.", ST, "consequential", "medium", "derived", "The Notes to Law 10 were rewritten in this pair, so the Note number follows them.", ["S18", "S08"])
