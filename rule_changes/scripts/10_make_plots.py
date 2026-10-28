"""
10_make_plots.py  -  figures of rule change through time (rule_changes/figures/*.png).

Uses system python3 (matplotlib/pandas):   python3 rule_changes/scripts/10_make_plots.py
Inputs: data/categories/event_labels_all.csv, data/final/*.csv, data/nodes/, data/gold/raitkerr_chronology.csv.
Substantive = substantive_changes.csv (752 events + 244 Law-level RENUMBERING rows). Editions are irregular, so bars are one per
edition pair (x label = the later edition's year) and rates are per year of gap between the two editions.
"""
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

csv.field_size_limit(sys.maxsize)
ROOT = Path(__file__).resolve().parents[1]
D = ROOT / "data"
FIG = ROOT / "figures"
FIG.mkdir(exist_ok=True)

SURF, INK, INK2, MUTED, GRID, AXIS = "#fcfcfb", "#0b0b0b", "#52514e", "#898781", "#e1e0d9", "#c3c2b7"
BLUE, ORANGE, AQUA, YELLOW, MAGENTA, GREEN = "#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300"
plt.rcParams.update({"figure.facecolor": SURF, "axes.facecolor": SURF, "savefig.facecolor": SURF, "text.color": INK, "axes.labelcolor": INK2,
                     "xtick.color": MUTED, "ytick.color": MUTED, "axes.edgecolor": AXIS, "font.size": 10, "axes.spines.top": False,
                     "axes.spines.right": False, "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.6, "axes.axisbelow": True,
                     "legend.frameon": False, "font.family": "DejaVu Sans"})

GROUPS = [("STRUCTURAL", "Structural (clarify, codify, reorganise)", BLUE), ("UNCATEGORISED", "Rule change, no cause stated", ORANGE),
          ("CAUSAL", "Rule change with a stated cause", AQUA), ("RELOCATION", "Relocation (move, merge, split)", YELLOW),
          ("RENUMBERING", "Renumbering", MAGENTA), ("SEMANTIC_WORDING", "Wording that may alter enforcement", GREEN)]
CAUSAL = {"ENJOYMENT", "NOVEL_EVENT", "EXTERNAL_FORCE", "ECONOMY"}
grp = lambda c: "CAUSAL" if c in CAUSAL else c

labels = list(csv.DictReader(open(D / "categories/event_labels_all.csv", encoding="utf-8")))
sub = list(csv.DictReader(open(D / "final/substantive_changes.csv", encoding="utf-8")))
recs = list(csv.DictReader(open(D / "final/changes_all_records_labelled.csv", encoding="utf-8")))
yr = lambda p: tuple(int(x) for x in p.split("_"))
PAIRS = sorted({r["pair"] for r in labels}, key=lambda p: yr(p)[1])
X = np.arange(len(PAIRS))
TICK = [str(yr(p)[1]) for p in PAIRS]
GAP = {p: max(1, yr(p)[1] - yr(p)[0]) for p in PAIRS}
ERAS = [(1884, "1884 Code"), (1939, "1939 re-order"), (1947, "1947 Code"), (1980, "1980 Code"), (2000, "2000 Code"), (2017, "2017 Code")]


def style_pairs(ax, rot=90):
    ax.set_xticks(X)
    ax.set_xticklabels(TICK, rotation=rot, fontsize=7.5)
    ax.set_xlim(-0.7, len(X) - 0.3)
    ax.grid(axis="x", visible=False)


def era_marks(ax, ytop=None, head=1.32):
    """Dashed line + label per recodification; the label sits in headroom above the tallest bar."""
    lo, hi = ax.get_ylim()
    ax.set_ylim(lo, hi * head)
    for y, t in ERAS:
        for i, p in enumerate(PAIRS):
            if yr(p)[1] == y:
                ax.axvline(i, color=AXIS, lw=0.8, ls=(0, (3, 3)), zorder=0)
                ax.text(i - 0.25, 0.995, t, rotation=90, va="top", ha="right", fontsize=7.5, color=MUTED, transform=ax.get_xaxis_transform())


def stack(ax, series, colors, names, ylabel, width=0.78):
    bottom = np.zeros(len(PAIRS))
    for vals, c, n in zip(series, colors, names):
        v = np.array(vals, float)
        ax.bar(X, v, width, bottom=bottom, color=c, label=n, edgecolor=SURF, linewidth=0.8)
        bottom += v
    ax.set_ylabel(ylabel)
    return bottom


def save(fig, name):
    fig.savefig(FIG / name, dpi=170, bbox_inches="tight")
    plt.close(fig)
    print("wrote", name)


def label_tops(ax, tot, thr=1, fs=7):
    for i, t in enumerate(tot):
        if t >= thr:
            ax.text(i, t + max(tot) * 0.012, f"{int(t)}", ha="center", va="bottom", fontsize=fs, color=INK2)


# ---------- 1. rule change over time ----------
cnt = {g[0]: Counter() for g in GROUPS}
for r in sub:
    cnt[grp(r["category"])][r["pair"]] += 1
tot = np.array([sum(cnt[g][p] for g, _, _ in GROUPS) for p in PAIRS], float)
fig, (a, b) = plt.subplots(2, 1, figsize=(13, 9), gridspec_kw={"height_ratios": [3, 2]})
bt = stack(a, [[cnt[g][p] for p in PAIRS] for g, _, _ in GROUPS], [c for _, _, c in GROUPS], [n for _, n, _ in GROUPS], "Substantive changes per edition pair")
label_tops(a, bt)
style_pairs(a)
era_marks(a)
top = PAIRS[int(np.argmax(tot))]
a.set_title(f"Substantive change by edition pair: {int(tot.max())} in {top.replace('_', '→')}, the largest rewrite", loc="left", fontsize=13, fontweight="bold", pad=50)
a.legend(ncol=3, loc="lower left", fontsize=8.5, bbox_to_anchor=(0.0, 1.02))
a.text(0.0, -0.17, "Renumbering before 1884 mostly reflects the order of unnumbered headed blocks in the early editions, so treat the pink there as a re-ordering signal, not true renumbering.",
       transform=a.transAxes, fontsize=8, color=MUTED, ha="left")
rate = tot / np.array([GAP[p] for p in PAIRS])
yrs = [yr(p)[1] for p in PAIRS]
b.plot(yrs, rate, color=BLUE, lw=2, marker="o", ms=5, markeredgecolor=SURF)
b.set_ylabel("Changes per year of gap")
b.set_xlabel("Edition year")
b.set_title("The same counts per year between editions (gaps range from 1 to 19 years)", loc="left", fontsize=11, color=INK2)
for p in sorted(PAIRS, key=lambda p: -rate[PAIRS.index(p)])[:4]:
    i = PAIRS.index(p)
    b.annotate(p.replace("_", "→"), (yrs[i], rate[i]), textcoords="offset points", xytext=(6, 4), fontsize=8, color=INK2)
fig.tight_layout()
save(fig, "01_rule_change_over_time.png")

# ---------- 2/3. additions and subtractions ----------
reloc_ev = {r["event_id"] for r in labels if r["category"] == "RELOCATION" or r["secondary_category"] == "RELOCATION"}
sub_ev = {r["event_id"] for r in sub}
words = lambda t: len((t or "").split())


def add_remove_fig(op, textcol, name, title, noun, note):
    n_new, n_mov, w_new, w_mov = Counter(), Counter(), Counter(), Counter()
    for r in recs:
        if r["label_level"] != "event" or r["op"] != op or r["event_id"] not in sub_ev:
            continue
        moved = r["event_id"] in reloc_ev
        (n_mov if moved else n_new)[r["pair"]] += 1
        (w_mov if moved else w_new)[r["pair"]] += words(r[textcol])
    fig, (a, b) = plt.subplots(2, 1, figsize=(13, 8.5), sharex=True)
    for ax, new, mov, yl in ((a, n_new, n_mov, f"{noun} records"), (b, w_new, w_mov, "Words")):
        bt = stack(ax, [[new[p] for p in PAIRS], [mov[p] for p in PAIRS]], [BLUE, YELLOW],
                   ["In events that change a rule or its wording", "In relocation events (text moved, merged or split)"], yl)
        label_tops(ax, bt, thr=bt.max() * 0.12)
        style_pairs(ax)
    era_marks(a)
    a.legend(loc="upper left", fontsize=8.5, bbox_to_anchor=(0.0, 0.88))
    a.text(0.0, 1.02, note, transform=a.transAxes, fontsize=8, color=MUTED)
    a.set_title(title, loc="left", fontsize=13, fontweight="bold", pad=18)
    b.set_xlabel("Later edition of the pair")
    fig.tight_layout()
    save(fig, name)


tot_add = sum(1 for r in recs if r["label_level"] == "event" and r["op"] == "add" and r["event_id"] in sub_ev)
tot_rem = sum(1 for r in recs if r["label_level"] == "event" and r["op"] == "remove" and r["event_id"] in sub_ev)
add_remove_fig("add", "new_text", "02_additions.png", f"Additions: {tot_add} added passages in substantive events", "Added", "Raw counts: where a clause was reworded and the diff could not pair it with its old version, the new wording counts here (and the old wording under subtractions).")
add_remove_fig("remove", "old_text", "03_subtractions.png", f"Subtractions: {tot_rem} removed passages in substantive events", "Removed", "Raw counts: where a clause was reworded and the diff could not pair it with its new version, the old wording counts here (and the new wording under additions).")

# ---------- 4/5. mergers and splits ----------
for kind, fname, col in (("merge", "04_mergers.png", YELLOW), ("split", "05_splits.png", ORANGE)):
    prim, sec = Counter(), Counter()
    for r in labels:
        if r["category"] == "RELOCATION" and r["subtype"] == kind:
            prim[r["pair"]] += 1
        if r["secondary_category"] == "RELOCATION" and r["secondary_subtype"] == kind:
            sec[r["pair"]] += 1
    fig, ax = plt.subplots(figsize=(13, 4.8))
    bt = stack(ax, [[prim[p] for p in PAIRS], [sec[p] for p in PAIRS]], [col, BLUE],
               [f"Main change of the event is a {kind}", f"A {kind} alongside a rule change"], f"Events")
    label_tops(ax, bt)
    style_pairs(ax)
    era_marks(ax)
    ax.legend(loc="upper left", fontsize=9, bbox_to_anchor=(0.0, 0.88))
    n = int(bt.sum())
    ax.set_title(f"{'Mergers' if kind == 'merge' else 'Splits'}: {n} events, clustered at the big recodifications", loc="left", fontsize=13, fontweight="bold")
    ax.set_xlabel("Later edition of the pair")
    fig.tight_layout()
    save(fig, fname)

# ---------- 6. interesting events ----------
SHORT = {"1755_1774_E004": "Bets section", "1755_1774_E006": "Bat width limit", "1788_1803_E001": "New ball each innings",
         "1809_1816_E009": "No-ball law: delivery must be underhand", "1830_1835_E050": "Follow-on introduced", "1857_1884_E011": "Shoulder limit dropped (over-arm)",
         "1884_1890_E011": "Over 4 → 5 balls", "1884_1890_E023": "Declaration law", "1896_1900_E017": "Over 5 → 6 balls", "1923_1932_E028": "Ball circumference lower limit",
         "1932_1939_E019": "L.B.W. reworded", "1932_1939_E040": "Umpires may act on unfair play", "1992_2000_E002": "Spirit of Cricket preamble",
         "2010_2017_E002": "Gender-neutral definitions", "2010_2017_E101": "Players' conduct Law"}
OFF = {"1884_1890_E011": (-6, 16), "1896_1900_E017": (6, 26), "2010_2017_E002": (-6, 18), "2010_2017_E101": (-8, 34), "1992_2000_E002": (-6, 18),
       "1755_1774_E004": (4, 12), "1884_1890_E023": (-4, 24), "1857_1884_E011": (-8, 40), "1809_1816_E009": (4, -24), "1830_1835_E050": (6, 26), "1788_1803_E001": (-30, 30)}
OFFHA = {"1884_1890_E011": "right", "2010_2017_E002": "right", "2010_2017_E101": "right", "1992_2000_E002": "right", "1884_1890_E023": "right", "1857_1884_E011": "right", "1788_1803_E001": "right"}
LANES = [("ENJOYMENT", "Enjoyment", AQUA), ("NOVEL_EVENT", "Novel event", ORANGE), ("EXTERNAL_FORCE", "External force", BLUE), ("ECONOMY", "Economy", YELLOW)]
cz = [r for r in labels if r["category"] in CAUSAL]
fig, ax = plt.subplots(figsize=(13, 6.3))
rng = np.random.default_rng(3)
for li, (c, n, col) in enumerate(LANES):
    pts = [r for r in cz if r["category"] == c]
    xs = [yr(r["pair"])[1] + rng.uniform(-0.8, 0.8) for r in pts]
    ys = [li + rng.uniform(-0.17, 0.17) for _ in pts]
    ax.scatter(xs, ys, s=[70 if r["basis"] == "stated" else 38 for r in pts], color=col, edgecolor=SURF, linewidth=1, zorder=3,
               alpha=1.0, label=f"{n} ({len(pts)})")
    for r, x, y in zip(pts, xs, ys):
        if r["event_id"] in SHORT:
            ax.annotate(SHORT[r["event_id"]], (x, y), textcoords="offset points", xytext=OFF.get(r["event_id"], (4, 12)), fontsize=7.8, color=INK2, ha=OFFHA.get(r["event_id"], "left"),
                        arrowprops=dict(arrowstyle="-", color=AXIS, lw=0.6))
ax.set_yticks(range(len(LANES)))
ax.set_yticklabels([n for _, n, _ in LANES])
ax.set_ylim(-0.6, len(LANES) - 0.2)
ax.grid(axis="y", visible=False)
ax.set_xlabel("Edition year")
ax.legend(loc="upper center", ncol=4, fontsize=8.5, bbox_to_anchor=(0.5, -0.12), title="Large dot = a source states the cause; small = inferred or attributed. Dots are jittered within a lane and a few years", title_fontsize=8)
ax.set_title(f"The {len(cz)} changes with a cause: " + ", ".join(f"{n.lower()} {sum(1 for r in cz if r['category'] == c)}" for c, n, _ in LANES), loc="left", fontsize=12.5, fontweight="bold")
fig.tight_layout()
save(fig, "06_interesting_events.png")

# ---------- 7. growth of the Laws vs pace of change ----------
ed_words = {}
for p in D.glob("nodes/*.jsonl"):
    ed_words[int(p.stem)] = sum(len(json.loads(l)["text"].split()) for l in open(p, encoding="utf-8"))
eds = sorted(ed_words)
fig, (a, b) = plt.subplots(2, 1, figsize=(13, 7.5), sharex=True)
a.plot(eds, [ed_words[e] for e in eds], color=BLUE, lw=2, marker="o", ms=4.5, markeredgecolor=SURF)
a.set_ylabel("Words in the processed text")
a.set_title("The Laws grew from about 1,000 to about 33,000 words; change comes in bursts, mostly at recodifications", loc="left", fontsize=12.5, fontweight="bold")
b.bar([yr(p)[1] - GAP[p] / 2 for p in PAIRS], rate, width=[GAP[p] * 0.96 for p in PAIRS], color=ORANGE, edgecolor=SURF)
b.set_ylabel("Substantive changes per year of gap")
b.text(0.0, -0.3, "Bars span the years between the two editions compared. Word counts include prefaces and appendices where an edition has them.", transform=b.transAxes, fontsize=8, color=MUTED)
b.set_xlabel("Edition year")
for ax in (a, b):
    for y, t in ERAS:
        ax.axvline(y, color=AXIS, lw=0.8, ls=(0, (3, 3)), zorder=0)
for y, t in ERAS:
    a.text(y, a.get_ylim()[1] * 0.98, t, rotation=90, va="top", ha="right", fontsize=7.5, color=MUTED)
fig.tight_layout()
save(fig, "07_growth_vs_change.png")

# ---------- 8. Rait Kerr chronology vs detected events ----------
gold = [r for r in csv.DictReader(open(D / "gold/raitkerr_chronology.csv", encoding="utf-8")) if r["row_type"] == "change"]
gy = []
for r in gold:
    m = re.search(r"\b(1[789]\d\d)\b", r["date"] or "")
    if m and int(m.group(1)) > 1744:
        gy.append(int(m.group(1)))
dec = lambda y: y // 10 * 10
decades = list(range(1750, 1950, 10))
gc = Counter(dec(y) for y in gy)
ec = Counter()
for r in sub:
    y = yr(r["pair"])[1]
    if y <= 1947 and r["category"] != "RENUMBERING":
        ec[dec(y)] += 1
fig, ax = plt.subplots(figsize=(13, 5))
w = 3.6
ax.bar([d - w / 2 for d in decades], [gc[d] for d in decades], w, color=BLUE, edgecolor=SURF, label=f"Rait Kerr's chronology of changes ({len(gy)} dated after 1744)")
ax.bar([d + w / 2 for d in decades], [ec[d] for d in decades], w, color=ORANGE, edgecolor=SURF, label="Substantive events found in the edition comparison")
ax.set_xticks(decades)
ax.set_xticklabels([f"{d}s" for d in decades])
ax.grid(axis="x", visible=False)
ax.set_ylabel("Per decade")
ax.legend(loc="upper left", fontsize=9)
ax.set_title("Rait Kerr's chronology and the edition comparison, per decade (different definitions: events also count clarifications, reorganisation and moves)", loc="left", fontsize=11.5, fontweight="bold")
fig.tight_layout()
save(fig, "08_raitkerr_vs_detected.png")

# ---------- 9. most-changed Laws ----------
byl = defaultdict(Counter)
titles = defaultdict(Counter)
for r in labels:
    if r["substantive_change"] == "1" and r["canonical_law"]:
        byl[r["canonical_law"]][grp(r["category"])] += 1
        if r["law_title"]:
            titles[r["canonical_law"]][r["law_title"].strip().title()] += 1
lin = {r["canonical_id"]: r for r in csv.DictReader(open(D / "law_identity/law_lineage.csv", encoding="utf-8"))}
top = sorted(byl, key=lambda k: -sum(byl[k].values()))[:15][::-1]
fig, ax = plt.subplots(figsize=(12, 7))
left = np.zeros(len(top))
for g, n, c in GROUPS:
    v = np.array([byl[k][g] for k in top], float)
    ax.barh(range(len(top)), v, left=left, color=c, label=n, edgecolor=SURF, linewidth=0.8)
    left += v
nm = []
for k in top:
    t = titles[k].most_common(1)[0][0] if titles[k] else (lin.get(k, {}).get("titles_seen", "") or "").split("|")[0] or k
    nm.append(f"{t[:46]}  ({lin[k]['first_edition']}–{lin[k]['last_edition']})" if k in lin else t[:46])
ax.set_yticks(range(len(top)))
ax.set_yticklabels(nm, fontsize=8.5)
for i, t in enumerate(left):
    ax.text(t + 0.4, i, f"{int(t)}", va="center", fontsize=8, color=INK2)
ax.grid(axis="y", visible=False)
ax.set_xlabel("Substantive events over the whole period")
ax.legend(loc="lower right", fontsize=8.5)
ax.set_title("The 15 most-changed Laws (followed by content across renumberings)", loc="left", fontsize=13, fontweight="bold")
fig.tight_layout()
save(fig, "09_most_changed_laws.png")

# ---------- 10. composition by era ----------
ERA = [(0, 1830, "1752–1830"), (1830, 1884, "1830–1884"), (1884, 1947, "1884–1947"), (1947, 1992, "1947–1992"), (1992, 2020, "1992–2019")]
fig, ax = plt.subplots(figsize=(11, 5.2))
mat = []
for lo, hi, _ in ERA:
    c = Counter(grp(r["category"]) for r in sub if lo < yr(r["pair"])[1] <= hi)
    t = sum(c.values()) or 1
    mat.append([c[g] / t for g, _, _ in GROUPS])
mat = np.array(mat)
left = np.zeros(len(ERA))
for j, (g, n, c) in enumerate(GROUPS):
    ax.barh(range(len(ERA)), mat[:, j], left=left, color=c, label=n, edgecolor=SURF, linewidth=1)
    for i in range(len(ERA)):
        if mat[i, j] > 0.06:
            ax.text(left[i] + mat[i, j] / 2, i, f"{mat[i, j]:.0%}", ha="center", va="center", fontsize=8, color="#ffffff" if c != YELLOW else INK)
    left += mat[:, j]
ax.set_yticks(range(len(ERA)))
ax.set_yticklabels([f"{n}  (n={sum(1 for r in sub if lo < yr(r['pair'])[1] <= hi)})" for lo, hi, n in ERA])
ax.invert_yaxis()
ax.set_xlim(0, 1)
ax.xaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0))
ax.grid(axis="y", visible=False)
ax.legend(ncol=3, loc="upper center", bbox_to_anchor=(0.5, -0.1), fontsize=8.5)
ax.set_title("Share of substantive changes by type and era (renumbering before 1884 is mostly heading-block re-ordering)", loc="left", fontsize=12.5, fontweight="bold")
fig.tight_layout()
save(fig, "10_composition_by_era.png")
