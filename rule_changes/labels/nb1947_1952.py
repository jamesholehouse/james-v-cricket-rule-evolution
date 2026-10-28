"""Labels for events surfaced by the second-pass classifier fixes (authored against the pipeline output of that run)."""
from _h import make
PAIR = "1947_1952"
L, LABELS = make(PAIR)
ST, UN, NC = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE"
L("E020", "Law 39: OCR error 'ease' for 'case' in the 1947 text, and 'pilch' for 'pitch' in the 1952 text; same rule.", NC, "ocr_noise", "high", "derived", "The only differences are mis-recognised words (OCR errors); the rule is identical.", ["S18"])
L("E032", "Law 47 (drying regulations): 'the wicket' becomes 'the pitch' (terminology brought into line with the 1947 Code's definition of 'Pitch').", ST, "wording_only", "medium", "derived", "One word replaced by its defined synonym; the regulation is unchanged.", ["S18"])
