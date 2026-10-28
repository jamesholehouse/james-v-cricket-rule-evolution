# Data-integrity findings (from the change-detection work)

The processed rule texts (`data/datasets/rule_texts/processed/`) are OCR output cleaned by an AI pass. Comparing them with the raw OCR
(`.../raw/`) and with independent transcriptions showed that **some numbers in the processed texts are wrong where the OCR was illegible**,
by one of two mechanisms:

- **AI clean-up invention**: the raw OCR is garbled or empty and the clean-up supplied a plausible number (1947 ball size, 1952 bat and
  bails, 1968 covers, 2000 ball, 2019 bat covering).
- **OCR misread kept in the text**: the raw OCR itself already contains the wrong character and the clean-up kept it (1962 bail projection
  "1 inch", 2010 ball "815/16", 2017 "m" for "in").

A "change" built on such a number is not a change to the Laws. Everything below was found by `scripts/07_audit_numeric_cues.py`,
`08a_acs_presence.py` and hand checks (re-checked line by line against the raw OCR by the Opus verification, see
`verification/C_labels_2000_2019_report.md` section 6), and is recorded as `NOT_A_CHANGE / cleaning_artefact_numeric` labels in
`data/categories/post1947_event_labels.csv` (see the counts printed by `08_build_labels.py`; labels with `integrity = suspect` mark the
events whose source text is doubtful).

| Edition (dataset) | Text says | Raw OCR | Independent source says | Mechanism |
|---|---|---|---|---|
| 1947 | ball 9 to 9 1/8 in. | "not less than inches, nor more than 9 inches" (lower limit missing) | ACS 1947 Code: 8 13/16 to 9 in. | clean-up invented the lower figure and changed the upper limit from 9 to 9 1/8 |
| 1952 | ball 8 7/8 to 9 in.; bat 4 1/2 in.; bails 4 1/2 in. | "8ti?", "42" (garbled) | ACS (1st, 2nd, 4th eds): 8 13/16-9; 4 1/4; 4 3/8 | clean-up |
| 1962 | bat 4.5 in.; bails 4.5 in. | "4\|" | ACS: 4 1/4; 4 3/8 | clean-up |
| 1962 | bail projection 1 in. | "1 inch" | ACS: 1/2 in. | OCR misread of 1/2, kept in the text |
| 1962 | ball size 8.8125 in. | "8-$- inches" | 8 13/16 = 8.8125 | correct by luck: the clean-up produced the right value from garbled OCR |
| 1968 | covers 8 ft in front of the crease; bails 4 5/16 in.; bat 4 1/2 in. | "distance than feet" (number missing); bails "4-J"; bat "exceed inches" (no digit) | ACS: 3 1/2 ft; 4 3/8 in.; 4 1/4 in. | clean-up |
| 1968 | ball 8 13/16, weight 5 1/2 | garbled ("not less than 8\|i", "not less than ounces") | same | correct by luck |
| 2000 | ball lower limit 8 3/4 in.; women's ball 4 7/8, 5 5/8 oz | "8'K>" (garbled); women's "5s/i6" (= 5 5/16) | MCC 2010 text: 8 13/16; 4 15/16, 5 5/16 oz | clean-up |
| 2000 | bail/spigot figures appear missing | present, displaced into the next table block | - | **not an error**: table-layout displacement, a segmentation artefact |
| 2008 | commercial-identification thickness 0.08 in/0.2 mm; covering 0.012 m | "m" for "in" | 0.008 in/0.2 mm (MCC 2010) | printing/OCR error corrected in 2010 |
| 2010 | ball lower limit 8 15/16 in. | "815/16 in/22.4cm" | MCC 2010 text: 8 13/16 (22.4 cm = 8 13/16) | OCR misread, kept in the text |
| 2010 | junior ball 8 5/8 in. | "8“/i6" (8 11/16) | MCC 2010 text: 8 11/16 | clean-up |
| 2010 | women's ball lower limit 8 1/2 in. | "8V2" | MCC 2010 text: 8 1/4 (21.0 cm = 8.27 in) | clean-up (second artefact in the same event as the junior ball) |
| 2017 | men's ball "8.81 m/22.4 cm ... 9 m"; women's lower limit "8.25 m" | "m" in both 2017 and 2019 | inches (MCC 2026 text: 8.81 in/22.4 cm) | OCR unit misread; the 2019 clean-up corrected it, the 2017 one did not |
| 2019 | bat covering 0.004 in./0.1 cm | "0 04 m/0.1 cm" | 0.04 in./0.1 cm (MCC 2026 text) | clean-up turned a correct 0.04 into 0.004 |

Other findings:

- **Edition printing dates.** The dataset's "1952" text is a genuine 2nd-edition (1952) printing. Its Law 30 and Law 31 carry the original
  (pre-amendment) wording of the ACS 2nd-edition page ("except his hand"; "if either or both of the bails be previously off"), and the
  kicking/"kneeing" Note and raised-knee signal in Law 30 are *original 2nd-edition* wording. The 5 May 1954 amendments ("except his hand
  holding the bat"; "if both bails be off") first appear in the dataset's 1962 text. An earlier version of this file claimed the 1952
  text carries 1954 wording; that claim was refuted by the verification and is withdrawn. Several rule changes still appear one edition
  later than Rait Kerr dates them (e.g. serials 112 and 115, dated 1899-1900, first appear in the 1902 edition).
- **ACS pages are not clean snapshots.** The ACS pages (S08, S10, S11) show amended text with the originals inset; the "1980 Code" page
  includes later amendments (helmet placement 41.4, "may request to have the pitch rolled", stumped "other than a protective helmet").
  Agreement with an ACS page therefore does not by itself confirm the wording of a dated edition.
- **1890 reversion.** 12 of the 39 modified records from 1890 to 1892 return to wording found verbatim in 1884 but not in 1890; several of
  these are transcription typos in the 1890 dataset text ("commencemen", "no less than"), not evidence of a separate printing. Wording-only
  differences there are noise.
- Whole-Law boundaries in the digitised 2017/2019 texts differ (Laws 2/3), producing relocation artefacts that are labelled as such.
- OCR garbage tokens ("docs" for "does", "froi" for "from", "lawigTboundaries") are identified by `scripts/_textclass.py` (class
  `ocr_noise`: a rare token paired with a near-identical frequent word) and labelled `NOT_A_CHANGE / ocr_noise`.

## Wrong or unreliable editions (found while labelling 1744-1947)

Differences caused by these are labelled `NOT_A_CHANGE / edition_artefact` (or flagged `source_edition_issue = 1`), and the rationale says what the real
edition is. Sources: Rait Kerr Appendix III (list of editions), title pages in the raw OCR, ACS transcriptions of the official text.

| Dataset edition | What it really is |
|---|---|
| 1774 | Probably Blake's Maidstone edition (c.1786) - identified by content only (the title page reads 'New LAWS &c. Of The Game of Cricket', not Blake's 'New Articles'): has Hit wicket, an extra single-wicket clause and a third-stump note that the ACS 1774 text lacks. |
| 1786 | Turpin's 1786 booklet, in effect the true 1774 code (the 1755 code tacked on was removed). So 1774->1785 and 1785->1786 events largely run backwards. |
| 1806 | J. Bailey's undated printing, c.1809-11 in content (matches the 1811 Liverpool edition). |
| 1809 | Baxter's Lewes booklet, which Rait Kerr calls unreliable; differs from the authentic Wallis text of May 1809. |
| 1820 | AI clean-up errors: drops "rolling", inverts "is not meant to prevent" to "is to prevent", invents "when the Ball shall be delivered". |
| 1823 | "Bat" for "Hat" (raw OCR "pat"). |
| 1828 | A reprint (Sporting Magazine via Scores and Biographies): reverts to "notch" wording; stops before the 19 May 1828 amendments. |
| 1830 | Unofficial booklet repeating 1819/1820 wording, omitting laws still official; a page (9-11) missing. About 50 events are artefacts of it. |
| "1835" | The 1835 Code as amended to c.1845 (contains Rait Kerr serials 82-92, not 93). |
| 1857 | A Toronto reprint (Rowsell) printed before May 1858; pages 10-11 missing and filled from 1835. |
| 1884 | Pile printing numbers Laws 48/49 and 54, not the official 48A/48B and 53; processed text invents bail lengths 4 3/4 in/3/4 in (true 4 in/1/2 in). |
| 1890 | Pocket reprint with its own errors; all 1890->1892 differences are noise. |
| 1900 | Wright & Co. pamphlet that paraphrases/misprints the official text and omits Law 33B and the 1900 declaration Law, so serials 112, 114 and 115 first show in 1902. Also invents "middle stump" and "All runs". |
| 1923/1932 | Instruction sections (Notice to Umpires, The Batsman, The Bowlers, Signalling) are not segmented into Laws, so most "new" 1939 notes are really moves. |

**Unsegmented instruction sections.** The 'Instructions to Umpires' / 'Notice to Umpires' / 'The Batsman' / 'The Bowlers' / Signalling sections of the 1902-1932 books are never segmented or compared. Consequences found by the verifiers: the 1907 rule allowing a new ball after 200 runs (printed from 1908; Rait Kerr ch.4) and its 1913 and 1923 amendments never become events; most 'new' notes in 1932->1939 are really moves. Records 1908_1910_0033 and 1918_1920_0080 mention it but belong to no event. Segmenting these sections is deferred (user decision, 2026-10-27).

## Known limitations of the tooling

1. `_numvals.py` was rewritten after the first verification (ASCII fractions, decimals with "in.", numbers after Law references, Unicode
   fraction slash, super/subscript fractions); it is a heuristic and an unusual notation can still be misread.
2. A changed Law/clause number inside a cross-reference is class `xref_change` and counts as a change in every pair except 2010-2017, where the whole Code was renumbered; list labels such as (b) or (iv) are ignored as layout. The `substantive` flag and event type are heuristics (token-level classifier `_textclass.py`); events can mix a real change with
   segmentation noise (e.g. 2017_2019 E057, which holds both the Law 41.16 rewrite and Law 41.15 segmentation). The label then describes
   the substantive part and says so in `notes`.
3. Segmentation before 1884 is by headings (pseudo-Laws), so early Law lineage is weak; 1752 is a single block. Where OCR damages a Law
   number (1900 declaration Law printed "1.-" after Law 53) Laws can merge.
4. Law identity uses content similarity with title/number agreement and a fixed threshold; borderline Laws can be mismatched.
5. Hand labels are resolved to events by overlap of the change records they were written for (`labels/keys.json`), with an event-digest
   fallback. When the pipeline later merges two labelled events both labels are kept in one row (`notes` says so); a label whose event no
   longer exists is reported by `08_build_labels.py` and not written.
6. Labels are unreviewed (`review_status = unreviewed`). About 30% of post-1947 events are UNCATEGORISED because no source states a cause.
   `basis = stated` is used only when a source states the cause of that specific change; the MCC prefaces state the aim of a whole
   revision, so consolidation/restructure labels carry `basis = inferred`.
7. 1744-1947 diff records are now labelled (labels/q*.py, written by Opus agents against Rait Kerr and ACS transcriptions) but unreviewed; Rait Kerr's own 138 entries also have drafts in `data/categories/raitkerr_drafts.csv`.
8. Evidence quality varies; see `data/evidence/sources.csv` (S22 and S06 are secondary press; S13 is Wikipedia; S20 and S21 returned HTTP 403
   and are unverified).
