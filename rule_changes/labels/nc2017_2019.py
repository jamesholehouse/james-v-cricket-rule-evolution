"""Labels for events surfaced by the cross-reference-change class."""
from _h import make
ST, UN, NC = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE"
D19 = "MCC 2017 Code 2nd edition, in force 1 April 2019 (S04)."
PAIR = "2017_2019"
L, LABELS = make(PAIR)
L("E017", "Law 13.1: the heading 'Number of innings' and the numbers 13.1.1/13.1.2 are re-segmented; the clause text is unchanged.", NC, "segmentation_artefact", "high", "derived", "Only unit boundaries differ.", ["S18"])
L("E026", "Law 18.12: the heading 'Batsman returning to wicket he/she has left' and the number 18.12.1 are re-segmented; the clause text is unchanged.", NC, "segmentation_artefact", "high", "derived", "Only unit boundaries differ.", ["S18"])
L("E050", "Law 33.4 (Caught, No runs to be scored): the cross-reference 'Law 18.11.1 (Batsman returning to original end)' becomes 'Law 18.12.1 (Batsman returning to wicket he/she has left)'.", ST, "clarification_umpire_workability", "high", "stated",
  "MCC (S04): 'There was an incorrect cross-reference in Law 33.4, which referred back to Law 18.11 rather than 18.12.' This has been fixed.", ["S04"], date=D19)
