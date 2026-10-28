"""Labels for events added after the first labelling pass (authored against the pipeline output of the verification-fix run)."""
from _h import make
PAIR = "1992_2000"
L, LABELS = make(PAIR)
ST, UN, NC = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE"
L("E015", "Law 18: 'So often as the Batsmen, after a hit or at any time while the ball is in play, shall have crossed...' becomes 'so often as the batsmen, at any time while the ball is in play, have crossed...': 'after a hit or' dropped.", ST, "wording_only", "medium", "inferred", "The definition of a run drops 'after a hit or'; the 2000 re-write aimed to remove ambiguities (S01 preface), but the rule is unchanged in effect.", ["S01"], date="2000 Code, approved 3 May 2000 (S01).")
L("E043", "Law 24/37: cross-reference 'See Law 42.12.' becomes 'See Law 42.17(b)'.", ST, "consequential", "medium", "derived", "A cross-reference renumbered with the 2000 re-write.", ["S18"])
