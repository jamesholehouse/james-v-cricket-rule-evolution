"""Labels added in round 4 (authored against that run)."""
from _h import make
ST, UN, NC, SW = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE", "SEMANTIC_WORDING"
PAIR = "1962_1968"
L, LABELS = make(PAIR)
L("E009", "Law 28 (Wide ball): OCR slips ('so so wide', 'place\'' for 'places'); 'fieldsmen' becomes 'fieldsman' in the interference Note.", NC, "ocr_noise", "medium", "derived", "Differences are repeated words, plural slips and OCR marks; the interference rule is identical.", ["S18"])
L("E010", "Law 29: OCR 'M' for the opening quote mark before 'Wide Ball'; same rule.", NC, "ocr_noise", "high", "derived", "A mis-recognised quotation mark.", ["S18"])
L("E018", "Law 47 (scoring Notes): quote-mark spacing and a truncated line ('No Balls and \"'); same text.", NC, "format_artefact", "high", "derived", "Only quotation marks and spacing differ.", ["S18"])
