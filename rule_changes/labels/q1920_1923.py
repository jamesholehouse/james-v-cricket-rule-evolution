"""Labels for 1920 -> 1923. Evidence: Rait Kerr (S16), ACS 1919/1922/1924/1927 Law texts (S37-04, S37-05; Laws only),
raw OCR, project checks (S17, S18). The ACS 1922 revision changed only 'For Australia only' variants (eight-ball over etc.),
which the project texts omit as country-specific, so no events here concern them. Most events undo 1920 OCR errors."""
from _h import make
PAIR = "1920_1923"
L, LABELS = make(PAIR)
ST, UN, NC, SW = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE", "SEMANTIC_WORDING"

def ocr(e, what, ev=("S18",)):
    L(e, what, NC, "ocr_noise", "high", "derived", "OCR misreading(s) in one edition; same wording otherwise.", list(ev))

L("E001", "One-day Law 1: 'first and' printed 'firstand' and final full stop missing in 1923.", NC, "format_artefact", "high", "derived", "Spacing/punctuation only (raw 1923 'firstand').", ["S18"])
ocr("E002", "Single-wicket Law 1: 'Law G' (1920 OCR) back to 'Law 6'.")
ocr("E003", "Single-wicket Law 2: 'oft' back to 'off'; page number '16' appended.", ("S17", "S18"))
ocr("E004", "Single-wicket Law 3: 'io'/'he' (1920 OCR) back to 'to'/'be'.")
ocr("E006", "Single-wicket Law 8: 'lost hall' back to 'lost ball'.")
L("E007", "Notes on Law 11: 1920 OCR garbles ('/V howler may howl', 'net', 'jwirt') corrected; 'No Ball' read as 'No Bail' and 'off' as 'off’' in 1923.",
  NC, "ocr_noise", "high", "derived", "OCR misreadings and a heading merge; same Notes.", ["S18"])
ocr("E008", "Notes on Law 12: 'rim'/'noton' back to 'run'/'not on'.")
ocr("E009", "Note on Law 13: 'he'/'lime' back to 'be'/'time'.")
L("E010", "Note on Law 16: '(see Laws 23 and 28)' rejoined to its sentence; ', dearly' back to 'clearly'.", NC, "segmentation_artefact", "high", "derived", "Record boundary and OCR only.", ["S18"])
L("E011", "Notes on Law 16: 'If one run is attempted and the batsman is run out the “No Ball” alone counts' merged with the next sentence (full stop missing in 1923).",
  NC, "segmentation_artefact", "high", "derived", "Same sentences; record boundaries only.", ["S18"])
L("E012", "Note on Law 18: heading detached and 'lu'/'bo' back to 'In'/'be'.", NC, "segmentation_artefact", "high", "derived", "Heading/record boundary and OCR only.", ["S18"])
ocr("E013", "Law 20: 'balls' (1920 OCR) back to 'bails'; 'be' read as 'bo' in 1923.")
L("E014", "Notes on Law 21 (Bowled): new Note 'The striker would be out under this Law if any part of either bail is “struck off” (see Law 20) the top of the wicket'; and the existing Note's 'giving a batsman out “Bowled”' becomes 'giving the striker out “Bowled”'.",
  ST, "clarification_umpire_workability", "medium", "inferred",
  "Both changes are in raw 1923 (l.381-385) and absent from 1920 raw. The new Note interprets 'struck off' in Law 20 (part of a bail displaced is enough), a ruling for umpires; 'batsman' -> 'striker' aligns the Note with the Law's heading ('The Striker is Out'), since only the striker can be bowled. The ACS places this Note in the 1927 revision of the Laws (S37-05), so it appeared among the Notes in this printing before it was formally attached to Law 21. Rait Kerr serial 135 (1947) later reversed it, requiring the bail to fall clear of the grooves (S16). No source states why the 1920s ruling was made.",
  ["S16", "S37-05", "S18"], sec=UN, secsub="no_cause_stated", date="First printed in the 1923 edition; formally a note to Law 21 in the ACS 1927 revision (S37-05).")
ocr("E015", "Notes on Law 22: 'Law !J2'/'hall' back to 'Law 32'/'ball'.")
L("E016", "Notes on Law 23: '“Run Out.”' restored to the first Note; 'oft' back to 'off'; 'of' read as 'oi'.", NC, "segmentation_artefact", "high", "derived", "Record boundaries and OCR only.", ["S18"])
ocr("E017", "Note on Law 24: '1 b w' read as 'lb w'.", ("S17", "S18"))
ocr("E018", "Note on Law 24: '1 b w' printed 'l.b.w'.", ("S17", "S18"))
L("E019", "Notes on Law 25: cross-reference '(See Law 16, Note 3.) *' attached to the following Note.", NC, "segmentation_artefact", "high", "derived", "Same text (raw 1920 l.321 and 1923 l.435 both have the cross-reference); record boundary only.", ["S18"])
L("E020", "Law 27 and Notes: 1920 OCR errors corrected and the heading fragment 'Either Batsman is' gone.", NC, "ocr_noise", "high", "derived",
  "OCR corrections; the heading 'Either Batsman is Out' is present in both raw texts.", ["S17", "S18"])
ocr("E021", "Note on Law 28: 'ball' read as 'nail' in 1923.")
ocr("E022", "Note on Law 32: 'off' read as 'oft’' in 1923.")
L("E023", "Law 33b and Note: page number '9' gone; 'off'/'struck' read as 'of!'/'stnick' in 1923.", NC, "ocr_noise", "high", "derived", "Page number and OCR only.", ["S17", "S18"])
L("E024", "Note on Law 34: 'A ball can only become “Dead” under Laws ... or on the call of a boundary hit' becomes '... or on the call of a boundary' ('33b' read as '336').",
  SW, "qualifier_scope", "medium", "derived",
  "Raw 1920 l.410 'boundary hit', raw 1923 l.523 'boundary' (also 1932). Dropping 'hit' covers boundaries reached by byes, leg-byes or overthrows as well as hits; this may change how the Note is read, but no source shows a change of rule (the ball was already dead on reaching a boundary).",
  ["S18"])
ocr("E026", "Note on Law 37: 'is well'/'is necessary' read as 'iswcll'/'isnecessaiy' in 1923.")
ocr("E027", "Law 39: 'to'/'be' read as 'tc'/'bo' in 1923.")
L("E030", "Law 42: first sentence merged with the next (no full stop in 1923); Note split at 'The Umpire must decide ...'.", NC, "segmentation_artefact", "high", "derived", "Same words (raw 1923 l.582-590); record boundaries only.", ["S18"])
L("E031", "Law 43 cross-reference: page number '11' vs '14' and a missing ')'.", NC, "format_artefact", "high", "derived", "Page numbers and punctuation only.", ["S17", "S18"])
ocr("E032", "Note on Law 46: 'How’s that?' read as 'Mow’s that?' in 1923.")
L("E033", "Law 53: 'three days’' printed 'threedays’'.", NC, "format_artefact", "high", "derived", "Spacing only; the 150/100-run limits are the same in both editions and in the ACS 1919/1922 texts (S37-04, S37-05).", ["S17", "S18", "S37-05"])
L("E034", "Law 55: the two-day clause 'Law 1 ‘one day matches’ shall apply' becomes 'Law 54 and Law 1 ‘one day matches’ shall apply' (also the three-day clause's 'Law 1' restored in the processed text).",
  ST, "consequential", "low", "inferred",
  "Raw 1923 l.675 reads 'Law 54 and Law 1' in the two-day clause; raw 1920 l.555 reads 'Law 1' only. It makes the declaration Law (54) apply on the one-day footing as the three-day clause already did; inferred as a consequential tidy-up. The 1920 processed text had dropped the '1' (raw has it): a clean-up artefact.",
  ["S18", "S37-05"], date="First printed in the 1923 edition.", integrity="suspect",
  note="The ACS 1922, 1924 and 1927 Law 55 texts (S37-05) have the two-day clause as 'Law 1 \"one day matches\"' only, without 'Law 54'. The dataset's printed text and the ACS disagree; unresolved.")
L("E035", "Notes on Law 9: new Note 'In week end starts the wicket may be mown on the Monday morning under the supervision of the Umpires'; the rolling Note now reads 'for not more than 10 minutes” immediately before the commencement of each innings'; '“the pitch”' sentence split off.",
  UN, "no_cause_stated", "medium", "none",
  "Both additions are in raw 1923 (l.221, l.224) and absent from raw 1920. The mowing Note deals with matches starting on a Saturday with the Sunday rest day; 'immediately' narrows when the 10-minute rolling may take place. No source gives a reason; Rait Kerr's chronology has nothing between serials 121 and 126 on rolling or mowing (S16), and the ACS shows Law 9 itself unchanged for England (S37-05).",
  ["S16", "S37-05"], sec=SW, secsub="qualifier_scope", date="First printed in the 1923 edition.")
L("E036", "Note on Law 9: '3ft Gin' (1920 OCR) back to '3ft 6in'.", NC, "ocr_noise", "high", "derived", "Raw 1920 l.139 'Gin'; raw 1923 l.238 '6in'. OCR misreading of a number.", ["S17", "S18"])
