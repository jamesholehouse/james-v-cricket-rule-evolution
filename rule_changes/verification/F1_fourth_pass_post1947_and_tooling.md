# Verification F1: fourth pass (post-1947 labels, round-4 classifier, builder, datasets)

This review was read-only. The only project file written is this report. All scripts ran on a copy in a scratch directory
(`run_pipeline.sh`, `08_build_labels.py`, `09_build_datasets.py`). The copy reproduces `data/changes`, `data/events`, `data/categories`,
`data/final` and `labels/keys.json` **byte for byte**. Gold recall is 11/11. Event ids below are current ids. Labels from earlier
reports are traced by `label_ref`.

## Verdict summary

| Scope | Result |
|---|---|
| E items (NOT FIXED / PARTLY / new errors), 47 checked | 23 FIXED, 8 PARTLY, 16 NOT FIXED (13 of the 16 are LOW) |
| Datasets: mechanical integrity | Clean. All 7,262 records appear exactly once. Every event-level row equals its `event_labels_all` row (category, subtype, basis and all 4 flags). Every record-level mechanical label equals the classifier class. `substantive_changes.csv` = exactly the 742 rows with `substantive_change=1`. The flag formula holds for all 1,506 rows. All 150 consolidation_merge rows are included. |
| Taxonomy v0.2 | Clean. 0 invalid category/subtype/secondary values. UNCATEGORISED always has basis `none`, NOT_A_CHANGE always `derived`, and every evidence id is among the 66 in `sources.csv`. There are no blank primary subtypes, no duplicate sigs, and no `?` in `label_ref`. |
| Classifier on real data | 0 false negatives among all 52 `ocr_noise` records. 0 real changes among all 59 `format_only` records whose words differ (502 post-1947). All 214 post-1947 `minor_wording` records were scanned and 1 small hidden change was found. Several latent blind spots remain (section 2). |
| New problems | 1 HIGH, 4 MEDIUM, 9 LOW |

The most serious problems:

1. **HIGH: the merge step plus `is_semantic()` drops real changes from `substantive_changes.csv`.**
   - When two labels merge, `real()` treats a gender-neutral or terminology label as "real". The tie is then broken by record overlap, so a semantic label can become the primary.
   - `is_semantic()` looks only at the primary, so the whole event gets `substantive_change=0`.
   - **2010_2017_E038** (ref `n2010_2017:E038+p2010_2017:E035`) is EXTERNAL_FORCE/legal_social with gender-neutral wording, so `substantive_change=0`. Yet its records include:
     - removal of the automatic dead ball "it lodges in a protective helmet worn by a fielder" (0753). The 2010 text l.1772 has it and the 2017 text has no counterpart; this is the 2017 helmet change.
     - the new "match is concluded" dead ball (0882);
     - "a serious injury" -> "a **possibly** serious injury" (0318), which is not described anywhere.
   - **2010_2017_E039** is STRUCTURAL/terminology, so `substantive_change=0`. It absorbs the stated MCC 2013 clarification (bowler not releasing the ball = Dead ball). Because both labels are STRUCTURAL, no secondary category is kept.
2. **MEDIUM: digest-fallback resolution attaches labels to the wrong events.**
   - `fuzz.token_set_ratio` scores 100 whenever one digest's tokens are a subset of the other's. A 1-record event can therefore "match" an 8- or 12-record label.
   - 23 labels resolve through the fallback, all at score 100. 10 of them have very different record counts.
   - Confirmed wrong:
     - **2010_2017_E047** (`p2010_2017:E022`, 8 records -> 1-record event 0751 "(Umpire calling and signalling Dead ball)" removed). It still claims "Law 17 ... 'Law 23.4(b)' becomes 'Law 20.4.2.6'; 'deception' added to the distraction clause".
     - The merged part of **2010_2017_E039** (`p2010_2017:E036`, 12 records -> 3). It describes the bowler-not-releasing clause, which is record 0322 in **2010_2017_E040**.
3. **MEDIUM: the merge loses the second label's category.**
   - `merge_labels` adds b's category as secondary only if a has no secondary and the categories differ.
   - **2017_2019_E036** now holds MCC 2019 items #7 (21.6) and #8 (21.12). The stated ENJOYMENT/fairness_spirit cause for 21.12 ("It was felt that this was unfair") survives only as text. The primary is STRUCTURAL/consequential and the secondary is EXTERNAL_FORCE with an empty subtype, inherited from 21.6.
   - **2017_2019_E057** merges the 2017 "m"-for-"in" ball artefact (`p:E049`, cleaning_artefact_numeric, suspect) under `nd:E054` (format_artefact, `integrity=ok`).
4. **MEDIUM: 2008-2010 "NZC modernised" wording_only labels still hide rule changes.** All of these rows are `semantic_only=1`, so they are excluded from dataset 2. Section 4 has the table.

---

## 1. Third-pass (E) items

| E item | Current row (label_ref) | Verdict | Evidence |
|---|---|---|---|
| HIGH 2010_2017_E095 fake fielding etc. | 2010_2017_E095 (p:E088) | FIXED | what_changed now names the cloth approval, "unfairly changed", the replacement-ball choice, "in the match by that team", first-instance 5 Penalty runs, "shall not count as one of the over" and "distract, deceive or obstruct". UNCATEGORISED. |
| MED 2010_2017_E047 "deception added" on a pointer removal | 2010_2017_E047 (p:E022) | NOT FIXED | Unchanged text. The cause is the digest fallback (summary #2). |
| MED 2017_2019_E022 may->must probably invented | 2017_2019_E022 (n:E021) | FIXED | SEMANTIC_WORDING/modal_strength, `integrity=suspect`, rationale cites raw OCR "rr"/"ma>", `substantive_change=0`. |
| 2010_2017_0589 "deliberate or avoidable" | in 2010_2017_E096 (merged, UNCATEGORISED) | FIXED | Named in what_changed. The text attributes it to the batsman paragraph, but 0589 is the general clause (minor). |
| 2010_2017_0318 "possibly serious injury" | in 2010_2017_E038 | NOT FIXED | Not named, and the event has `substantive_change=0` (summary #1). |
| 2010_2017_0537 caution "to that bowler" | in 2010_2017_E096 | PARTLY | In a substantive event, but not named. |
| 2008_2010_0344 "strikes or pulls a stump" | in 2008_2010_E061 | PARTLY | In an UNCATEGORISED event, but not named. |
| 2008_2010_0213 batsmen no longer informed | in 2008_2010_E029 (Law 18) | PARTLY | In an UNCATEGORISED event; the removal of "inform the batsmen" is not named. |
| 2000_2008_0105 "fairly put down" | 2000_2008_E039 (ne) | FIXED | SEMANTIC_WORDING/qualifier_scope, scope_change=1, counted substantive. |
| 2008_2010_0320 "with his bat" dropped | in 2008_2010_E055 | PARTLY | In the UNCATEGORISED wide-test event, but not named. |
| Classifier: wide->wider | | PARTLY | Now `minor_wording`, not `ocr_noise` (inflection rule works), but still hidden. |
| Classifier: striker->non-striker, retires hurt->retires, given out->in | | FIXED | All `substantive` (tested). |
| Classifier: "(a) above"->"(b) above", "2(a)"->"2(b)", "(a),(b),(c)"->"(a),(c)" | | NOT FIXED | minor_wording / minor_wording / format_only. Real-data cases (2000_2008_0051, 2008_2010_0240/0243/0068) are still format_only. They are consequential (LOW). |
| Classifier: Law-reference titles stripped ("Law 33 (Handled the ball)"->"Law 34 (Hit the ball twice)") | | NOT FIXED (by design) | xref_change. On real data the 59 word-differing format_only records are all title-only (e.g. 2010_2017_0375 "(Runs scored ...)"->"(Runs permitted ...)"; 2017_2019_0240 adds "(Substitute fielders)"). None is a rule change. |
| 'm' unit artefact orphaned (p2017_2019:E048/E049) | E056 (p:E048), E057 (nd:E054+p:E049) | FIXED / PARTLY | E048 is again NOT_A_CHANGE/cleaning_artefact_numeric, suspect. E049's subtype and `suspect` flag are lost in the merge (summary #3). |
| Dead code `and False` (`_textclass.py` l.111) | | NOT FIXED (LOW) | Still present. |
| 1952_1962 E015/E016 duplicate description | E015 (p:E011), E016 (n:E013) | NOT FIXED (LOW) | Both still describe "The captain shall take the bowler off as directed". |
| 2008_2010 merged rows with "leaves the rule as it was" | E029, E057, E070, E075 | PARTLY | The contradictory rationale text is gone (only the real label's rationale is kept). The secondary is still STRUCTURAL/wording_only on all four. |
| 2010_2017_E004 ENJOYMENT secondary with basis none | 2010_2017_E005 (p:E004) | NOT FIXED (LOW) | Secondary ENJOYMENT/fairness_spirit unchanged. |
| 2010_2017_E111 removal filed as reorganisation | 2010_2017_E110 (p:E104) | PARTLY (LOW) | Text says "a removal", but the category is still STRUCTURAL/reorganisation. |
| Wide test "normal guard position" | 2008_2010_E055 (n:E058) | FIXED | UNCATEGORISED; "may change how a borderline wide is judged". |
| "without appeal" | 2008_2010_E090 (n:E095) | NOT FIXED (LOW) | Still wording_only; record 0459. |
| "at the end of the match" | 2008_2010_E045 (n:E046) | NOT FIXED (LOW) | Still wording_only; record 0254. |
| 2008_2010_0424 "and 42.17(b)" | 2008_2010_E082 (p:E083) | NOT FIXED | Also hides a real change (section 4). |
| 5 preface-`stated` rows | 2010_2017_E014, E041, E103, E107, E108 | FIXED | All `inferred`. |
| E091 quotes S03 without citing it | 2010_2017_E091 | FIXED | evidence = S17;S01;S02;S03. |
| E102 "need both" as MCC quote | | FIXED | The phrase no longer appears in any label. |
| DATA_INTEGRITY intro ("recorded as cleaning_artefact_numeric labels") | | NOT FIXED (LOW) | Unchanged. It is false for the 2010 ball (2010_2017_E091 is UNCATEGORISED with a secondary) and the 2017 junior/women's "m" (format_artefact via the merge). |
| Stale "see E0xx": 1947_1952_E023, 2010_2017_E002 | | FIXED | Now worded by content. Other stale ids remain (section 5). |
| nc1947_1952 E028 (Law 27/25) | 1947_1952_E028 | FIXED | NOT_A_CHANGE/cleaning_artefact_numeric, suspect, cites acs_1947 l.866. |
| nc1947_1952 E035 | 1947_1952_E035 | FIXED | Now segmentation_artefact; "still present in 1952". |
| nd2010_2017 E040 "new" lost-ball item | 2010_2017_E040 | FIXED | "former Lost-ball provision folded in". |
| E082 Hit wicket No ball "new in 2017" | 2010_2017_E082 (p:E075) | FIXED | "the 2010 Law 24 already allowed dismissal off a No ball only under Laws 33, 34, 37 and 38". |
| 2010_2017_E002 Type D bat under reorganisation/stated | 2010_2017_E003 (p:E002) | FIXED | Basis `inferred`, secondary UNCATEGORISED, no stale id. |
| 2000_2008_E020 wrong primary | 2000_2008_E020 | FIXED | UNCATEGORISED. |
| 2010_2017_E039 stated clarification absorbed | 2010_2017_E039 | NOT FIXED, worse | Now also excluded from dataset 2, and the absorbed text belongs to E040 (summary #1, #2). |
| `?` in label_ref; self-referencing merge notice | builder l.112-116 | FIXED | 0 rows with `?`; notices read "X and Y: merged". |
| README l.19, CLAUDE.md l.113 stale | | FIXED | |
| 0176 described twice (E009/E010) | 2010_2017_E009, E010 | FIXED | E009 no longer claims the drinks change. |
| Random-sample minor issues: 1968_1980_E055; 1992_2000_E032, E052, E033; 2010_2017_E042 | same ids | NOT FIXED (LOW) | Unchanged: 30->45 minutes attendance, "unacceptable damage" covering and the Bowled exemption are not named; E042 is still NOVEL_EVENT primary for a bundle. |

## 2. Round-4 classifier (`scripts/_textclass.py`)

**Distribution of all 4,149 modify records:**

| Class | In an event | Outside events |
|---|---|---|
| format_only | 4 | 858 |
| minor_wording | 1 | 353 (214 post-1947) |
| ocr_noise | 0 | 52 |
| numbering_only | 25 | 0 |
| xref_change | 43 | 81 (all 2010_2017) |
| substantive | 2,456 | 0 |

**ocr_noise (all 52 inspected): 0 false negatives.**
- Pairs include docs/does, pased, froi, becaus, sinker/striker (1902_1906_0012), wides/widen (1918_1920_0021), complete/complex (1980_1992_0028), repeal/repeat and offending/offend (2017_2019_0088).
- Each one is an OCR slip in its context.
- The inflection rule works ("wider" is no longer noise). It is asymmetric: a rare truncated form ("offend") is still treated as noise, which is correct here.

**format_only.** I checked all 59 post-1947 format_only records whose raw words differ:
- unit spacing ("12m"/"12 m");
- fraction notation (1952_1962_0002 "5 ½" vs "5.5");
- Law-reference titles;
- list letters.

None is a rule change. 2000_2008_0017 and 1980_1992_0006 etc. are equal values in different notation.

**minor_wording (all 214 post-1947, plus spot checks pre-1947).**
- Almost everything is OCR noise, articles, plurals, gender pronouns or tense.
- One small hidden change: 2010_2017_0515 "the supervision of **the** umpire" -> "**an** umpire" (LOW).
- The singular/plural umpire flips (2000_2008_0014 "the umpires shall wait" -> "the umpire"; 2008_2010_0062) are minor_wording. They could matter, but were not verified against the texts.

**Adversarial tests:**

| Input | Class | Note |
|---|---|---|
| "A **and** B" -> "A **or** B" | minor_wording | and/or are STOP words, so the swap test skips them |
| "1/2 in. **above** the stumps" -> "**below**" | minor_wording | above/below were **added to STOP in round 4**; this widens the blind spot |
| "run **from** the wicket" -> "**to**"; "**at**" -> "**in**" | minor_wording | |
| "the umpire" -> "the umpires" | minor_wording | |
| "5.5 m" -> "5.5 in" | minor_wording | Real 2017 cases have 2 unit tokens and come out substantive |
| "he" -> "she" | minor_wording | Intended |
| "(a) above" -> "(m) above" | minor_wording | |
| leg/off, before/after, front/behind, first/second, six/eight, within/without, fair/unfair, Caught/Bowled, Dead ball/No ball, field/outfield, wicket/crease, non-striker variants, deleted "wilfully" | substantive | Correct |

On real data the only STOP-word swaps hidden as minor_wording are 2008_2010_0029 "at/on the resumption" and 2008_2010_0402 "(iii) or (iv)" -> "(iii) and (iv)". Both are harmless. The **indel threshold of 1** (one inserted or deleted content word = substantive) is what moved E's seven hidden records into events. I found no false positive from it among the labelled events I read.

**Other.**
- The list-label filter drops b-h and roman numerals ii-x but keeps 'a', 'i' and 'm'. So "(a)" -> "(b)" is minor_wording while "(b)" -> "(c)" is format_only. This is inconsistent but harmless on real data.
- The `toks()` comment is now accurate.

## 3. Builder (`scripts/08_build_labels.py`)

| # | Severity | Problem | Evidence |
|---|---|---|---|
| B1 | HIGH | `real()` (l.142) ranks only NOT_A_CHANGE / wording_only as non-real. A SEMANTIC_WORDING, terminology or gender-neutral label can win the merge. `is_semantic()` reads the primary only, so `substantive_change=0` for an event that holds a real change. | 2010_2017_E038, E039 (summary #1). |
| B2 | MEDIUM | `merge_labels` (l.154) keeps b's category only when a has no secondary and the categories differ; b's secondary is always dropped; integrity is a's. | 2017_2019_E036 (ENJOYMENT stated for MCC #8 lost), 2017_2019_E057 (cleaning artefact + suspect lost), 2010_2017_E039. |
| B3 | MEDIUM | The digest fallback (l.94-104) uses `token_set_ratio`, which gives 100 for any token subset. The only gate is `law_to` or `law_from` equality, with no record-count check. All 23 fallback resolutions scored exactly 100 (bo = 0.70). Those with record-count mismatch, label -> event: 2010_2017:E022 8->1 (wrong), 2010_2017:E036 12->3 (wrong), 2010_2017:E092 7->2, 2017_2019:E001 7->3, 2008_2010:E082 3->7, 2000_2008:E021 1->5, plus four 3->1 cases. I checked the last six against the records and they are plausible. | Instrumented copy of `resolve()`. |
| B4 | LOW | `is_semantic()` ignores the secondary category. A semantic primary with a real secondary (2010_2017_E002: new off side/on side/in front of/behind definitions as secondary codification) is excluded from dataset 2. So are rows whose real part is only in text. | |
| B5 | LOW | `EDITION_RE` matches words in rationales that are not about the dataset edition, so `source_edition_issue=1` is set wrongly. | 1830_1835_E027 ("earlier unofficial editions"), 1820_1823_E008/E009 ("unofficial c.1805 edition"), 1939_1947_E021/E042/E089 ("press reprint" of the evidence source). 122 rows are flagged, 0 of them post-1947. |
| B6 | LOW | Blank NOT_A_CHANGE subtype -> edition_artefact (l.162). All 45 blanks are in q modules and mostly are edition issues. 1828_1830_E010 and E054 are described as "Mis-paired" segmentation, which is segmentation_artefact. 0 labels set edition_artefact explicitly, so the subtype exists only through this normalisation. | |
| B7 | LOW | Docstring still says "Assemble the post-1947 event labels". | |

**Key spaces.**
- `p` -> `pair:Exxx`. Files n/nb/nc/nd/ne/q -> `pair:<prefix>:Exxx` via `[nq][a-z]?`.
- No collisions. Duplicate check is per file. No pair has more than 999 events, so `event_id[-4:]` is safe.
- 13 orphaned labels, all in E's list. 2017_2019:E048/E049 and nb:E028/E030 now resolve. No new orphan; none drops a real change.
- Nothing is silently dropped: the builder prints every orphan, and `unlabelled_events.csv` is empty.

## 4. Datasets (`09_build_datasets.py`, `data/final/*.csv`)

Every row of both files was checked by program rather than sampling 40 (see the summary). Record-level mechanical rows:
- 858 format_artefact and 244 renumber;
- 353 wording_only (`semantic_only=1`);
- 81 xref and 35 pure "(See ...)" add/remove (consequential);
- 52 ocr_noise.

0 rows need a hand label. Definitions in the 09 docstring and in the builder agree.

The datasets are only as good as the labels. These semantic_only (excluded) post-1947 rows hide real or arguable changes:

| Row (ref) | Label | Hidden change (quoted) |
|---|---|---|
| 2010_2017_E038 | EXTERNAL_FORCE/legal_social | Removal of dead ball "it lodges in a protective helmet worn by a fielder" (0753); "the match is concluded ..." dead ball (0882); "a possibly serious injury" (0318). **HIGH** |
| 2010_2017_E039 | STRUCTURAL/terminology | Merged MCC 2013 clarification (its records are in E040). MEDIUM |
| 2008_2010_E080 (p:E081) | wording_only, "opposing side -> fielding side" | New "This shall apply whether or not there is any disadvantage to the fielding side" (0809; absent in 2008, present in 2010 l.2560); "while the ball is in play" added; returning-the-ball clause adds "other than a hand not holding the bat". MEDIUM |
| 2008_2010_E082 (p:E083) | wording_only, "No ball provision restated" | Run out: "the run in progress when the wicket is put down shall not be scored, but runs completed by the batsmen shall stand" (0422); runner case "before the wicket is put down" and penalties stand (0423); "and 42.17(b)" dropped (0424). MEDIUM |
| 2008_2010_E043 (p:E045) | wording_only, "cross-reference added" | "Umpires awarding a match Notwithstanding any agreement under Law 12.1(b) (Number of innings)" added (0776/0777); "A forfeited innings is to count as a completed innings" removed (0653). LOW-MED |
| 2008_2010_E072 (n:E076) | wording_only | Law 18.12 applies "from the instant of the completion of the catch" (was "of the catch"); "over" -> "beyond the boundary". LOW |
| 2008_2010_E090, E045 | wording_only | "without appeal"; "at the end of the match" (E items). LOW |
| 2010_2017_E002 (p:E001) | EXTERNAL_FORCE/legal_social | New Appendix A.13 definitions (off side/on side; in front of/behind the popping crease). LOW |
| 2010_2017_E036 (p:E033) | EXTERNAL_FORCE/legal_social | "The umpires shall consult with each other whenever necessary" removed. "Disagreement and dispute ... the umpires together shall make the final decision" added; 2010 had "All disputes shall be determined by the umpires" (l.360). LOW |
| 1947_1952_E032 | STRUCTURAL/terminology | "other grades of English Cricket" -> "Cricket in the United Kingdom" widens geographic scope. LOW |

## 5. Post-1947 round-4 rows

- **SEMANTIC_WORDING post-1947 (5 rows): all correct.**

  | Row | Label |
  |---|---|
  | 2000_2008_E039 | qualifier_scope, "fairly" |
  | 2008_2010_E013 | clarifying_rewrite, "required" dropped |
  | 2008_2010_E017 | modal_strength, will->shall |
  | 2008_2010_E041 | qualifier_scope, "may only resume" -> "may resume ... only" |
  | 2017_2019_E022 | modal_strength, suspect |

- **ne modules (8 labels): all correct.** 1947_1952_E022, 1962_1968_E009/E010/E018, 2010_2017_E001 and the three above.
- **May/must:**
  - Every post-1947 modal swap (may/must/should/shall/can, excluding shall/will and must/shall) sits in a substantive event.
  - The exceptions are 2008_2010_E007 ("must not exceed" -> "may not exceed", equivalent; label wording_only, suspect) and 2017_2019_E022.
- **Wide test:** 2008_2010_E055 is FIXED.
- **E095-type events:** E095 is fixed. The same under-description pattern persists in the large merged rows and in the 2008_2010 NZC wording_only rows (section 4).
- **MCC 2019 list:** all 22 items still have rows. #7 and #8 now share 2017_2019_E036, which loses #8's stated category (B2). #16 is E058/E064, #17 E062/E063, #18 E066.
- **Stale event-id cross-references (LOW; LABELLING_GUIDE forbids ids):**

  | Row | Reference | Actually is |
  |---|---|---|
  | 1952_1962_E018 | "compare E013" | E013 is the LBW 'hand' Note |
  | 2010_2017_E060 | "E072" | batsman's bat bouncing |
  | 2010_2017_E090 | "Counterpart of E060" | Law 28 fielder |
  | 2017_2019_E047 | "Counterpart of E038" | 'extratakes' OCR |

  1980_1992_E015, 2000_2008_E053 and 2008_2010_E091 point correctly.

## 6. Taxonomy and document counts

- Taxonomy v0.2 is consistent (see the summary). `taxonomy_version=v0.2` is on all 1,506 rows. The secondary subtype is blank for 2 EXTERNAL_FORCE rows and 1 NOT_A_CHANGE row (valid but uninformative).
- Counts:

  | Count | Value | Matches docs? |
  |---|---|---|
  | Events | 1,506 | yes |
  | Records | 7,262 | yes |
  | Substantive events | 742 | yes |
  | Sources | 66 | yes |
  | Unlabelled | 0 | yes |
  | Post-1947 UNCATEGORISED | 30.1% | yes ("about 30%") |
  | Pre-1947 events | 948 | **no**: README l.17 and CONTINUATION l.75 say "all 913 pre-1947 diff events"; 913 are q hand labels plus 35 mechanical. LOW |
  | Post-1947 events | 558 (385 p, 148 n*, 25 mechanical) | |

- CLAUDE.md "Labels" paragraph lists key prefixes `n:`, `nb:`, `nc:`, `nd:` only; `ne` and `q` modules exist (LOW).
- The README table row headed "post-1947" now describes all pairs (cosmetic).

## Not verified

- Pre-1947 q labels: these were out of scope apart from builder and flag effects.
- Web-only sources.
- Whether the 2017 helmet dead-ball removal (0753) is described in another event. It is still excluded in E038.
- The full text of every record in the large rewrite events: I read up to about 20 records per event.
- The umpire/umpires singular-plural flips against page images.
