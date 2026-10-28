"""Labels for events added after the first labelling pass (authored against the pipeline output of the verification-fix run)."""
from _h import make
PAIR = "1980_1992"
L, LABELS = make(PAIR)
ST, UN, NC = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE"
L("E008", "Law 30: cross-reference 'See Law' 34.1' (OCR apostrophe) corrected to 'See Law 34.1'.", NC, "format_artefact", "high", "derived", "A stray OCR apostrophe in a cross-reference; the reference is the same.", ["S18"])
L("E010", "Law 37: the scorebook-entry sentence is duplicated in the 1992 digitised text ('the score book when the Striker is given out under the score book when a Batsman is given out'); same rule.", NC, "segmentation_artefact", "high", "derived", "The repeated words are a digitisation duplication; the entry ('obstructing the field', bowler gets no credit) is unchanged.", ["S18"])
L("E012", "Law 39 (Stumped), ball rebounding from the wicket-keeper: the wicket-keeper's person or equipment 'other than a protective helmet'.", UN, "no_cause_stated", "low", "none", "A helmet exception is added to the stumped-rebound rule (a helmet rule, like the run-out rebound exception in E014 of this pair); the ACS 1980 text (S11) already carries it though the dataset's 1980 text does not, so the date is unresolved. No source states a reason.", ["S01", "S11"], date="Between 1980 and 1992 (S01); dating unresolved.")
