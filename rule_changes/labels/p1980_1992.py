"""Labels for the 1980 -> 1992 edition pair. MCC: the 1992 edition was a 'second edition of the 1980 Code... incorporating
all the amendments which were approved during the intervening twelve years' (S01). Individual amendments are not dated or
explained in any source found."""
from _h import make
PAIR = "1980_1992"
L, LABELS = make(PAIR)
ST, UN, NC, EF = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE", "EXTERNAL_FORCE"
D92 = "Between the 1980 Code and its second edition of 1992 (S01); the individual amendment dates are not documented in the sources found."


def pol(eid, what, why, note=""):
    L(eid, what, UN, "no_cause_stated", "low", "none", why, ["S01"], date=D92, note=note)


pol("E001", "Law 10: if the start is delayed after the toss, the batting captain 'may request' (previously 'shall have the right to') a 7-minute roll, and the umpires must refuse the request if the delay has had no significant effect on the pitch.",
    "An amendment to the rolling provision made between 1980 and 1992; no source states a reason.")
L("E003", "Cross-reference 'See Law 27.' removed from Law 17.", ST, "wording_only", "medium", "derived", "A pointer only; no rule changes.", ["S18"])
pol("E004", "Law 17: the last-over rule now applies to 'any over of the minimum number to be played' left uncompleted at an interruption.",
    "A clarification of which overs must be completed after an interruption; no source states a reason.")
pol("E007", "Law 2 (Substitutes): the 1980 'substitutes by right for illness or injury, consent of the opposing captain for any other reason' becomes 'in normal circumstances a substitute for a player who satisfies the umpires that he has become injured or ill during the match'; in very exceptional circumstances the umpires may allow a substitute for another wholly acceptable reason, with the opposing captain's consent; a player changing shirt or boots may leave the field but no substitute is allowed.",
    "A tightening of when substitutes are allowed, by umpires' discretion; a substitute also may no longer keep wicket (in 1980 the opposing captain could object); no source states a reason.")
pol("E008", "Law 2 (Runner's equipment): the runner must wear 'the same external protective equipment as the injured batsman' (previously batting gloves and pads if the batsman is so equipped).",
    "The protective-equipment duty of a runner is widened from gloves and pads; no source states a reason (the spread of helmets and other protection is a possible context but no source says so).")
L("E009", "Law 2: the 1980 text (as digitised) is missing the words 'He may resume his' before 'innings at the fall of a wicket'; the 1992 text has them. Same rule.",
  NC, "segmentation_artefact", "high", "derived", "The old text is a truncated sentence ('...innings at the fall of a wicket, which for the purposes of this Law shall include the retirement of another Batsman'); the ACS transcription of the 1980 Code has the full rule.",
  ["S18", "S11"])
pol("E010", "Law 23 (Dead ball): a ball that does not leave the bowler's hand is dead 'other than in an attempt to run out the Non-Striker' (with a new cross-reference to Law 24.5, Bowler attempting to run out non-striker before delivery).",
    "Adds an explicit exception for the non-striker run-out attempt (Law 24.5 already existed in the 1980 Code); no source for 1980-92 states the reason (the later 2017 treatment, S06, shows the matter stayed contested).")
L("E012", "Law 36 (LBW): 'or in the case of a ball intercepted full pitch would have pitched in a straight line between wicket and wicket' shortened to 'or was intercepted full pitch': a ball intercepted full pitch no longer has to be one that 'would have pitched in a straight line'.",
  UN, "no_cause_stated", "low", "none", "A substantive change to the LBW conditions for full-pitch interceptions (old and new text compared directly), not a rewording; no source states a reason.", ["S01"], date=D92)
L("E014", "New provision under Law 38 (Run out): if, having been played by a batsman or having come off his person, the ball rebounds directly from a fielder's helmet on to the stumps with either batsman out of his ground, the batsman is Not out.",
  UN, "no_cause_stated", "low", "none", "The provision concerns fielders' helmets, but no source states the reason for the 'Not out' outcome, so no cause is asserted (helmet use is context, not evidence). Under the 2017 Code the position is reversed (a batsman can now be run out, caught or stumped from a ball deflecting off a fielder's helmet, S05).",
  ["S05", "S01"], date=D92)
L("E016", "New provisions in Law 41 (The fieldsman): protective helmets not in use must be placed, if above the surface, on the ground behind the wicket-keeper; if the ball strikes one there, five penalty runs are awarded.",
  UN, "no_cause_stated", "low", "none", "The provision regulates where fielders' helmets are placed (a fielding-advantage matter more than a safety one); no source states the reason. The same clause appears in the ACS transcription of the 1980 Code (S11), though not in the dataset's 1980 text, so its exact date of introduction is unresolved.",
  ["S11", "S01"], date=D92, note="Dating unresolved: present in ACS 1980 page, absent from dataset 1980 text.")
for e, w in (("E017", "Law 42.10 (Time wasting): cross-reference 'as set out in 8 above' added"), ("E018", "Law 42: 'reporting as set out in 8. above' cross-reference added")):
    L(e, w + " (cross-reference only).", ST, "wording_only", "medium", "derived", "Only a cross-reference is added; the procedure (caution, final warning, action against the bowler, reporting) is unchanged.", ["S18"])
L("E019", "'six-ball' written 'sixball' in the new-ball Note: format only.", NC, "format_artefact", "high", "derived", "Same text, hyphen lost (the 75 six-ball over minimum is unchanged).", ["S18"])
for e, w in (("E021", "Bails 4 3/8 in. and 1/2 in. projection written as '4 3/8' and '1/2' instead of '4⅜' and '½'"), ("E022", "Junior bails 3 7/8 in. written as '3 7/8' instead of '3⅞'")):
    L(e, w + ": notation only.", NC, "format_artefact", "high", "derived", "Same values written with a different fraction notation (a limitation of the project's own number parser, now documented).", ["S18"])
