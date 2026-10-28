"""Labels for events surfaced by the cross-reference-change class."""
from _h import make
ST, UN, NC = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE"
D19 = "MCC 2017 Code 2nd edition, in force 1 April 2019 (S04)."
PAIR = "1947_1952"
L, LABELS = make(PAIR)
L("E028", "Law 47 (Appeals), over-ending Note: the cross-reference 'Under Law 27 the ball is Dead on Over being called' (1947 dataset text) becomes 'Under Law 25' (1952).", NC, "cleaning_artefact_numeric", "medium", "derived", "Law 25 is Dead ball in both the 1947 and 1952 texts, and the ACS transcription of the 1947 Code already reads 'Under Law 25' (acs_1947.txt l.866); the raw 1947 OCR reads 'Law 27', so the dataset's 1947 number is a misprint or OCR error, not a renumbering.", ["S09", "S17"], integrity="suspect")
L("E035", "Law 47: the pointer 'Law 46, Note (5)' is segmented as a separate unit in 1947; the 1952 text still has 'Law 46, Note 5 (i) is applicable in such cases'.", NC, "segmentation_artefact", "medium", "derived", "The reference is still present in 1952; only its notation and unit boundary differ.", ["S18"])
