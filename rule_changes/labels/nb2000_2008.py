"""Labels for events surfaced by the second-pass classifier fixes (authored against the pipeline output of that run)."""
from _h import make
PAIR = "2000_2008"
L, LABELS = make(PAIR)
ST, UN, NC = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE"
L("E011", "Law 18: cross-reference '42.5(b)(iii)' becomes '42.5(b)(iv)' and the clause 'except as in (b) below' is re-segmented.", ST, "wording_only", "medium", "derived", "Cross-reference renumbering and re-segmentation; the rule is unchanged.", ["S18"])
L("E021", "Law 24: OCR split 'enter ing' for 'entering' in the 2008 text; same rule.", NC, "ocr_noise", "high", "derived", "The only differences are mis-recognised words (OCR errors); the rule is identical.", ["S18"])
