"""Labels for events surfaced by the second-pass classifier fixes (authored against the pipeline output of that run)."""
from _h import make
PAIR = "1980_1992"
L, LABELS = make(PAIR)
ST, UN, NC = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE"
L("E008", "Law 28 (The wicket is down): in the 1992 text 'providing that the bail is held in that hand' (1980: 'the ball') and 'the purpose of pulling the wicket down' (1980: 'putting').", UN, "no_cause_stated", "low", "none", "Two single-word differences in the bail-removal clauses. 'bail' for 'ball' looks like a digitisation/printing slip (the rule is about the hand holding the ball); 'pulling' for 'putting' is probably the same. Not checked against an independent 1992 transcription.", ["S01"], integrity="suspect")
L("E009", "Law 3 (umpires' signals): OCR error 'lips' for 'tips' of the fingers in the 1992 text; same signal.", NC, "ocr_noise", "high", "derived", "The only differences are mis-recognised words (OCR errors); the rule is identical.", ["S18"])
