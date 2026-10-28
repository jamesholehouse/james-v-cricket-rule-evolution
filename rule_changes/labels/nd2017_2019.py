"""Labels for events surfaced after the xref/list-label classifier changes."""
from _h import make
NC = "NOT_A_CHANGE"
PAIR = "2017_2019"
L, LABELS = make(PAIR)
L("E054", "Law 4 (junior ball weight): 'Weight, from 4.69 ounces' becomes 'Weight- from 4.69 ounces'; same specification.", NC, "format_artefact", "high", "derived", "Only punctuation and spacing differ.", ["S18"])
