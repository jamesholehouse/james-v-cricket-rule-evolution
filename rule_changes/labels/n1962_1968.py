"""Labels for events added after the first labelling pass (authored against the pipeline output of the verification-fix run)."""
from _h import make
PAIR = "1962_1968"
L, LABELS = make(PAIR)
ST, UN, NC = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE"
L("E003", "Law 13: a 'see also' cross-reference is added.", ST, "wording_only", "medium", "derived", "Only a cross-reference ('see also') is added; no rule changes.", ["S18"])
L("E009", "Law 37 (Hit the ball twice): OCR errors in the 1968 text ('an part', 'excep', 'froi') and spacing around the quoted heading; same rule.", NC, "ocr_noise", "high", "derived", "The differences are mis-recognised words and spacing.", ["S18"])
L("E012", "Law 45: the cross-reference '(see Law 10, Note 1)' is replaced by the lead-in 'Apart from Special Regulations'.", ST, "wording_only", "medium", "derived", "Only the cross-reference is replaced by an equivalent lead-in; the Law is unchanged in effect (the 'Special Regulations' Notes were removed from Law 10 in this pair).", ["S18"])
L("E013", "Law 47 appendix N.B. on drying regulations: 'in other grades of Cricket in the United Kingdom' becomes 'in other grades of Cricket' (the regulations' application elsewhere is at the discretion of the ground authorities).", UN, "no_cause_stated", "low", "none", "The UK qualifier is deleted from the N.B.; no source states why.", ["S08"])
