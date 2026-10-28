"""Labels for events surfaced by the second-pass classifier fixes (authored against the pipeline output of that run)."""
from _h import make
PAIR = "1962_1968"
L, LABELS = make(PAIR)
ST, UN, NC = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE"
L("E009", "Law 36: OCR error 'but' for 'out' in the 1968 text; same rule.", NC, "ocr_noise", "high", "derived", "The only differences are mis-recognised words (OCR errors); the rule is identical.", ["S18"])
L("E014", "Law 46: 'unaccom. panied' for 'unaccompanied' (hyphenation break); same rule.", NC, "ocr_noise", "high", "derived", "The only differences are mis-recognised words (OCR errors); the rule is identical.", ["S18"])
