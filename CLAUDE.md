# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Data, scripts and figures for the manuscript *"Three Centuries of the Laws of
Cricket Reveal Core Principles of the Evolution of Regulatory Mechanisms"*
(Chia, Youn, Singer, Jeong, Kempes, Ogbunugafor, West, Holehouse). It is the
longest continuous machine-readable rule-set dataset known: all 44 editions of
the Laws of Cricket, 1752-2019 (268 years; MCC has been the governing body for
the last ~239 years). The paper is now in PNAS format.

**Source documents (newest first):**
- `evolution_of_cricket_rules_PNAS_SI-3.pdf` - current Supporting Information (read; summarised below).
- `cricket_PNAS_format-6.pdf` - current main PNAS paper. **Currently 0 bytes (failed copy) - not yet read; re-copy it, then re-read and update this file.**
- `manuscript-old.pdf` - the earlier arXiv-style manuscript (formerly `manuscript.pdf`, git shows that path deleted). The "Key findings" below came from it; the PNAS version may differ in numbers and figure numbering.

This is a personal fork (`origin` = `jamesholehouse/james-v-cricket-rule-evolution`);
the original is `upstream` (`ZaniuSchiaaa/cricket-rule-evolution`).

## Key findings (manuscript)

1. Rule books grow exponentially in time but as a **sublinear power law in
   cumulative matches played** (words ~ matches^0.4; unique words ~ ^0.5, i.e.
   Heaps' law; leaves ^0.41, nodes ^0.45). Rule addition per match decelerates.
   Matches data only exists from 1877, so time is used as the x-variable before then.
2. Zipf-Mandelbrot fits to word rank-frequency are good (R2 > 0.96) every year,
   but the exponent varies 0.7-0.9 over time (punctuated evolution).
3. Rule trees get deeper (higher average depth = "thinner", more specific
   rules); **phase transitions** appear in tree structure (e.g. average
   branching factor around 1939); number of Laws stays nearly constant.
4. Interdependency networks (cross-references between Laws, weighted and
   directed): in-/out-weight distributions are mostly power law, sometimes
   power law with exponential cutoff (Poisson fits worst); Gini of in-strength
   falls, while reciprocity, clustering and modularity (normalised against
   random baselines) rise - emerging community structure. Most
   eigenvector-central Laws shift from gameplay toward officiating/governance.

## Data provenance (from the SI)

- Books scanned at the MCC library at Lord's (CZUR ET18 Pro scanner, Sept 2024), OCR'd, then cleaned with the Gemini API (prompt: fix typos/spacing/punctuation only, no added/removed content). Gemini fixed OCR letter distortions and page decorations read as characters.
- Where several publications existed for one year, a primary source (not a compilation) that fits chronologically was chosen. Non-gameplay segments (ball/wicket dimensions, country-specific laws, county qualification rules) were dropped by heuristics documented in `data/datasets/rule_texts/data_appendix.xlsx`. Missing pages were imputed from neighbouring editions.
- Match counts exist only for 1877-2019: 28 of 44 rule sets. Cumulative matches is exponential in time, so the two x-variables are near-interchangeable there. Matches are preferred (hypothesised driver of rule change); time is used where pre-1877 data matters. Both versions are in SI Figs. S12-S13 (words R2 0.935 vs. matches / 0.948 vs. time; unique words 0.837 / 0.942; nodes 0.918 / 0.911; leaves 0.890 / 0.910).
- Citation extraction is regex-based (generative AI attempts failed); spot-check accuracy ~90-95%.
- Original vs. flattened trees: numbering each paragraph added an extra depth level, causing a spurious jump in average depth around 1828, so flattened trees (paragraph at same depth as its enumeration) are used as a proxy for rule specificity.
- Tree extraction needed a different regex algorithm per numbering scheme (e.g. 1980 uses `8(a)(i)`, 2019 uses `19.1.1.7`); trees were checked against the original PDFs via anytree html visualisations and radial network layouts (kamada-kawai, twopi).
- Network fits: in/out-degree and in/out-weight distributions fit with Poisson, power law, and power law with exponential cutoff on strictly positive values only (zero-degree nodes excluded), each normalised over the observed support, chosen by AIC. SI Fig. S5: clustering-coefficient distributions favour a power law (Vuong test) from 2000-2019, suggesting more hierarchical organisation.
- Eigenvector centrality is edge-weighted. Law numbers/names drift over time (e.g. "Caught" is Law 22 in 1896, 35 in 1947, 32 in 1980, 33 in 2019; "The Fieldsman" became "The Fielder"; "Handled the ball" merged into "Obstructing the field"), so Law labels and the four Law categories were assigned by hand from the PDFs. Case studies: "Caught" (declines after 1923), "Fair/Unfair Play" (from 1939, consistently top), "The Fieldsman" (dips 1902-1947, later top).
- SI Fig. S14 compares US Code size scaling against US population (data: Jeong et al., Sci. Data 13:13, 2026) - a companion dataset by overlapping authors.

## Environment

Python 3.12.4. `requirements.txt` is a pip-compile lock file (spacy, nltk,
networkx, powerlaw, pandas, matplotlib, graphviz, pyyaml, anytree, tqdm).

```bash
python -m pip install -r requirements.txt
python -m nltk.downloader punkt_tab stopwords   # extra data, not in requirements
dot -V                                          # Graphviz system binary needed for some viz scripts
```

There is no test suite, build system or package - every `.py` file is a
standalone script. **All scripts must be run from the repo root** with paths
relative to it (e.g. `python figures/main_body/fig7/source/fig7.py`); each
script's docstring states its inputs, outputs and usage.

## Layout

- `data/datasets/`
  - `rule_texts/raw|processed/<year>_*.txt` - OCR'd then text-corrected rule books; `data_appendix.xlsx` documents them.
  - `rule_set_structure/yaml_files/{original,flattened}/<year>_*.yaml` - rule trees (Law > nested clauses > leaf paragraphs), editions 1752-2019. **Only `flattened` is used for analysis** (flattening merges an enumeration node with leaf-only children, e.g. `3.1` + `P1` -> `3.1 P1`). Hand-corrected after automatic extraction, so they differ slightly from script output.
  - `rule_set_structure/source/2017_to_2019_extract_rule_set_structure.py` - regex-based tree extractor for the 2017-2019 enumeration style only (other eras use different enumeration, so no generic extractor); outputs `*-raw` yaml; `IS_FLATTENED` flag.
  - `interdependency_networks/citation_tables/` - per-year CSV of every rule's cited Laws (1823-2019, 33 editions), made by `source/extract_citations.py` (spaCy + regex) from `source/enumerated_text/`.
  - `interdependency_networks/graph_files/gexf/{multi_count,single_count}/` - Law-level directed weighted networks (1835 onward) built by `source/extract_interdependency_network.py`. `multi_count` increments edge weight per citation instance, `single_count` once per citing-Law/cited-Law pair. **All manuscript analysis uses `multi_count`.**
  - `num_matches/cumulative_matches_played.csv` - cumulative men's matches by year, from 1877 (ESPNCricinfo).
- `data/visualizations/` - tree layouts (html), network layouts (png/svg) of rule books, and Gephi interdependency-network renderings for 1918/1962/2019.
- `figures/main_body/figN/` and `figures/supplemental/figSN/` - each has `*_final.{svg,pdf}` (assembled figure), optional `components/` (panels) and `source/` (script producing each panel). `fig7/fit_parameters.csv` holds per-year power-law/Poisson/cutoff fit parameters (best chosen by AIC). Fig 1 timeline, Fig 3 tree nomenclature, Fig 4 timeline, Fig 10 pipeline flowchart and Fig 11 case studies are partly hand-assembled.
- `manuscript.pdf` - the paper (41 MB; large binary, avoid re-reading casually).
- `the_laws_of_cricket_rait_kerr_1950/` - untracked folder of ~160 scanned page images (jpg) of the 1950 Rait Kerr book; not part of the published repo layout.

Repo is ~240 MB (data 143 MB, figures 99 MB); don't grep or cat across `data/` or
`figures/` blindly.

## Gotchas

- README's tree labels `fig3` twice (text-analysis summary folder is actually `fig2`); trust the files on disk.
- Editions covered differ by dataset: structure yamls and texts 1752-2019 (44 editions), citation tables from 1823 (33), graph files from 1835, match counts from 1877.
- Citations may reference Laws by number, appendix or worded title ("One Day Matches", "Single Wicket", "Notes for Scorers and Umpires"); the extractor handles each.
- Network statistics are normalised against random baselines; error bars for reciprocity/modularity are wide in early years, so conclusions there are weak.

## rule_changes/: edition-to-edition change dataset (work in progress)

Goal: for every pair of consecutive editions, find what was added/removed/modified/moved (and at what level), classify why, cite
evidence, and later have a human verify it. See `rule_changes/README.md` (status table), `rule_changes/DATA_INTEGRITY_FINDINGS.md`
and the approved plan `~/.claude/plans/cozy-puzzling-token.md`. Use `.venv/bin/python` (venv at repo root, gitignored); scripts run from
the repo root; `rule_changes/scripts/run_pipeline.sh` rebuilds everything downstream of the processed texts.

- Pipeline: `01*` segment -> `02` diff -> `04` Law identity -> `06` events -> `07/08a/08b/08c` mechanical checks -> `08_build_labels.py`.
- Gold: `data/gold/raitkerr_chronology.csv` (Rait Kerr 1950 ch. 6, transcribed from page images; 138 serials, includes handwritten
  annotations of the scanned copy as separate columns).
- Labels: hand-written in `rule_changes/labels/p<pair>.py` (first pass) and `n<pair>.py` and nb/nc/nd/ne<pair>.py and q<pair>.py (pre-1947) (authored against later pipeline runs; key prefixes `n:`, `nb:`, `nc:`, `nd:`, `ne:`, `q:`), plus `labels/overrides.json` (verification corrections keyed by event id + content signature); the builder
  resolves each label to the event holding most of the change records it was written for (`labels/keys.json`; n-labels are keyed
  `pair:n:Exxx`), so pipeline fixes that shift event ids do not orphan labels. "No claim without evidence" is enforced by the builder
  (every label needs a rationale and registered source ids; UNCATEGORISED must have basis `none`; NOT_A_CHANGE basis `derived`). Use
  `basis = stated` only when a source states the cause of that specific change; prefaces that state the aim of a whole revision give `inferred`.
  A "restructure" label must not hide a policy change: add the real change and a secondary UNCATEGORISED.
- **The AI clean-up of the digitised texts can invent numbers** where OCR was illegible (ball/bat/bail sizes in 1947-1968, 2000, 2010,
  2017, 2019). Do not trust a numeric "change" without checking raw OCR and an independent transcription (ACS 1947/1980 codes, MCC 2010
  text). The ACS transcriptions and MCC change documents are saved under `rule_changes/data/evidence/`.
- Dataset edition labels are not exact printing dates; some rule changes appear one edition late. The "1952" text is a genuine 2nd-edition
  printing (the 1954 amendments first appear in 1962); ACS pages show amended text with originals inset, so they do not confirm a dated wording alone.
- Opus verification reports A-E are in `rule_changes/verification/`; their findings were applied (see `rule_changes/CONTINUATION.md`).
- Nothing in this sub-project is committed yet; labels are unreviewed.
