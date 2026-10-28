"""Labels for events added after the first labelling pass (authored against the pipeline output of the verification-fix run)."""
from _h import make
PAIR = "2000_2008"
L, LABELS = make(PAIR)
ST, UN, NC = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE"
D = "Between the 2000 Code and its 3rd edition of 2008 (2nd edition 2003); individual amendment dates not documented in the sources found."


def art(eid, what, why, sub="segmentation_artefact", conf="high"):
    L(eid, what, NC, sub, conf, "derived", why, ["S18"])


def pol(eid, what, why="An amendment between the 2000 Code and its 3rd edition (2008); no source found states a reason."):
    L(eid, what, UN, "no_cause_stated", "low", "none", why, ["S01"], date=D)


for e, w in (("E013", "Law 19 (Boundaries): the list of Laws under which penalty runs stand alongside a boundary ('any penalties under any of Laws 2.6, 18.5(b), ...') is shortened to 'either of Laws 18.5(b) and ...'."),
             ("E014", "Law 19: the boundary-allowance wording is re-pointed ('these runs' becomes 'the runs in (b)(ii) above') and the same shortened list of penalty Laws is used."),
             ("E017", "Law 20 (Lost ball): the list of Laws under which penalty runs stand ('any of Laws 2.6, 18.5(b), ...') is shortened to 'either of Laws 18.5(b) and ...'.")):
    pol(e, w, "The list of penalty-run Laws that stand together with a No ball/Wide penalty is restated; whether this changes the rule (the penalty for a player returning without permission, Law 2.6, is no longer named) is not shown, and no source states a reason.")
L("E023", "Law 27 (Appeals): the heading 'Appeal \u201cHow\u2019s That?\u201d' appears as a separate unit in the 2008 text.", ST, "wording_only", "low", "derived", "A heading unit for the appeal formula; no rule text is added.", ["S18"], date=D)
art("E024", "Law 28 (Wicket is down): the 'Dispensing with bails' provision, already in the 2000 text, is re-segmented (a stray '4.' is dropped and a trailing '(b)' clause moves).", "Both texts contain the provision; only the segmentation and a stray '4.' differ.", conf="medium")
art("E025", "Law 29: OCR errors ('out' for 'but', 'non-striker' vs 'nonstriker'); same rule.", "The differences are mis-recognised words and hyphenation.", sub="ocr_noise")
art("E027", "Law 3: cross-reference '15 9(b)(ii)' (missing full stop) corrected to '15.9(b)(ii)'.", "A one-character typographical difference in a cross-reference.", sub="format_artefact")
art("E030", "Law 3 (Umpires' signals): the signals table ('Five penalty runs', 'Revoke last signal') is laid out differently in the two texts; same signals.", "The words are the same; only the table layout of the digitised text differs.")
art("E033", "Law 34: OCR error 'La a' for 'Law'; same rule.", "An OCR error in the 2008 text.", sub="ocr_noise")
art("E036", "Law 36 (LBW): conditions (a)-(c) are written with different spacing and quote marks; same rule.", "Differences are spacing and punctuation (and 'full pitch' vs 'fullpitch').", sub="format_artefact")
art("E041", "Law 41: OCR error 'nor contravened' for 'not contravened'; same rule.", "An OCR error in the old text.", sub="ocr_noise")
pol("E044", "Law 42 (Fair and unfair play): the procedure for dangerous or unfair bowling is rewritten: 'As soon as the umpire at the bowler's end decides under 6(a) that the bowling of fast short pitched balls has become dangerous and unfair, or ... there is an instance of dangerous and unfair bowling as defined in 6(b)'; 'second instance' becomes 'any further instance', and 'further instance' becomes 'any further repetition'.")
L("E052", "Law 8 (The wickets): the pointer 'See Appendix A' and list numbers 1-4 are dropped from the stumps clause; same specification.", ST, "wording_only", "medium", "derived", "A cross-reference and list markers are removed; the stump size rule is unchanged.", ["S18"], date=D)
