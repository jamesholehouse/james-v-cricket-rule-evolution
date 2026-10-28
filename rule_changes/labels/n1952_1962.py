"""Labels for events added after the first labelling pass (authored against the pipeline output of the verification-fix run)."""
from _h import make
PAIR = "1952_1962"
L, LABELS = make(PAIR)
ST, UN, NC = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE"
L("E001", "Law 10 after-rain rolling Note extended: 'In Australia, South Africa, the West Indies, and New Zealand' becomes 'Except in the United Kingdom' (the damaged rain-affected pitch may be swept and rolled for up to ten minutes).",
  UN, "no_cause_stated", "low", "none", "The territorial scope of the rolling Note is widened from four named countries to every country except the UK; the ACS dates the change to late 1962 or early 1963 (the West Indies had been added in the 1947-52 pair). No source states a reason.",
  ["S08"], date="ACS: changed sometime late 1962 or early 1963.")
L("E011", "Law 42: the heading 'A striker is out Stumped' sits at the head of the clause in 1962 instead of as a separate unit; same rule.", NC, "segmentation_artefact", "high", "derived", "The same words occur in both editions; the heading was a separate unit in the earlier text.", ["S18"])
L("E013", "Law 46 Note on intimidatory bowling: new sentence 'The captain shall take the bowler off as directed.'", UN, "no_cause_stated", "low", "none", "Part of the later, undated tightening of the intimidation Note ('Request' -> 'Direct' of this pair); the ACS 2nd-edition text, which already has the 1953 revision, does not carry the sentence. No source states a reason.",
  ["S08"], sec=ST, secsub="notes_revision")
L("E015", "Law 47 appendix, drying regulations: footholds on the pitch may be dried as directed by the umpires at any time; the groundsman may protect against bowlers' marks with sawdust only if the umpires so direct; the paragraph on removing the drier is dropped.", UN, "no_cause_stated", "low", "none", "A procedural change to who controls pitch drying (compare E013); no source gives a reason or a date.", ["S08"])
L("E007", "Law 27: OCR errors in the 1952 text ('docs', 'arc') are corrected in 1962; same rule.", NC, "ocr_noise", "high", "derived", "The only differences are mis-recognised words (OCR errors); the rule is identical.", ["S18"])
L("E009", "Law 29: OCR error 'cither' corrected in 1962 ('break' -> 'breaks' is grammatical only); same rule.", NC, "ocr_noise", "high", "derived", "The only differences are mis-recognised words (OCR errors); the rule is identical.", ["S18"])
L("E012", "Law 35 (Caught): OCR errors in the 1952 text ('n<', 'lodgin') corrected in 1962; same rule.", NC, "ocr_noise", "high", "derived", "The only differences are mis-recognised words (OCR errors); the rule is identical.", ["S18"])
