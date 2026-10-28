"""Labels for events surfaced by the second-pass classifier fixes (authored against the pipeline output of that run)."""
from _h import make
PAIR = "2017_2019"
L, LABELS = make(PAIR)
ST, UN, NC = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE"
L("E013", "Preamble: 'extends to all players, umpires and ... parents' becomes 'extends to all players, match officials and ... parents'.", ST, "terminology", "high", "stated", "MCC (S04) lists the replacement of 'umpires' by 'match officials' in the Preamble among its changes of 1 April 2019.", ["S04"], date="MCC 2017 Code 2nd edition, in force 1 April 2019 (S04).")
L("E023", "Law 18.3.2: 'the latter if completed shall not be regarded as short' becomes 'the run if completed ...'.", UN, "no_cause_stated", "low", "none", "A pronoun is replaced by 'the run' (a clarification); this is not on MCC's list of 2019 changes (S04) and no source states a reason.", ["S04"])
L("E028", "Law 19: OCR garble 'p'e' for 'play' in the 2019 text; same rule.", NC, "ocr_noise", "high", "derived", "The only differences are mis-recognised words (OCR errors); the rule is identical.", ["S18"])
L("E030", "Law 19: OCR garble 'v. :*' for 'within' in the 2019 text; same rule.", NC, "ocr_noise", "high", "derived", "The only differences are mis-recognised words (OCR errors); the rule is identical.", ["S18"])
L("E033", "Law 20: OCR truncation 'Pena' for 'Penalty' in the 2019 text; same rule.", NC, "ocr_noise", "high", "derived", "The only differences are mis-recognised words (OCR errors); the rule is identical.", ["S18"])
L("E034", "Law 20: OCR truncation 'e' for 'end' in the 2019 text; same rule.", NC, "ocr_noise", "high", "derived", "The only differences are mis-recognised words (OCR errors); the rule is identical.", ["S18"])
L("E035", "Law 21: OCR garble 'nc'' for 'nor' in the 2019 text; same rule.", NC, "ocr_noise", "high", "derived", "The only differences are mis-recognised words (OCR errors); the rule is identical.", ["S18"])
