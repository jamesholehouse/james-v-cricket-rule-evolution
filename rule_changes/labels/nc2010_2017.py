"""Labels for events surfaced by the cross-reference-change class."""
from _h import make
ST, UN, NC = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE"
D19 = "MCC 2017 Code 2nd edition, in force 1 April 2019 (S04)."
PAIR = "2010_2017"
L, LABELS = make(PAIR)
L("E067", "Law 3: the pointer 'See Laws 4.2 (Correctness of scores), 21.8 (Correctness of result) and 21.10 (Result not to be changed)' is removed.", ST, "reorganisation", "medium", "inferred", "A cross-reference pointer is dropped in the 2017 re-ordering of the Laws (S02 preface); no rule text is removed.", ["S02"])
L("E104", "Law 7/6 (non-turf pitches): the length and width minima (58 ft/17.68 m; 6 ft/1.83 m) are re-segmented into the preceding unit and the pointer changes from 'See Law 10.8' to 'See Law 9.8'.", ST, "consequential", "medium", "inferred", "The measurements are identical in both texts; the pointer follows the 2017 renumbering (MCC preface, S02).", ["S02"])
