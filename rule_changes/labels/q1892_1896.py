"""Labels for 1892 -> 1896.

One MCC change in this interval: the follow-on limit raised (Rait Kerr serial 111, June 10th 1894; ACS 'The change in the 1894
revision was to Law 53', S35-03). Everything else is printing, OCR, segmentation or AI clean-up noise. 1896 text = Cricket Press
printing 'The Laws of Cricket. 1896. As revised by the Marylebone Cricket Club'.
"""
from _h import make
PAIR = "1892_1896"
L, LABELS = make(PAIR)
ST, UN, NC, SW = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE", "SEMANTIC_WORDING"

L("E001", "Law 13: 'No-ball', 'Wide ball', 'Over' printed 'no-ball', 'wide-ball', 'over'.", NC, "format_artefact", "high", "derived",
  "Capitals and hyphenation only.", ["S18"])
L("E002", "Law 16: 'wide ball' -> 'wide-ball'; 'if no run be otherwise obtained' -> 'if no runs be otherwise obtained'.", NC, "ocr_noise", "medium", "derived",
  "Hyphenation plus a singular/plural printing variant (both in raw OCR); one run is still added when none is otherwise obtained. The 1902 text reads 'no run' again, so this is not an MCC rewording.",
  ["S18"])
L("E004", "Law 2: the lead-in 'A run is scored—' is split off the first clause in 1896 ('1st So often as the batsmen ...').", NC, "segmentation_artefact", "high", "derived",
  "The 1896 raw OCR has 'A run is scored—' at the end of the previous line; the clause wording is unchanged.", ["S18"])
L("E005", "Law 4: ball circumference maximum '9¼in.' becomes '9½in.' in the processed texts.", NC, "cleaning_artefact_numeric", "high", "derived",
  "The raw OCR fractions are illegible in both ('9.fin.' 1892, '9|in.' 1896); ACS 1889/1894/1900 (S35-02, S35-03, S35-05) and the 1900 printing give 'nine inches and one-quarter' throughout. The 1896 ½ is an AI clean-up invention; Rait Kerr's chronology has no ball-size change before 1927.",
  ["S17", "S35-03", "S35-05"], integrity="suspect")
L("E006", "Law 48 ends with a stray '48*.' (1892) / '48½.' (1896); 'No-ball' -> 'No ball' in the 'especial care' Law.", NC, "segmentation_artefact", "high", "derived",
  "Both stray tokens are the next Law's number 48a (raw OCR '485.' in both printings) attached to Law 48 and then 'cleaned' into different numbers; the wording of both Laws is unchanged.",
  ["S18", "S17"], integrity="suspect")
L("E007", "Law 5: bat width '4½ in.' (1892 processed) becomes '4¼in.'", NC, "cleaning_artefact_numeric", "high", "derived",
  "Reverses an AI clean-up invention in the 1892 processed text (raw OCR 'If in.'); the bat width was 4¼ in. throughout (ACS S35-03; Rait Kerr: unchanged 'ever since 1771').",
  ["S17", "S16", "S35-03"], integrity="suspect")
L("E008", "Law 53 (follow-on): 'shall follow their innings, if they have scored eighty runs less than the opposite side' becomes 'if they have scored 120 runs less than the opposite side in a threedays match, or 80 runs in a two-days match.' (still compulsory).",
  "NOVEL_EVENT", "tactic_abuse", "medium", "inferred",
  "Rait Kerr serial 111 (June 10th 1894): 'The limit of runs for a “follow on” is increased to 120 runs in a three-day match. The Law still however provides no option in its application.' Ch.4: the compulsory follow-on 'was the subject of much muddled thought', and 'The University matches of 1891, 1893 and 1896 all pointed to the absurdity of a rule which forced a side to field for two consecutive innings'; he also says the follow-on and declaration alterations 'were primarily directed towards reducing the number of drawn matches'. In the 1893 University match Oxford apparently tried to throw away a wicket to follow on and 'C. M. Wells frustrated this intention by bowling two wide balls to the boundary', after which 'the follow on rule was adjusted for the subsequent season' (S35-07). The contemporary report of the 1894 meeting (S35-06) gives no official reason. The link to the 1893 incident is inferred from timing and Rait Kerr's mention of that match, not stated by MCC.",
  ["S16", "S35-03", "S35-06", "S35-07", "S35-08"], sec="ENJOYMENT", secsub="avoid_draws",
  date="Rait Kerr: June 10th 1894; ACS S35-03 (1894 revision, Law 53). First appears in the 1896 printing (no edition between 1892 and 1896).",
  note="ACS S35-03 transcribes only the 120-run figure; the 80-run two-day clause is in the 1896 printing and is also reported by secondary summaries.")
L("E009", "Law 6: bail length '4⅚in.' becomes '4¼in.' in the processed texts; 'during a match ... become unfit' printed 'during the match ... becomes unfit'.",
  NC, "cleaning_artefact_numeric", "high", "derived",
  "Raw OCR gives 4in. bails in both printings ('din,' 1892, '4in.' 1896), as do ACS S35-03/S35-05 ('four inches', projection 'half-an-inch'): the fractions are AI inventions. 'a'/'the match' and 'become'/'becomes' are printing variants (ACS keeps 'a match ... become'); same rule.",
  ["S17", "S35-03"], integrity="suspect")
