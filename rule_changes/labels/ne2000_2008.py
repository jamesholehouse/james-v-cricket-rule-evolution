"""Labels added in round 4 (authored against that run)."""
from _h import make
ST, UN, NC, SW = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE", "SEMANTIC_WORDING"
PAIR = "2000_2008"
L, LABELS = make(PAIR)
L("E039", "Law 39 (Stumped), condition (iv): 'his wicket is put down by the wicket-keeper' becomes 'his wicket is fairly put down by the wicket-keeper'.", SW, "qualifier_scope", "low", "inferred", "The qualifier 'fairly' makes explicit that a stumping needs the wicket to be put down in accordance with the Laws; it may change how a doubtful dismissal is judged, but no source says the rule itself changed.", ["S01"], date="Between the 2000 Code and its 3rd edition of 2008; dates not documented in the sources found.")
L("E052", "Law 5 (women's ball): weight 4 7/8 oz to 5 5/8 oz and circumference 8 1/4 to 8 7/8 in. appear to become 4 15/16 oz to 5 5/16 oz (140 g to 151 g) and 8 1/4 to 8 7/8 in.", NC, "cleaning_artefact_numeric", "medium", "derived",
  "The 2000 text's fractions are wrong: 140 g is 4 15/16 oz and 151 g is 5 5/16 oz (the raw 2000 OCR reads '5s/i6'); the 2008 values agree with the gram figures given in both editions.", ["S17", "S01"], integrity="suspect")
