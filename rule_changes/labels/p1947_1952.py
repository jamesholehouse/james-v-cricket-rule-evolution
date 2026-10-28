"""Labels for the 1947 -> 1952 edition pair (24 substantive events). Evidence: ACS transcriptions of the 1947 Code
1st and 2nd editions (S09, S08), MCC/Rait Kerr (S16), project audits (S17, S18)."""
from _h import make
PAIR = "1947_1952"
L, LABELS = make(PAIR)
ST, UN, NC = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE"
ED2 = "Wording found in the ACS transcription of the 2nd edition (adopted 7 May 1952) and not in the 1947 first edition (ACS)."

L("E001", "New Note on Law 1: no match with more than eleven a side can be regarded as First-class, and no side should field more than eleven.",
  UN, "no_cause_stated", "low", "none", "A new Note appears in the 2nd edition; no source gives a reason (the sentence 'a side should not field with more than eleven players' also leaves the Law text).",
  ["S08", "S09"], date=ED2)
L("E002", "Rolling Note revised (and 'the West Indies' added to the list of countries in the after-rain rolling Note): normal rolling before each day's play not earlier than half an hour before play; batting captain may delay it to 10 minutes before (plus a stray list number removed).",
  UN, "no_cause_stated", "low", "none", "Procedural change to pitch rolling in the Notes; present in the 2nd edition, absent from the 1st; no source states a cause.",
  ["S08", "S09"], date=ED2)
L("E003", "Further rolling/mowing Note revisions: rolling 'before the start of play' qualification; mowing on alternate days rather than by weekday wording; rest day counts as a day.",
  UN, "no_cause_stated", "low", "none", "Revision of the mowing provisions in the Notes (word-level changes: 'may'->'shall', 'third day'->'start', rest-day sentence added); present in the 2nd edition only; no cause stated.",
  ["S08", "S09"], date=ED2)
L("E005", "Note on Law 14 removed: 'In Australia the lead necessary to enforce a follow-on in a match lasting three days or more is 200 runs.'",
  ST, "codification_definition", "high", "stated", "ACS (S09): 'In September 1951 the Australian Cricket Board of Control agreed that the follow-on margin should be 150 rather than 200. Subsequent to that date, the Note was no longer published with the Laws.' The local variation (200 in Australia) disappeared because the Australian Board adopted the Law's own margin.",
  ["S08", "S09"], date="Australian Board decision September 1951 (S09); Note present in the 1947 first edition, absent from the 2nd edition (1952).")
L("E006", "Note 2 on Law 1 ('A side should not field with more than eleven players') replaced by the new Note (its substance reappears in the new Note on Law 1).",
  ST, "reorganisation", "medium", "derived", "Note 2 on Law 1 is replaced by the new Note: text comparison with the ACS 1st and 2nd editions shows it present in the first and in the Notes of the second.",
  ["S08", "S09", "S18"], date=ED2)
L("E007", "New Note on Law 20: if flags or posts mark a boundary, the line joining them is the boundary, which should be marked by a white line if possible.",
  ST, "notes_revision", "medium", "inferred", "Interpretive Note added in the 2nd edition (absent from the 1st); The ACS page's remark that the 2nd edition only corrected and added to the Notes could not be re-verified in the saved copy, so the cause is not taken as stated.",
  ["S08", "S09"], date=ED2)
L("E010", "New Note 4 on Law 25: the term 'dress' includes the equipment and clothing of players and umpires as normally worn.",
  ST, "codification_definition", "medium", "inferred", "A defining Note added in the 2nd edition (absent from the 1st); Law 31 (Note 5) and Law 30 refer to it.",
  ["S08", "S09"], date=ED2)
L("E011", "Law 30 revised: deliberate kicking or 'kneeing' of the ball by the striker is unfair and the umpire calls Dead ball with no runs; leg-bye/bye signal changed to touching a raised knee (the older wording about wilful deflection and the leg-raising signal removed).",
  UN, "no_cause_stated", "low", "none", "The kicking/'kneeing' Note and the raised-knee signal are in the ACS 'Original Law 30' (the 2nd edition, 1952) and not in the first; no source states why (a link to the pad-play debate is plausible but no source says so, so none is asserted). The 5 May 1954 amendment changed only the Law body ('except his hand' -> 'except his hand holding the bat'; see 1952_1962).",
  ["S08", "S09"], date="Wording of the 2nd edition as adopted 7 May 1952 (ACS 'Original Law 30'). The dataset's 1952 text is a genuine 1952 printing; the Note was itself replaced in late 1955/early 1956 (see the 1952-1962 pair).")
L("E012", "Law 31: no change of wording; differences are quote marks and an OCR fragment ('?\\ny' for 'Any').",
  "NOT_A_CHANGE", "format_artefact", "high", "derived", "Changed tokens are OCR fragments ('ny'/'any', 'tbe'/'the') and quote marks; the Law text is the same.",
  ["S18"], note="Only a different part of the Law differs. The 1954 wording of Law 31 ('if both bails be off') is in neither edition's text here.")
L("E013", "Law 31 definition: 'person includes a player's dress and equipment as normally worn' becomes 'person includes a player's dress as defined in Law 25, Note 4'.",
  ST, "codification_definition", "medium", "inferred", "The definition now points to the new defining Note on 'dress'; both are in the 2nd edition (the ACS 'Original Law 31' Note 5 already refers to Law 25, Note 4).",
  ["S08", "S09"], date=ED2, note="The ACS gives 'dress and equipment as defined'; the dataset/raw 1952 text gives 'dress as defined' (raw l.635). Difference unresolved. The 5 May 1954 amendment of Law 31 (both bails) is a different change, first visible in 1962.")
L("E015", "New Note on Law 34: the striker is out Bowled when the ball is deflected on to his wicket off his person even if an LBW decision might also be justified.",
  ST, "notes_revision", "medium", "inferred", "Interpretive Note added in the 2nd edition (absent from the 1st); no cause stated.",
  ["S08", "S09"], date=ED2)
L("E016", "New Note on Law 37: a batsman may not attempt to hit the ball twice if in doing so he baulks the wicket-keeper or a fieldsman attempting a catch.",
  ST, "notes_revision", "medium", "inferred", "Interpretive Note added in the 2nd edition (absent from the 1st); no cause stated.",
  ["S08", "S09"], date=ED2)
L("E019", "Law 43 Note: the striker may not be penalised for legitimate defence of his wicket 'except as provided for in Law 37, Note 2' (cross-reference to the new Note on Law 37).",
  ST, "notes_revision", "medium", "inferred", "Consequential cross-reference to the new Note on Law 37.",
  ["S08", "S09"], date=ED2)
L("E020", "Editorial pointer '(The notes to this Law are overleaf)' dropped.",
  ST, "wording_only", "medium", "derived", "A page-layout pointer, not rule text; its removal does not change any rule.",
  ["S18"])
L("E021", "New Note on Law 46: no player shall leave the field for a rub down or shower while play is actually in progress.",
  UN, "no_cause_stated", "low", "none", "A new conduct provision appears in the 2nd edition (absent from the 1st); no source gives a reason.",
  ["S08", "S09"], date=ED2)
L("E023", "Law 47: the words 'An appeal' move from the end of one clause to the front of the next.",
  NC, "segmentation_artefact", "high", "derived", "Changed tokens are only the repeated words 'an appeal': a heading word that sits at the end of one clause in one edition and at the start of the next in the other.",
  ["S18"])
L("E026", "Umpire's signal for a leg bye changed: 'raising the leg and touching it with the hand' becomes 'touching a raised knee with the hand'.",
  UN, "no_cause_stated", "low", "none", "Part of the 2nd-edition wording of Law 30 (see the Law 30 revision label; ACS 'Original Law 30' Notes); no source gives a reason.",
  ["S08"], date=ED2)
L("E028", "Drying-regulations Note: 'other grades of English Cricket' becomes 'other grades of Cricket in the United Kingdom'; 'wicket' becomes 'pitch' throughout.",
  ST, "terminology", "medium", "inferred", "The 1947 Code defined 'Pitch' and confined 'Wicket' to the stumps and bails (Rait Kerr), so the drying regulations are brought into line with that terminology.",
  ["S16", "S18"])
L("E029", "A sentence on removing the drier ('The drier shall be removed when they are satisfied that the pitch is fit for play, or as they may direct') appears in a different place in the drying regulations.",
  ST, "reorganisation", "medium", "derived", "The same sentence is removed from one paragraph and inserted in another: a move within the regulations, with 'wicket' -> 'pitch'.",
  ["S18"])
L("E030", "Matching removal of the 'drier' sentence from the paragraph that cross-refers to Law 46, Note 5.",
  ST, "reorganisation", "medium", "derived", "Other half of the drier-sentence move (the matching insertion elsewhere in the drying regulations).", ["S18"])
L("E031", "Ball size appears to change from 9 to 9 1/8 inches to 8 7/8 to 9 inches: not a real change. All independent transcriptions give 8 13/16 to 9 inches in 1947, 1952 and 1970.",
  NC, "cleaning_artefact_numeric", "high", "derived", "The raw 1947 OCR has no digits for the lower limit ('not less than inches, nor more than 9 inches'); the AI clean-up invented '9 ... 9 1/8'. The raw 1952 OCR reads '8ti?', which the clean-up rendered '8 7/8'. The ACS texts of the 1st, 2nd and 4th editions all say 8 13/16 to 9 inches.",
  ["S17", "S09", "S08"], integrity="suspect")
L("E032", "Law 5 Note on the new ball: outside the UK (or where local regulations differ) a new ball after 200 runs; in UK first-class matches a new ball after 65 six-ball overs instead of 200 runs; other-grades sentence reworded.",
  "ENJOYMENT", "bowler_batsman_balance", "low", "inferred", "Rait Kerr lists the new ball (granted in 1907 after 200 runs, which 'most certainly did encourage seam bowling') among 'other measures adopted to assist the bowler' and notes that 'in recent years this rule has been altered experimentally for first-class cricket to one under which a new ball can be claimed after a fixed number of overs'. He does not state the reason for the overs-based version.",
  ["S16", "S08", "S09"], date="Present in the 2nd edition, absent from the 1947 first edition (ACS); Rait Kerr (1950) describes the overs-based rule as experimental.")
L("E033", "Bat width appears to change from 4 1/4 to 4 1/2 inches: not a real change (4 1/4 inches since 1771).",
  NC, "cleaning_artefact_numeric", "high", "derived", "Raw 1952 OCR reads '42 inches' (garbled 4 1/4); the AI clean-up rendered it '4 1/2'. ACS texts of the 1947 Code (1st, 2nd, 4th editions) say 4 1/4 inches, as does Rait Kerr's chronology (limit set 1771).",
  ["S17", "S09", "S08", "S16"], integrity="suspect")
L("E034", "Bail length appears to change from 4 3/8 to 4 1/2 inches: not a real change. Real change in this event: the sentence 'The use of stumps with metal fittings is a source of danger and should not be encouraged' is dropped from the Note.",
  NC, "cleaning_artefact_numeric", "high", "derived", "Raw 1952 OCR reads '42 inches' for the bails; ACS texts of all three editions say 4 3/8 inches. The metal-fittings sentence is in the 1st edition and absent in the 2nd (a Notes revision; no cause stated).",
  ["S17", "S09", "S08"], sec="STRUCTURAL", secsub="notes_revision", integrity="suspect")
