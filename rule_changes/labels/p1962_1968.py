"""Labels for the 1962 -> 1968 edition pair. Dated amendments from the ACS 2nd-edition page (S08)."""
from _h import make
PAIR = "1962_1968"
L, LABELS = make(PAIR)
ST, UN, NC = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE"

L("E001", "Law 10 (Rolling, mowing and watering) Notes: mowing rules now distinguish matches of less than three days (no mowing unless 'Special Regulations' so provide) from matches of three or more days (mown before play on alternate days); the long explanatory Notes on what 'Special Regulations' are, and that they do not bind touring teams, are removed.",
  UN, "no_cause_stated", "low", "none", "ACS records Law 10 amended late 1966 or early 1967 (and changed late 1962 or early 1963); no source gives a reason.",
  ["S08"], date="ACS: Law 10 amended late 1966 or early 1967.")
L("E002", "Law 11: distance covers may extend in front of the popping creases appears to change from 3 1/2 feet to 8 feet: not real. Every independent transcription gives 3 1/2 feet.",
  NC, "cleaning_artefact_numeric", "high", "derived", "The raw 1968 OCR has no number ('...distance than feet in front of the Popping creases'); the AI clean-up supplied '8'. ACS texts of the 1947 Code (1st, 2nd, 4th editions) say 3 1/2 feet.",
  ["S17", "S09", "S08", "S10"], integrity="suspect", note="The quote marks around 'Special Regulations' are a real but trivial change.")
L("E004", "Law 15 Note added: a captain may forfeit his second innings; the interval is then 10 minutes and the decision must be notified in time to allow seven minutes' rolling.",
  UN, "no_cause_stated", "low", "none", "ACS records this Note added to Law 15 in late 1968 or early 1969; no reason is given.",
  ["S08"], date="ACS: Note added late 1968 or early 1969.", )
L("E005", "Law 18 Note extended: the last-over provision also applies if the batsman is out off, or retires after, the last ball of an over when less than two minutes remain at the end of the match.",
  UN, "no_cause_stated", "low", "none", "ACS records Note 2 on Law 18 amended late 1968 or early 1969; no reason is given.",
  ["S08"], date="ACS: Law 18 Note 2 amended late 1968 or early 1969.")
L("E008", "Law 26 (No ball) Notes: the sentence that an umpire may regard failure to notify a change in the mode of delivery as unfair and call No ball is moved from after the throwing-at-the-wicket Note to before it.",
  ST, "reorganisation", "medium", "derived", "The same sentence is removed and reinserted elsewhere in the Notes; no change of wording.",
  ["S18"])
L("E009", "Law 30 Note replaced again: the 1955/56 provision (leg byes from unintentional deflection are fair; Dead ball if the umpire is not satisfied the act was unintentional) becomes: deliberate deflection of the ball by any part of the striker's person other than the hand holding the bat is unfair, tested by whether the batsman attempted to play the ball with his bat; then Dead ball.",
  UN, "no_cause_stated", "low", "none", "ACS dates the change to May 1965; no reason is given.",
  ["S08"], date="ACS: Note changed May 1965.")
L("E010", "Law 41 (Run out): a sentence ('But unless he attempt to run, the Striker shall not be given Run out in the circumstances stated in Law 42, even should No ball have been called') is joined onto the preceding clause.",
  NC, "segmentation_artefact", "high", "derived", "The sentence is present in both texts; in the 1968 text it is run on to the previous sentence (with OCR noise 'give*'), so the diff sees it removed and re-added.",
  ["S18"])
L("E011", "New Note 2 on Law 43 (Wicket-keeper): if the umpire judges that the wicket-keeper's encroachment has gained no advantage, did not interfere with the striker, and had no effect on the dismissal, he shall disregard the infringement.",
  UN, "no_cause_stated", "low", "none", "The Note is in the raw 1968 OCR; no source gives a reason. It is not in the ACS transcription of the '4th edition (adopted 1970)', so it may have been dropped soon after, or the ACS page omits it.",
  ["S10"])
L("E014", "Ball weight and size written as '5 1/2, 5 3/4 ounces; 8 13/16 to 9 inches' instead of decimals: notation only (8.8125 = 8 13/16).",
  NC, "format_artefact", "high", "derived", "The values are identical to the previous edition's decimal values; only the way fractions are written differs. Integrity point: the raw 1968 OCR is garbled here ('not less than ounces ... not less than 8|i'), so the 1968 '8 13/16' and '5 1/2' were supplied by the AI clean-up (correct values, but not read from the raw text); the 1968 bat '4 1/2' likewise comes from a blank in the raw OCR ('not exceed inches').",
  ["S18"], integrity="suspect")
L("E015", "UK first-class new ball: after 65 six-ball overs becomes after 85 six-ball overs.",
  UN, "no_cause_stated", "low", "none", "ACS records the Law 5 Note changed late 1966 or early 1967 and its 2nd-edition text reads 85 overs; the independent text confirms the number. No source states why the interval was lengthened.",
  ["S08"], date="ACS: Law 5 changed late 1966 or early 1967.")
L("E016", "Bail length appears to change from 4 1/2 in. (1 inch projection) to 4 5/16 in. (1/2 inch projection): not real. The Law has always read 4 3/8 inches with at most 1/2 inch projection.",
  NC, "cleaning_artefact_numeric", "high", "derived", "Raw 1968 OCR reads '4-J inches' (garbled); the AI clean-up produced 4 5/16, which is also wrong (4 3/8 is the Law). The projection '1 inch' in the 1962 text was a raw-OCR misread of 1/2; the 1968 '1/2 inch' is correct. ACS texts of all editions say 4 3/8 and 1/2 inch.",
  ["S17", "S09", "S08", "S10"], integrity="suspect")
