# F3: fourth-pass verification of hand labels, 1857 to 1923

Scope: the final rows in `data/categories/event_labels_all.csv` for the 15 pairs from 1857_1884 to 1920_1923. There are **413 rows** (the brief estimated about 450): 254 NOT_A_CHANGE, 109 STRUCTURAL, 18 SEMANTIC_WORDING, 15 ENJOYMENT, 9 UNCATEGORISED, 5 NOVEL_EVENT, 2 ECONOMY and 1 EXTERNAL_FORCE. Of these, 400 are hand labels (`q*.py`) and 13 are mechanical.

I read every row's label next to its old and new change-record text. I checked against the following sources:
- the Rait Kerr text, with chapter boundaries located (ch.3 = lines 1889-2343, ch.4 = 2344-3092, ch.5 = 3093-3352);
- the gold chronology, serials 93-138;
- the raw OCR in `data/datasets/rule_texts/raw/`;
- the ACS transcriptions for 1884, 1889, 1894, 1899, 1900, 1902, 1906, 1910, 1912, 1914, 1919, 1922, 1924 and 1927, downloaded to the scratchpad;
- the OCR text of the *Cricket* pages cited as S34-01/02/03, S35-06 and S36-07/08/09/10;
- the Wikipedia pages cited as S35-07, S35-08 and S37-06.

All work was read-only. The only file written is this report.

## Verdict summary

| Group | Checked | Correct | Minor problem | Wrong / material |
|---|---|---|---|---|
| Real-change labels (not NOT_A_CHANGE; includes 18 SEMANTIC_WORDING and 4 mechanical STRUCTURAL/wording_only) | 159 (all) | 141 | 14 | 4 |
| NOT_A_CHANGE | 254 read; about 25 checked line by line against raw OCR or ACS | 252 | 2 (rationale wording) | 0 |
| Sources S34-S37 | 25 | 22 | 3 | 0 |

The quality is high:
- Every Rait Kerr serial is matched to the right event and date. That includes:
  - serials 95, 100, 101 and 102-107 (1884);
  - 108-110 (1889, first seen in 1890);
  - 111 (1894, first seen in 1896);
  - 113 (first seen in 1900);
  - 112, 114 and 115 (first seen in 1902, because the 1900 Wright & Co. pamphlet omits them);
  - 117 (first seen in 1906: the 1902 Lacey edition is dated March 1902 and its Law 7 Note still announces the proposal);
  - 118, 119, 120 and 121 (1914 and 1919).
- Edition-lag statements agree with the title pages in the raw OCR.
- Every quotation from Rait Kerr I tested is verbatim. That includes "public opinion so forced the issue", "clearly designed to help the bowlers", "quite improperly", "openly boasting", "a last-minute addition", "These changes were designed to save time during play", "completely accepted", the Lacey passage and "obscure amendment".
- The quotations from Taylor's 1901 series ("has done away with many disputes", "hat or any other article", the long-stop and leg-bye sentence) and from *Cricket* 1894 and 1906 are exact against the archive OCR.
- Every NOT_A_CHANGE claim I spot-checked against raw OCR held, including the numeric artefacts:
  - 1884-1896 bails 4¾ / 4½ / 4⅝ / 4¼ (raw "4in." and "din,");
  - 1892 bat 4½ (raw "If in.");
  - 1896 ball 9½ (raw "9|in.");
  - 1900 "middle stump" (raw "iu«ii>io ntump");
  - 1900 "allowances under 41" (raw "41");
  - 1890 "weigh no", "struck by" and "bail" (all present in the raw).

**No real Law change is hidden under an artefact label among the diffed events.** The one material omission is outside the labels: a whole section of the books is never diffed (problem 1 below).

## Problems

Severity: **M** = material (a wrong category, cause or missing change); **m** = minor (citation, wording or consistency).

| # | Sev | Event / item | Evidence | Correct reading |
|---|---|---|---|---|
| 1 | M | Coverage gap, 1906_1908 to 1920_1923 (no event exists) | The "Instructions to Umpires" section is not segmented or diffed. 1908 processed text, lines 539-541: "NEW BALL. After 200 runs have been made with a ball the fielding side can demand a new one." This is absent from 1906. Rait Kerr ch.4 (around line 2890): "The next advance in 1907 ... was the grant of a new ball after 200 runs had been scored off the old one". Change record `1908_1910_0033` (Law 4 Note: "(See Instructions to Umpires, “new ball.”)") is in no event, and nor is `1918_1920_0080` (its removal). Also undiffed: 1913 adds "Umpires should inform the batsmen when a new ball is about to be used."; 1923 narrows the rule to "After 200 runs have been made with a ball in the County Competition ..." and adds ball-gauging text. | A real bowler-assistance change (1907, first printed in 1908) is absent from the dataset, along with its later amendments. It needs a pipeline or segmentation fix, or manual events. |
| 2 | M | 1900_1902_E021 (Law 14), SEMANTIC_WORDING/modal_strength | The rationale itself says the 1900 wording "is a printer's paraphrase in the Wright & Co. edition ... not an M.C.C. change". The mirror event 1896_1900_E018 is labelled NOT_A_CHANGE/format_artefact. ACS 1899, 1900 and 1902 all read "shall be allowed ... provided only that he does not bowl two overs consecutively". | NOT_A_CHANGE (edition artefact). As labelled, it inflates the SEMANTIC_WORDING count and is inconsistent with E018. |
| 3 | M | 1902_1906_E015 (Law 54, two-day declaration), ENJOYMENT/avoid_draws, secondary ENJOYMENT, basis stated | The secondary category repeats the primary. The only cause-specific source (*Cricket*, 29 Mar 1906 and 3 May 1906, both verified) says "The time limit is ... inserted with a view to preventing the batting side from securing an unfair advantage in a failing light". That is a fairness reason for the restriction. Rait Kerr's "primarily directed towards reducing the number of drawn matches" covers the follow-on and declaration Laws as a group, and the Rait Kerr chapter is mis-cited as ch.5 (it is ch.4, line 2997). | Split the cause: the extension (first-day declarations in two-day matches) is avoid_draws, inferred from Rait Kerr's group statement; the 100-minute limit is fairness, stated by *Cricket*. Drop the duplicate secondary. |
| 4 | M | 1884_1890_E023 (new Law 54, declarations), secondary EXTERNAL_FORCE | Nothing in the rationale or the cited sources (S16, S35-02) supports an external force. Rait Kerr's stated reasons are drawn matches and the "burlesque" of batsmen getting themselves out. | Remove the secondary, or justify it. A candidate is NOVEL_EVENT/tactic_abuse, since Rait Kerr names the "burlesque of batsmen knocking down their own wickets". |
| 5 | m | Inconsistent basis across the declaration and follow-on family | The same Rait Kerr group statement gives basis **stated** in 1884_1890_E023, 1900_1902_E002, E057 and E058, 1902_1906_E015 and 1908_1910_E013. It gives **inferred** in 1857_1884_E070, 1896_1900_E012 and E034, 1913_1914_E021 and 1918_1920_E028. | Choose one rule. By the guide (a statement about a group of provisions is not a statement about this one), *inferred* fits everywhere. The exception is serial 114 (optional follow-on), where Rait Kerr gives a specific cause: Australian pressure and the 1899 Old Trafford Test. So 1900_1902_E002 and E057 may stay *stated*. |
| 6 | m | Rait Kerr chapter mis-cited as "ch. 5" for ch.4 passages | 1900_1902_E002, E057 and E058 (follow-on and declaration passage, lines 2995-3015); 1900_1902_E045 ("new-ball-after-200-runs rule followed in 1907 (Rait Kerr ch. 5)", line 2890); 1902_1906_E015; 1902_1906_E016 ("Other measures adopted to assist the bowler", bowling crease, line 2880); 1908_1910_E013. Other pairs correctly say ch.4. The Lacey and Notes passages *are* ch.5 (line 3160), so those citations are right. | Change these citations to ch.4. |
| 7 | m | 1857_1884_E034 (Law 19 to 26), SEMANTIC_WORDING/qualifier_scope | OLD: "either of the strikers prevent a ball from being caught, the striker of the ball is out". NEW: "either of the batsmen wilfully prevent a ball from being caught". The rationale itself says an accidental obstruction "is no longer out". | The text shows the rule narrowed, which by the guide is a rule change rather than wording. Better: STRUCTURAL/UNCATEGORISED, no_cause_stated. Debatable; flag to the owner. |
| 8 | m | Mechanical STRUCTURAL/wording_only rows that are OCR or segmentation noise | 1902_1906_E012 ("howling" for "bowling"); 1914_1918_E011 (lost "A" in "A Batsman", segmentation); 1920_1923_E025 (the clean-up's "i.e."; raw "Laws, l ie may", per 1918_1920_E021); 1920_1923_E028 ("lie" for "He"). The 1911_1913_E002 and 1918_1920_E025/E027 cross-reference relabelling rows are fine. | NOT_A_CHANGE/ocr_noise or segmentation_artefact. These are mechanical (08b) labels, not q-module labels, but they are in the final rows and count as STRUCTURAL. |
| 9 | m | 1908_1910_E008 (Law 28 Note) | WHAT says the "1908 OCR errors ('bis', 'hall', 'nail') corrected". But NEW (1910) reads "unless the bail had been touched": a new error (raw 1910 "nail", cleaned to "bail"). 1910_1911_E008 describes this correctly. | The label is right (NOT_A_CHANGE) but the description is inaccurate. |
| 10 | m | 1900_1902_E024 (Law 18) and mechanical 1892_1896_E003 | The rationale says "the 1896 and 1900 printings misplace the full stop". Raw 1896 line 109 reads 'call “ Play from that time uno trial ball'; raw 1900 line 116 reads 'call “playfrom that time ik) trial ball'. Neither printing has a full stop; it was introduced in processing (dropped closing quote). | The label is right (NOT_A_CHANGE); the explanation should say it is a processing or segmentation artefact, not a printer's error. |
| 11 | m | 1892_1896_E008 (follow-on 120) | The rationale quotes S35-07 as "'the follow on rule was adjusted for the subsequent season'". On the Wikipedia page this sentence is the article's own narrative, not part of the Wisden quotation, and reads "Partially as a result of this, the follow on rule was adjusted ...". Also, Rait Kerr ties the 1891, 1893 and 1896 University matches to the 1900 optional rule, not to the 1894 figure. | Add "partially" and attribute the sentence to Wikipedia, not Wisden. The label stays inferred and low to medium confidence, as it is. |
| 12 | m | 1857_1884_E071 (Law 6) | Correct, and integrity is rightly suspect. The rationale relies on raw OCR plus Taylor (S34-03); the ACS 1884 transcription (S35-01), which reads "four inches ... half-an-inch", is the stronger confirmation and is not cited here. | Add S35-01. |
| 13 | m | Source S35-07 note | It says the source "quotes Wisden on the 1893 University match ... and 'the follow on rule was adjusted for the subsequent season'". The second phrase is Wikipedia's own sentence and begins "Partially as a result of this". | Correct the note. |
| 14 | m | Source S34-03 note | It says Taylor "gives the 1884-code wicket as 8in wide with two bails of 4 inches each". Taylor prints the law current in January 1901, which is unchanged since 1884. His other claims (rolling rule first applied in Sussex v M.C.C. 1883; all restriction on arm height abolished 10 June 1864) are verified. | Say "the law as printed in 1901, unchanged since 1884". |
| 15 | m | Sources S37-01 and S36-06 | Both register the same ACS page (`.../1910.html`) with near-identical notes. | Merge, or cross-reference one to the other. |

## Sources S34-S37: accuracy of the notes

The following were verified as accurate against the fetched page or the local text:
- S34-01: leg byes, 2 May 1850, the "long stop" sentence.
- S34-02: "May 15th, 1845"; "or recovered ... has done away with many disputes"; "hat or any other article"; obstruction first mentioned in 1864; substitutes "generally granted".
- S34-04: the 1857 raw addenda dated "Toronto, May 29th, 1858"; "dangerous to the Batsman, and destructive of good cricket".
- S35-01 to S35-05 and S35-06: "120 runs are the limit now"; no discussion; under fifteen minutes.
- S35-08.
- S36-01 to S36-06.
- S36-08 and S36-09: "unfair advantage in a failing light"; F. B. May.
- S36-10: "with certain verbal alterations"; seven a.m.
- S37-02 to S37-04.
- S37-05: the 1922 Australia-only changes; the 1924 and 1927 Law 55 two-day clause reads "Law 1" only; the 1927 header reads "the addition of the note to Law 21".
- S37-06: 5 February, "eleven against five".

The S35-04 and S36-02 statement that ACS Law 10 still reads "the umpire shall call" is correct. The dataset's printed books, however, read "either Umpire" in Law 10 from 1900 through 1923. That suggests ACS reproduces only part of the change, and 1896_1900_E016 handles it appropriately at medium confidence.

## Could not verify

- S36-07 (*Cricket*, 28 Feb 1901, p.22, on Law 33b): the text I extracted from page 28 did not obviously contain "unaccountable", and I did not search it fully. 1900_1902_E040 uses this source only for an inferred, low-confidence cause.
- S37-07 (Papers Past): I did not fetch it; its note says it is bot-blocked.
- Page images of the scanned books: I relied on raw OCR, so I cannot independently confirm printed wording where both OCR and ACS are silent. This affects:
  - the 1896 two-day "80 runs" clause, which ACS S35-03 omits;
  - the 1920 and 1923 Law 55 "Law 54 and Law 1" wording, where ACS disagrees (raw 1920 lines 553-555 and raw 1923 lines 673-676 match the labels' description).
- The ACS pages give Laws only, not the Notes. So for the dates of the Lacey-edition Notes (1902-1923), "first printed in edition X" is the best available evidence, and the labels say so.
