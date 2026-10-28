"""Labels for events added after the first labelling pass (authored against the pipeline output of the verification-fix run)."""
from _h import make
PAIR = "1968_1980"
L, LABELS = make(PAIR)
ST, UN, NC = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE"
L("E035", "Law 29 (Batsman out of his ground): the definition is restructured under a heading ('When out of his Ground'); 'shall be held to be' becomes 'shall be considered to be out of his ground'; 'bat in hand' becomes 'bat in his hand'.", ST, "consolidation_merge", "medium", "inferred", "MCC states that the 1979 revision, begun in 1974, aimed 'to remove certain anomalies, consolidate various Amendments and Notes, and to achieve greater clarity and simplicity' (preface, S01). The change is confined to this one heading and wording.", ["S01", "S11"], date="1980 Code, approved 21 November 1979 (S01).")
