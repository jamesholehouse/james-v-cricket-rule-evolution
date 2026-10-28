"""Labels for 1913 -> 1914. Evidence: Rait Kerr (S16; serial 121, 6 May 1914), ACS 1912/1914 Law texts (S37-02, S37-03),
raw OCR, project checks (S17, S18)."""
from _h import make
PAIR = "1913_1914"
L, LABELS = make(PAIR)
ST, UN, NC, SW = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE", "SEMANTIC_WORDING"

L("E001", "Single-wicket Law 2: page number '16' gone; 'off' read as 'oft' in 1914.", NC, "ocr_noise", "high", "derived", "Page number and OCR misreading only.", ["S17", "S18"])
L("E002", "Notes on Law 13: 'No Balls and Wides are recorded in their proper place on the score sheet' becomes '... should be recorded ...' (plus the next Note split at '(see. Law 45)' and a page number '8').",
  SW, "modal_strength", "high", "derived",
  "Raw OCR confirms 'are recorded' in 1910/1913 and 'should be recorded' in 1914 (raw l.184). A descriptive statement becomes an instruction to scorers; what is recorded is unchanged. The split sentence and the '8' are OCR/segmentation artefacts.",
  ["S18"])
L("E003", "Law 16: 'No Ball' read as 'No Bail' and 'be scored' as 'be’scored' in 1914.", NC, "ocr_noise", "high", "derived", "OCR misreadings; ACS Law 16 is unchanged (S37-03).", ["S18", "S37-03"])
L("E006", "Law 2: 'A run is scored:— 1st ... 2nd ...' split into separate records in 1914.", NC, "segmentation_artefact", "high", "derived", "Same words, different segmentation of the enumerated clauses.", ["S18"])
L("E007", "New Note (Law 2/run scoring): 'Where a batsman takes his guard in front of the popping crease and a run is made from that point it is not the custom for the Umpire to call “one short”.'",
  ST, "codification_definition", "medium", "inferred",
  "Genuine new Note (absent from 1913 raw, present in 1914 raw l.55-57 and later editions). By its own words it records existing custom, so it is read as codification; no source gives a reason (nothing in Rait Kerr, S16).",
  ["S16", "S18"], date="First printed in the 1914 edition.")
L("E008", "Heading 'The Striker is Out—' / 'The Striker is Out-' treated as a new provision.", NC, "segmentation_artefact", "high", "derived", "Heading present in both raw texts; only the dash differs.", ["S18"])
L("E009", "Notes on Law 23: the 'one bail' Note merged into the previous Note (with a page number '10') in 1914.", NC, "segmentation_artefact", "high", "derived",
  "Both sentences are present in both editions; only the record boundaries and a page number differ.", ["S17", "S18"])
L("E010", "Note on Law 24: 'l b w' printed 'lbw'.", NC, "format_artefact", "high", "derived", "Abbreviation spacing only.", ["S18"])
L("E011", "Note on Law 24: 'an l b w' printed 'an lbw'.", NC, "format_artefact", "high", "derived", "Abbreviation spacing only.", ["S18"])
L("E012", "Law 27: semicolon/dash restored and a page number '11' appended.", NC, "format_artefact", "high", "derived", "Punctuation and page number only.", ["S17", "S18"])
L("E013", "Heading 'Either Batsman is Out-' lost in 1914.", NC, "segmentation_artefact", "high", "derived",
  "1914 raw l.339 still reads 'Either Batsman is Out-'; the processed text kept only 'Either Batsman' as a fragment.", ["S18"])
L("E014", "Note on Law 28: 'Either batsman can be “run out” at any time ... including the bowler' gains '(except as provided above)'.",
  ST, "consequential", "high", "inferred",
  "Raw 1914 l.354 confirms the addition. It brings the Note into line with the May 1912 Law 28 proviso (striker playing at a No-ball not run out by the wicket-keeper unless the ball touched bat or hand: Rait Kerr serial 120, S16; ACS 1912, S37-02), which the old Note contradicted. Inferred consequential amendment.",
  ["S16", "S37-02"], date="Law change 1 May 1912; Note amended in the 1914 edition.")
L("E016", "Law 32: 'The Striker being caught no run shall be scored. A Batsman being run out ...' segmented as one sentence missing 'A' in 1914.", NC, "segmentation_artefact", "high", "derived",
  "Raw 1914 l.366 reads 'scored, latsman' (damaged 'A Batsman'); 1918 raw has the full text. Same Law.", ["S18"])
L("E017", "Law 33b: 'If the Ball' read as 'If the Bail' in 1914.", NC, "ocr_noise", "high", "derived", "OCR misreading (raw 1914 'Bail').", ["S18"])
L("E018", "Note on Law 35: 'anyway' vs 'any way'.", NC, "format_artefact", "high", "derived", "Word spacing only (raw 1914 itself reads 'anyway').", ["S18"])
L("E019", "Law 43: page number '14' appended.", NC, "format_artefact", "high", "derived", "Page number only.", ["S17", "S18"])
L("E020", "Note on Law 45: 'out-coming' vs 'out coming'.", NC, "format_artefact", "high", "derived", "Hyphenation only.", ["S18"])
L("E021", "New Law 55: 'Where there is no play on the first day of a three day match Laws 53 and 54 shall apply as if the match were a two day match, and if in a three day match there is no play on the first two days, Laws 53, 54 and Law 1 ‘one day matches’ shall apply as if the match were a one day match.'",
  "ENJOYMENT", "avoid_draws", "medium", "inferred",
  "Rait Kerr serial 121 (6 May 1914): if the start is delayed by weather the follow-on and declaration rules apply according to the days remaining (S16); ACS: the 1914 revision's only change was Law 55 (S37-03). Rait Kerr says the follow-on and declaration Laws 'were primarily directed towards reducing the number of drawn matches' (ch.4, S16); he states this for that family of Laws, not for serial 121 itself, so the cause is inferred.",
  ["S16", "S37-03"], date="Adopted 6 May 1914 (S16 serial 121; S37-03); first in the 1914 edition.")
L("E022", "Law 6: 'bail' (1913 OCR) back to 'ball'.", NC, "ocr_noise", "high", "derived", "1913 OCR misreading; ACS Law 6 reads 'ball' (S37-03).", ["S18", "S37-03"])
