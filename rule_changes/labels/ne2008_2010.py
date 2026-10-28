"""Labels added in round 4 (authored against that run)."""
from _h import make
ST, UN, NC, SW = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE", "SEMANTIC_WORDING"
PAIR = "2008_2010"
L, LABELS = make(PAIR)
L("E013", "Law 13 (Follow-on): 'the minimum required leads' becomes 'the minimum leads'.", SW, "clarifying_rewrite", "medium", "inferred", "The word 'required' is dropped; the leads (200, 150, 100, 75) are unchanged.", ["S01"], date="2000 Code 4th edition, effective 1 October 2010 (S01, S15).")
L("E023", "Law 16: 'completed on resumption of play' becomes 'completed on resumption'.", ST, "wording_only", "medium", "derived", "Two words dropped; no change in effect.", ["S18"])
L("E086", "Law 40 (wicket-keeper's equipment): 'the only member of the fielding side permitted to wear gloves and external leg guards' becomes 'the only fielder permitted ...'.", ST, "wording_only", "medium", "derived", "A defined term replaces its longer synonym ('fielder' for 'member of the fielding side', the 4th-edition drafting change); the equipment rule is unchanged.", ["S18"], date="2000 Code 4th edition, effective 1 October 2010 (S01, S15).")
