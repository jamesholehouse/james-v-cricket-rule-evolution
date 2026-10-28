"""Labels for events surfaced by the cross-reference-change class."""
from _h import make
ST, UN, NC = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE"
D19 = "MCC 2017 Code 2nd edition, in force 1 April 2019 (S04)."
PAIR = "1980_1992"
L, LABELS = make(PAIR)
L("E004", "Law 18: the cross-reference 'See Law 2.7.' becomes 'See Law 2.'", ST, "wording_only", "medium", "derived", "A cross-reference is generalised from a sub-clause to the whole Law; no rule text changes.", ["S18"])
