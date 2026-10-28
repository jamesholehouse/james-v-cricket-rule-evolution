# F2 – Fourth-pass verification of hand labels, pairs 1752_1755 … 1835_1857

Verifier: independent, read-only (no project file edited; no script run except read-only dumps into a scratch dir).
Scope: 350 rows in `data/categories/event_labels_all.csv` for the 15 pairs (137 labelled other than NOT_A_CHANGE, 213 NOT_A_CHANGE).

## Verdict summary

| Rows | Checked | Correct | Minor problem | Wrong |
|---|---|---|---|---|
| Real-change and SEMANTIC_WORDING/STRUCTURAL rows (137) | all 137, against the event's old/new records | 122 | 10 | 5 |
| NOT_A_CHANGE rows (213) | about 150 read against the text, covering every pair (all of 1774_1785, 1785_1786, 1788_1803 to 1816_1820, 1823_1828, 1828_1830, 1830_1835 and 1835_1857) | about 149 | 1 (rationale mismatch) | 0 |

- **No real change was found hidden under a NOT_A_CHANGE label.**
- **Rait Kerr serial numbers:** every serial cited (22-96) matches the gold CSV by date and subject.
- **Quotations from Rait Kerr:** about 30 were checked against the text file, including the ones on betting, the Nyren stumps passage, careless drafting, set policy, "turning a blind eye", round-arm, Lambert, full assault, "pin prick", "removing the uncertainty", "undecided matches", "drawn matches", "stamped out" and "later in the day". All are exact, apart from OCR noise in the source text.
- **Main weakness:** in 1830_1835, several wording changes are dated to the "1835 revision" and given labels, but the dataset's own 1823 text already has that wording. In the 1823_1828 pair, the same labelling effort correctly treats these differences as edition artefacts, so the two pairs are inconsistent. One real error follows from this: a claim that "towards the bowler" is new in 1835.
- **Second weakness:** an ECONOMY label for the Bets section disappearing in 1857 contradicts both Rait Kerr and the 1857 scan.

Severity: nothing affects a cause attribution backed by a "stated" basis. All 24 "stated" labels are justified by the quoted passages. The errors are dating and edition-artefact problems that inflate the count of SEMANTIC_WORDING and ECONOMY changes in 1830-1857.

## Problems

| # | Event | Severity | Label says | Evidence | Correct reading |
|---|---|---|---|---|---|
| 1 | 1830_1835_E040 | Wrong | SEMANTIC_WORDING. "The only new words are 'towards the bowler' (also in the March 1835 proposal)", dated "1835 revision". | `processed/1823_processed.txt` line 18: "with a RETURN CREASE at each end towards the Bowler at right Angles". The 1823_1828_E059 note itself says "'towards the Bowler' is missing in the 1828 reprint but present in ACS 1829 Law 4". | Nothing in this event is new in 1835. The whole difference is an artefact of the 1830 booklet (and the 1828 reprint). Should be NOT_A_CHANGE / edition_artefact. |
| 2 | 1830_1835_E010 | Wrong (date / double count) | SEMANTIC_WORDING. Catch wording 'from the stroke of the bat, or hand, but not the wrist', dated "1835 revision". | 1823 text (1820_1823_E024, new side): "from a Stroke of the Bat, or Hand, (but not wrist)". This change is already labelled SEMANTIC_WORDING in 1820_1823_E024. The 1830 booklet reprints the 1820 'over or under the bat'. | NOT_A_CHANGE / edition_artefact. It counts the 1823 change a second time. |
| 3 | 1830_1835_E013 | Wrong (date / double count) | SEMANTIC_WORDING. 'under pretence of running a notch' -> 'running', "1835 revision". | 1823 text (1820_1823_E024): "under Pretence of running or otherwise". | NOT_A_CHANGE / edition_artefact (1830 booklet). |
| 4 | 1830_1835_E022 | Wrong (date / double count) | SEMANTIC_WORDING. 'no notch' -> 'no run', "1835 revision". | 1823 text (1820_1823_E002/E017): "When a Ball shall be caught no run shall be reckoned". | NOT_A_CHANGE / edition_artefact. |
| 5 | 1835_1857_E023 | Wrong (medium) | ECONOMY/betting_stakes, inferred, for the absent Bets section. Its date says the absence "may be ... a loss in the missing pp.10-11". | Rait Kerr ch.3: the bets rules stayed in the Laws until "the first step taken in the revision of the code in 1884 was to delete these in toto". Raw 1857 OCR, lines 249-265: page 12 holds Single Wicket rules 6-10 and then the printer's colophon "Rowsell & Ellis, Printers". The Bets section (which followed Single Wicket in 1835) was never printed in this Toronto booklet, so missing pages cannot explain it. | NOT_A_CHANGE / edition_artefact (publisher's omission). The single-wicket wording items in the same event are already treated as noise. The 1884 deletion has no event because of this. That gap should be noted, not filled by labelling 1857. |
| 6 | 1830_1835_E045 | Minor (date) | 'No Notch' -> 'One Short' attributed to the 1835 revision. | 1823 text (1820_1823_E007): "If the Striker run a short run the umpire must call 'One Short'". The 1823_1828_E065 rationale also says ACS 1829 has 'One Short'. | Only 'either of the strikers' is new in 1835. The call itself is a booklet artefact and is counted twice. |
| 7 | 1830_1835_E023, E031 | Minor (date) | 'notch' -> 'run' credited to the 1835 revision. | 1823 already had 'the Run which they were attempting' and 'add five Runs' (1820_1823_E002). 'player' in 1830 is the booklet's wording: the 1820 facsimile and 1828 both read 'any Person'. | Only 'he and his partner' (E023) and 'fieldsman' (E031) are new in 1835. |
| 8 | 1830_1835_E051 | Minor | Single-wicket "new: ... 'crease in a line with it ... or go beyond them'; 'nor shall the striker be caught out behind wicket, nor stumped out'" credited to the 1835 revision. | All three phrases are in the 1823 broadsheet (1820_1823_E009 new text, and 1823_1828_E068 says so). | These are booklet / 1828-reprint artefacts. Only Law 47 (serial 86) and 'No bet is payable…' (first seen in the 1835 text) are new. |
| 9 | 1823_1828_E068 | Minor | UNCATEGORISED, substantive_change=1. The rationale itself concludes these are "probably omissions of that reprint rather than MCC changes". | The rationale reasons the same way (1835 restores the 1823 forms; the reprint misnumbers the law as '44th'). | Should be NOT_A_CHANGE / edition_artefact, or at least substantive_change=0. The label contradicts its own rationale. |
| 10 | 1828_1830_E008 | Minor | NOVEL_EVENT/bowling_innovation, stated (serial 70), source_edition_issue=0. | The label admits the 1830 text is the c.1811 form, not the 19 May 1828 law ("The ball shall be bowled. If it be thrown or jerked…", raw 1828 lines 197-205). | Attaching serial 70 to an artefact event is a judgement call. source_edition_issue should be 1 to match the label's own integrity="suspect". |
| 11 | 1823_1828_E019 | Minor (NOT_A_CHANGE rationale) | The rationale is the notch/run boilerplate ("all read 'run' ... 'notch' disappeared"). | The event is about the catch wording ('over or under the bat, or upon his hands'), not notch/run. | The label (NOT_A_CHANGE) is right but the rationale is wrong. It should cite the 1823 wording and ACS 1829 'stroke of the bat, or hand'. |
| 12 | 1803_1806_E008 | Minor (citation) | "ch.6 says first in the official 1816 version" (trial balls). | Serial 57 in ch.6 says only "A fresh bowler is allowed two trial balls…". The words "a change which first appears in the official 1816 version" are in **Appendix III** (the Wallis undated broadsheet entry, text lines 5996-6001). | Cite App. III. |
| 13 | 1830_1835_E006 (also E020) | Minor | E006 is STRUCTURAL/clarification_umpire_workability, stated. | Rait Kerr ch.3 (text lines 1928-1935): the 1839 LBW change and "two other alterations designed to tighten up the Law for 'Wides'" were "all directed towards limiting [round-arm's] effect". E020 cites this passage. E006 omits it and uses only "removing the uncertainty". | Add the round-arm aim as the main or a secondary cause for E006. |
| 14 | 1752_1755_E001 | Minor (basis) | SEMANTIC_WORDING, basis "stated". | Rait Kerr's "gradual modernisation ... ceasing to be referred to as 'She' or 'Her'" (line 1169) is evidence he uses to order undated printings. It does not state why the wording was changed. | "inferred" would be more accurate. The quote itself is exact. |
| 15 | 1828_1830_E004 | Low | "Neither Rait Kerr (ch.2, ch.6) nor S33-02 gives a reason." | Ch.2, lines 1835-1838: restraint on the "New style" was insisted on "by the introduction of penalties for both 'No balls' and 'Wides'". Serial 71 is about how a wide is recorded, not a penalty, so the label is defensible. | Optionally mention this passage. |

## Edition identities (checked against Rait Kerr App. III, text lines 5642-6137, and raw OCR)

- **'1774' = Blake, Maidstone, c.1786.** Supported by content. The text has two bails in two places (raw lines 44 and 96), a Hit wicket law, and the "unless he returns" single-wicket clause. These are exactly the three features App. III lists for Blake. However, the raw title is "New LAWS &c. Of The Game of Cricket", while Rait Kerr gives Blake's title as "New Articles of the Game of Cricket…". The identification therefore rests on content, not on the title page. The labels' wording "by Rait Kerr's App. III description" is appropriately hedged; the DATA_INTEGRITY table states it more firmly than the evidence allows. It is not Blake's second issue: the text still has the old obstruction wording.
- **'1786' = Turpin.** Consistent with the raw text: "LAWS, &c", then "END of the NEW LAWS", then the 1755 code. Rait Kerr says Turpin is identical to the 1774 Ridley text and has no third-stump note. Ch.2 (line ~1428) also says a 1786 edition of the 1774 Laws contained the 1755 code.
- **'1806' = Bailey (undated, binding 1806, c.1809-11):** correct (App. III, lines 5944-5991).
- **'1809' = Baxter (Lewes), unreliable:** correct.
- **'1828' = Sporting Magazine via Scores and Biographies:** correct (raw header). The raw text appends the 19 May 1828 resolutions, which the processed Laws do not include. Rait Kerr's "1827" entry says Haygarth took these Laws from the Sporting Magazine. This fits serial 62 ("omitted in 1827").
- **'1830' = an unofficial booklet:** consistent with the commentary preamble and the content. No publisher name survives in the OCR, so equating it with the Lewis & Co. / Clapshaw booklet is inferred from content. The labels' phrase "1819/1820 MCC wording" is an approximation: App. III says the Farnham (Clapshaw) editions "differ both in arrangement and content from the Craft edition of 1820".
- **'1835' = amended to c.1845:** confirmed. The processed text contains serials 82-92 (ball circumference, three stumps, no trial balls, both bails, bat practice, LBW 'pitched', ten minutes, all runs from wides, 'so closely infringe', 'fairly within the reach', change ends) and lacks serial 93 (sweeping and rolling, which appears in 1857).
- **'1857' = Toronto, Rowsell:** confirmed (raw header; addendum dated Toronto, 29 May 1858). Laws 44-47 are visibly imputed from 1835 (identical line breaks). As a result, serial 95 (the 1854 follow-on change to 60/80 runs) is invisible in 1857; q1857_1884 handles it.

## Sources S31-S33 (data/evidence/sources.csv)

- **S31-04:** accurate. Raw titles: 1803 "THE MANLY GAME" (Pocock), 1806 "NOBLE GAME" (Bailey), 1809 Baxter, 1816/1820 Craft "Authority" headers, 1786 "END of the NEW LAWS".
- **S32-02:** accurate. The facsimile is at text lines 1562-1695. It confirms 'rolling', 'This rule is not meant to prevent', 'when the Ball is delivered', 'shill have pitched' and 'back of the hand'.
- **S33-03:** accurate (raw 1835 lines 1-163). The circular is dated 20 March 1835. It mentions italics and the 14 May vote. It proposes a 4 ft 4 in popping crease and a 9 1/8 in ball limit. Laws 38-42 are illegible, and the struck-out proposal to deduct runs for a short run survives (lines 118-122).
- **S33-01:** I did not open data_appendix.xlsx, so its note is unverified.
- **S32-01 and S33-02 are duplicates** (same ACS 1829 URL). S33-02 is marked as fetched through a summarising tool. Merge them, or say which one was checked by hand.
- **S31-01, S31-02, S31-03 and the ACS 1829 contents:** not verifiable here (no web access used). All claims built on them (for example "ACS 1774 has no Hit wicket", "Wallis 1809 lacks 'Which are three'") are unverified by me. They are consistent with Rait Kerr's descriptions wherever he covers the point.

## Notes (not errors)

- 1830_1835_E033 marks the 'reasonable distance' clause as suspect. The 1857 text, on pages that survive, also lacks the clause. This supports it having been dropped by c.1845-1857 rather than lost in one printing.
- 1830_1835_E043 and E057 both count the 'on the ground' change: once in the Bowler law and once in the umpires' no-ball law. These are two textual sites of one decision.
- The 1774_1785_E012 Hit wicket removal is labelled as a real change even though the event comes from the edition order. The label explains this clearly and dates the change to 1774; I accept it.

## Not verified

- ACS online transcriptions (1755, 1774, 1809, 1829).
- data_appendix.xlsx (S33-01).
- Taylor 1901 (S34-*), cited in 1835_1857_E003/E011/E014/E015. Out of the S31-S33 scope and not read.
