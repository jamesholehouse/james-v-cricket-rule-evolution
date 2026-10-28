"""Labels for events surfaced by the cross-reference-change class."""
from _h import make
ST, UN, NC = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE"
D19 = "MCC 2017 Code 2nd edition, in force 1 April 2019 (S04)."
PAIR = "1952_1962"
L, LABELS = make(PAIR)
L("E003", "Law 16 (start of play delayed by weather): 'Laws 14 and 15 shall apply' becomes 'Law 14 shall apply' in accordance with the number of days' play remaining.", UN, "no_cause_stated", "low", "none",
  "ACS records Law 16 as amended on 1 May 1957, the date of the declaration change that removed the day-of-match restrictions from Law 15. The link to that change is an inference and no source states the reason.", ["S08"], date="ACS: Law 16 amended 1 May 1957.", sec=ST, secsub="consequential")
