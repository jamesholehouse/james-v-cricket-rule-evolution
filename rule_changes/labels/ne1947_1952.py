"""Labels added in round 4 (authored against that run)."""
from _h import make
ST, UN, NC, SW = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE", "SEMANTIC_WORDING"
PAIR = "1947_1952"
L, LABELS = make(PAIR)
L("E022", "Law 42 (Stumped): the heading 'A striker is out Stumped' is a separate unit in the 1952 text and 'The Striker is out Stumped' is merged into the clause in the 1947 text; the stumping rule and the wicket-keeper rebound Note are the same.", NC, "segmentation_artefact", "high", "derived", "Same words; only the heading units differ.", ["S18"])
