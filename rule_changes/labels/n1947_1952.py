"""Labels for events added after the first labelling pass (authored against the pipeline output of the verification-fix run)."""
from _h import make
PAIR = "1947_1952"
L, LABELS = make(PAIR)
ST, UN, NC = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE"
L("E016", "Law 41 (Run out): OCR errors in the old text ('an time', 'hi wicket', 'bats - man') and a stray list number; same rule.", NC, "ocr_noise", "high", "derived", "The differences are mis-recognised words and a stray '1.' marker.", ["S18"])
L("E023", "Law 47 (Appeals), scoring notes: 'IT runs' / 'If runs' and a stray list number '2.'; same rule.", NC, "ocr_noise", "high", "derived", "The differences are an OCR misreading and a stray list number.", ["S18"])
L("E010", "Law 27: OCR errors in the 1952 text ('docs', 'arc'); same rule.", NC, "ocr_noise", "high", "derived", "The only differences are mis-recognised words (OCR errors); the rule is identical.", ["S18"])
L("E011", "Law 28 (Wide ball): OCR errors in the 1952 text ('dclivcrc', 'callee', 'th.') and a stray list marker; same rule.", NC, "ocr_noise", "high", "derived", "The only differences are mis-recognised words (OCR errors); the rule is identical.", ["S18"])
L("E012", "Law 29: OCR error 'cither' for 'either' in the 1952 text; same rule.", NC, "ocr_noise", "high", "derived", "The only differences are mis-recognised words (OCR errors); the rule is identical.", ["S18"])
L("E018", "Law 35 (Caught): OCR errors in the 1952 text ('n<', 'ease', 'lodgin'); same rule.", NC, "ocr_noise", "high", "derived", "The only differences are mis-recognised words (OCR errors); the rule is identical.", ["S18"])
L("E020", "Law 39: OCR errors in the 1952 text ('al!', 'arc'); same rule.", NC, "ocr_noise", "high", "derived", "The only differences are mis-recognised words (OCR errors); the rule is identical.", ["S18"])
