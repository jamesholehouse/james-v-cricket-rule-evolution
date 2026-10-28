"""Labels for 1857 -> 1884.

Context for the whole pair:
- The 1884 code (adopted 21 April 1884) was a full redraft by an M.C.C. sub-committee told to revise the Laws 'by defining terms, supplying
  omissions, and better wording, but without altering the spirit of the game' (Rait Kerr ch.4). Rait Kerr says its introduction 'involved no
  major changes in the conduct of the game' and lists as the only important alterations serials 103-107, plus unnumbered 1884 entries
  (u1a players/innings/scoring/umpires/scorers, u1b 'dead ball', u2 bail thickness, u3 boundaries, u4 Lord Harris's No-ball clause, u5 one-day laws
  shown separately). That preface states the aim of the whole revision, so tidying labels below are STRUCTURAL with basis 'inferred'.
- Changes made between the editions: 1858 No-ball reinforcement (serial 97, later superseded), 1860 rolling at request of side next in
  (98), 1864 over-arm bowling (100), 1870 changing ends (101), 1883 rolling before play (102). The 1854 follow-on change (95) shows here
  only because the dataset's 1857 Laws 44-47 were imputed from the 1835 text (scan pp.10-11 missing).
- The pipeline pairs several old and new Laws by position, not content (e.g. old Law 10 with new Law 18, old Law 14 with new Law 48);
  the labels describe the actual content of each event's records and say where the paired text really went.
"""
from _h import make
PAIR = "1857_1884"
L, LABELS = make(PAIR)
ST, UN, NC, SW = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE", "SEMANTIC_WORDING"
EN, NE = "ENJOYMENT", "NOVEL_EVENT"
D1884 = "1884 code, adopted 21 April 1884 (Rait Kerr ch.4 and ch.6)."
AIM = ("Rait Kerr ch.4: the 1884 sub-committee was to revise the Laws 'by defining terms, supplying omissions, and better wording, but without "
       "altering the spirit of the game'; this states the aim of the whole revision, so the classification of this provision is inferred.")

L("E001", "New section 'ONE DAY MATCHES': '1. The side which goes in second shall follow their innings if they have scored 60 runs less than the opposite side. "
  "2. The match, when not played out, shall be decided by the first innings. 3. Prior to the commencement of a match it may be agreed that the over consists of 5 or 6 balls.'",
  ST, "reorganisation", "medium", "inferred",
  "Rait Kerr's 1884 entry (u5): 'Three Laws dealing with one-day cricket were removed from the general code and shown separately.' The 60-run "
  "one-day follow-on dates from 1854 (serial 95). Rait Kerr gives no date or reason for the first-innings decision or the 5- or 6-ball over option, "
  "which do not appear in the dataset's 1857 text.",
  ["S16"], sec=UN, secsub="no_cause_stated", date=D1884 + " One-day follow-on of 60 runs: serial 95, 15 May 1854.",
  note="The dataset's 1857 Laws 44-47 are imputed from 1835, so whether the one-day rules were already in the general code in 1857 cannot be checked here.")
L("E002", "Single Wicket section rewritten: new preamble 'The laws are, where they apply, the same as the above, with the following alterations and additions', new "
  "rule 1 'One wicket shall be pitched, as in Law 6, with a bowling stump opposite to it, at a distance of 22 yards. The bowling crease shall be in a line with "
  "the bowling stump, and drawn according to Law 7.'; 'leg-byes' added to the runs not allowed with fewer than five a side; 'ball stopped with hat' replaced by "
  "'ball wilfully stopped by a fieldsman otherwise than with any part of his person'; and 'There shall be no restriction as to the ball being bowled in overs, "
  "but no more than one minute shall be allowed between each ball.'",
  ST, "codification_definition", "medium", "inferred",
  AIM + " The new single-wicket rules spell out the set-up and adapt the section to the new general Laws (leg-byes now defined in the bye Law; the "
  "fieldsman penalty widened in the general fielding Law).",
  ["S16"], sec=UN, secsub="no_cause_stated", date=D1884,
  note="The record holds the whole new single-wicket section; the individual rules are also matched one-by-one in other events (segmentation overlap).")
L("E003", "Single Wicket rule on bounds: 'bounds shall be placed twenty-two yards each in a line from the off and leg stump' becomes '22 yards'; the heading "
  "'Laws for Single Wicket. 1' is no longer attached.",
  NC, "format_artefact", "high", "derived",
  "Number written in figures and heading split differently; the rule is identical (old text imputed from 1835 for the 1857 edition).", ["S18"])
L("E004", "Single Wicket rule on runs: 'in a line with it with his bat' becomes 'in a line with his bat' and 'returning to the popping crease as at double wicket, "
  "according to the 22nd law' becomes 'and return to the popping crease'.",
  ST, "consequential", "medium", "inferred",
  "The cross-reference to the old double-wicket Law 22 is dropped because the 1884 renumbering made it obsolete; the requirement to return to the "
  "popping crease is kept. " + AIM, ["S16", "S18"], date=D1884)
L("E005", "Single Wicket 'No hit' rule: 'otherwise the umpire shall call “No Hit.”' gains 'and no run shall be scored'.",
  ST, "codification_definition", "medium", "inferred",
  "The added clause states the consequence of a 'No hit' call, which the old rule left implicit. " + AIM, ["S16"], date=D1884)
L("E006", "Single Wicket rule for fewer than five a side: 'neither byes nor overthrows shall be allowed' becomes 'neither byes, leg-byes, nor overthrows'; "
  "'caught out behind wicket, nor stumped out' becomes 'behind the wicket, nor stumped'.",
  ST, "consequential", "medium", "inferred",
  "Leg-byes are added because the 1884 code defines them as a separate kind of run for the first time (Rait Kerr serial 105); the rest is wording.",
  ["S16"], date=D1884)
L("E007", "Single Wicket return rule: 'cross the play between the wicket, & the bowling stump' becomes 'cross the ground between the wicket and the bowling stump'.",
  SW, "terminology_term", "medium", "derived",
  "'The play' is replaced by 'the ground' for the strip between wicket and bowling stump; the same area is meant.", ["S18"])
L("E008", "Single Wicket further-run rule: 'he must touch the bowling-stump, and turn before the ball cross the play' becomes 'he must touch the bowling stump or "
  "crease and turn before the ball cross the ground'.",
  ST, "clarification_umpire_workability", "low", "inferred",
  "Adding 'or crease' brings this rule into line with the rule on the first run ('touch the bowling stump or crease'); it does relax what a striker must touch "
  "for a further run, and no source gives a reason. " + AIM,
  ["S16"], sec=UN, secsub="no_cause_stated", date=D1884)
L("E009", "Single Wicket rule for more than four a side: 'there shall be no bounds: all “hits,”' is split into 'there shall be no bounds.' with the list of allowed "
  "runs in the next sentence.",
  NC, "segmentation_artefact", "high", "derived",
  "Sentence split differently; the addition of 'leg-byes' to the allowed runs is part of the rewritten single-wicket section (event holding the new single-wicket text).",
  ["S18"])
L("E010", "New Law 1: 'A match is played between two sides of eleven players each, unless otherwise agreed to; each side has two innings, taken alternately, except in "
  "the case provided for in Law 54. The choice of innings shall be decided by tossing.'",
  ST, "codification_definition", "high", "inferred",
  "Rait Kerr 1884 entry (u1a): 'For the first time reference is found to the number of players on each side, to the number of innings ...'; the toss "
  "comes from old Law 37. " + AIM, ["S16"], date=D1884)
L("E011", "New Law 10: 'The ball must be bowled; if thrown or jerked, the umpire shall call “No ball.”' - the restriction that the hand must not be above the "
  "shoulder is gone, legalising over-arm bowling.",
  NE, "bowling_innovation", "high", "stated",
  "Rait Kerr serial 100 and ch.3: bowlers had been bowling over-arm for years despite the 1845 and 1858 reinforcements (serials 90, 97); after "
  "Willsher was no-balled six times by John Lillywhite at the Oval in 1862 and a circular to clubs showed 'the prevailing feeling seems to be, that the "
  "restriction on the height of the hand should be abolished', 'public opinion so forced the issue that, on June 10th, 1864, a General Meeting of the M.C.C. "
  "finally surrendered by granting complete emancipation to the bowlers.'",
  ["S16", "S34-04", "S34-03"], date="Rait Kerr serial 100, 10 June 1864 (the 1858 amendment, serial 97, was in force 1858-1864 but falls between the editions).")
L("E012", "Law 9 -> 11 (bowler's feet): 'and shall bowl four balls before he change wickets, which he shall be permitted to do only once in the same innings' is "
  "removed and 'otherwise the umpire shall call “No-Ball.”' (from old Law 40) is added.",
  ST, "consolidation_merge", "high", "inferred",
  "The foot-fault No-ball of old Law 40 is merged into the delivery Law; the four-ball over and the change-of-ends limit move to separate new Laws (overs; "
  "changing ends), where the 1870 change is labelled. " + AIM, ["S16"], date=D1884)
L("E013", "Old Law 12 (Wide) is removed as a block: its definition, one-run penalty, 'not reckoned as one of the four balls', and 'if the batsman shall by any means "
  "bring himself within reach of the ball, the run shall not be adjudged'.",
  ST, "reorganisation", "medium", "inferred",
  "Its parts are redistributed in 1884: definition and call to the new Wide Law, the runs to the new No-ball/Wide scoring Law, the over count to the new overs "
  "Law. The striker-moves-within-reach exception is not restated but follows from 'in the opinion of the umpire it is not within reach of the striker'. " + AIM,
  ["S16"], date=D1884)
L("E014", "New Law 12 (Wide): 'If the bowler shall bowl the ball so high over or so wide of the wicket that in the opinion of the umpire it is not within reach of "
  "the striker, the umpire shall call “Wide ball.”' (old: 'toss the ball over the striker’s head, or bowl it so wide that ... it shall not be fairly within the reach of the batsman').",
  ST, "codification_definition", "medium", "inferred",
  "Rewording of the 1845 Wide definition (Rait Kerr serial 91); 'fairly' is dropped and the reference point becomes the wicket, but Rait Kerr lists no "
  "change to Wides in 1884. " + AIM, ["S16"], date=D1884)
L("E015", "Old Law 13 removed: the runs from No-balls and Wides, and 'The names of the bowlers who bowl “wide balls” or “no balls,” in future to be placed on the score, "
  "to show the parties by whom either score is made', and the leg-bye call.",
  ST, "reorganisation", "high", "stated",
  "Rait Kerr ch.3: the 1844 scorers' instruction about bowlers' names 'appeared quite improperly as part of the Law until the revision of 1884'; it is "
  "dropped, and the scoring rules move to the new No-ball/Wide Law and the new bye/leg-bye Law.", ["S16"], date=D1884)
L("E016", "New Law 13 (Overs): 'The ball shall be bowled in overs of four balls from each wicket alternately. When four balls have been bowled, and the ball is "
  "finally settled in the bowler’s or wicket-keeper’s hands, the umpire shall call “Over.” Neither a “No-ball” nor a “Wide ball” shall be reckoned as one of the “Over.”'",
  ST, "consolidation_merge", "high", "inferred",
  "Collects the four-ball over (old Law 9), the call of 'Over' (old Law 44) and the exclusion of Wides from the over (old Law 12); extends the exclusion "
  "explicitly to No-balls. " + AIM, ["S16"], date=D1884)
L("E017", "New Law 14: 'The bowler may not change ends more than twice in the same innings nor bowl more than two overs in succession.' (old: change wickets 'only once in the same innings').",
  EN, "bowler_batsman_balance", "high", "stated",
  "Rait Kerr serial 101 and ch.3: the most important change of 1864-1884 'was clearly designed to help the bowlers by altering the 1744 provision that a "
  "bowler could only change ends once in any innings'.", ["S16"], date="Rait Kerr serial 101, 4 May 1870.")
L("E018", "Law 11 -> 15: 'He may require the striker at the wicket' becomes 'The bowler may require the batsman at the wicket'.",
  SW, "terminology_term", "medium", "derived",
  "Pronoun replaced by its noun (the Law no longer follows the bowler's Law) and 'striker' replaced by 'batsman', the 1884 code's general term; the bowler's right is unchanged.",
  ["S18"])
L("E019", "New Law 16: 'The striker may hit a “no-ball,” and whatever runs result shall be added to his score; but he shall not be out from a “no-ball,” unless he be "
  "run out or break laws 26, 27, 29, 30. All runs made from a “no-ball,” otherwise than from the bat, shall be scored “no-balls,” ... From a “wide ball” as many runs "
  "as are run shall be added to the score as “wide balls,” and if no run be otherwise obtained one run shall be so added.' (old: 'he shall not be put out except by running out').",
  ST, "codification_definition", "medium", "inferred",
  "Restates the No-ball/Wide scoring of old Law 13 and settles that runs hit off a No-ball go to the striker. It also makes the striker out from a No-ball "
  "for obstructing a catch, hitting twice, handling and obstructing the field, where the old Law said 'except by running out'; no source discusses that "
  "extension. " + AIM, ["S16"], sec=UN, secsub="no_cause_stated", date=D1884)
L("E020", "Old Law 17 removed: 'Or, if in striking, or at any other time when the ball shall be in play, both his feet shall be over the popping-crease, and his wicket put down, "
  "except his bat be grounded within it'.",
  ST, "reorganisation", "high", "inferred",
  "The content is split between the new definition of 'out of his ground', the new Stumped Law and the new Run out Law ('or at any other time, while the "
  "ball is in play'). " + AIM, ["S16"], date=D1884)
L("E021", "New Law 17: 'If the ball, not having been called “wide” or “no-ball,” pass the striker, without touching his bat, or person, and any runs be obtained, the umpire "
  "shall call “bye;” but if the ball touch any part of the striker’s person (hand excepted) and any run be obtained, the umpire shall call “leg-bye,” such runs to be "
  "scored “byes” and “leg-byes” respectively.'",
  ST, "codification_definition", "high", "inferred",
  "Rait Kerr serial 105: 'clearly both Byes and Leg Byes were a recognised means of scoring, they are now specifically defined for the first time'. "
  "Taylor 1901: leg byes were scored separately from 1850. A definition of existing practice.", ["S16", "S34-01"], date=D1884)
L("E022", "Old Law 18 removed: 'Or, if in striking at the ball he hit down his wicket'.",
  ST, "consolidation_merge", "high", "inferred",
  "Merged with old Law 22 (dress knocks down the wicket) into the new 'Hit wicket' Law. " + AIM, ["S16"], date=D1884)
L("E023", "The pipeline pairs old Law 10 (No ball: 'the hand must not be above the shoulder in delivery; and whenever the bowler shall so closely infringe ... the umpire "
  "shall call “no ball.”') with new Law 18: 'At the beginning of the match, and of each innings, the umpire at the bowler’s wicket shall call “Play”; from that time no "
  "trial ball shall be allowed to any bowler on the ground between the wickets, and when one of the batsmen is out the use of the bat shall not be allowed to any person "
  "until the next batsman shall come in.' New Law 18 merges old Law 14 (Play, trial balls) and old Law 47 (use of the bat), adds 'At the beginning of the match' and "
  "limits the trial-ball ban to 'the ground between the wickets'.",
  ST, "consolidation_merge", "medium", "inferred",
  "Mis-paired event: the removal of old Law 10's hand-height rule is labelled with the event holding the new over-arm Law 10. The content of new Law 18 is "
  "a merger of two old Laws; narrowing the trial-ball ban to the pitch is a small change no source explains. " + AIM,
  ["S16", "S18"], sec=UN, secsub="no_cause_stated", date=D1884)
L("E024", "New Law 19: 'A batsman shall be held to be “out of his ground” unless his bat in hand or some part of his person be grounded within the line of the popping crease.'",
  ST, "codification_definition", "high", "inferred",
  "A definition of a term previously described inside several dismissal Laws (old Laws 17, 21, 29). " + AIM, ["S16"], date=D1884)
L("E025", "New Law 2: 'The score shall be reckoned by runs. A run is scored—1st, so often as the batsmen after a hit, or at any time while the ball is in play, shall have crossed, "
  "and made good their ground from end to end. 2nd For penalties under Laws 16, 34, 41, and allowances under 44. Any run or runs so scored shall be duly recorded by scorers "
  "appointed for the purpose. The side which scores the greatest number of runs wins the match. No match is won unless played out or given up ...'",
  ST, "codification_definition", "high", "inferred",
  "Rait Kerr 1884 entry (u1a): first reference 'to the method by which runs are scored and the results of matches assessed, to the appointment of umpires and "
  "scorers'. " + AIM, ["S16"], date=D1884)
L("E026", "Old Law 20 removed: 'Or, if the ball be struck, and he wilfully strike it again'.",
  ST, "consolidation_merge", "high", "inferred",
  "Merged with old Law 34 (guarding the wicket) into the new 'Hit the ball twice' Law. " + AIM, ["S16"], date=D1884)
L("E027", "Old Law 15 'The striker is out if either of the bails be bowled off, or if a stump be bowled out of the ground' paired with new Law 20 'The wicket shall be held to be "
  "“down” when either of the bails is struck off, or, if both bails be off, when a stump is struck out of the ground.'",
  ST, "codification_definition", "high", "inferred",
  "Rait Kerr serial 106: the new Law defining a wicket 'down' confirms the 1838 rule (serial 85) that the fall of the remaining bail suffices; the old bowled "
  "wording goes to the new Bowled Law and the both-bails clause of old Law 21 is absorbed here. " + AIM, ["S16"], date=D1884)
L("E028", "New Law 21 (Bowled): 'If the wicket be bowled down, even if the ball first touch the striker’s bat or person—“Bowled.”'",
  ST, "codification_definition", "high", "inferred",
  "States that a ball played on still counts as bowled and names the dismissal; a definition of existing practice. " + AIM, ["S16"], date=D1884)
L("E029", "Old Law 22 removed: 'Or, if any part of the striker’s dress knock down the wicket'.",
  ST, "consolidation_merge", "high", "inferred",
  "Merged into the new 'Hit wicket' Law ('with his bat or any part of his person or dress'). " + AIM, ["S16"], date=D1884)
L("E030", "Law 16 -> 22 (Caught): 'from the stroke of the bat' -> 'from a stroke of the bat', 'before it touches' -> 'before it touch', and the dismissal name ':—“Caught.”' appended.",
  ST, "terminology", "high", "inferred",
  "The 1884 code names each mode of dismissal at the end of its Law; the catching rule itself is unchanged. " + AIM, ["S16", "S18"], date=D1884)
L("E031", "New Law 23 (Stumped): 'Or, if in playing at the ball, provided it be not touched by the bat or hand, the striker be out of his ground, and the wicket be put down by the "
  "wicket-keeper with the ball or with the hand or arm, with ball in hand:—“Stumped.”'",
  ST, "codification_definition", "high", "inferred",
  "First separate definition of stumping, previously covered by old Law 17 and the wicket-keeper Law; Rait Kerr lists no change of intent. " + AIM, ["S16"], date=D1884)
L("E032", "Law 24 (L.b.w.): the dismissal name ':—“Leg before Wicket.”' is appended; the rule (ball pitched in a straight line from wicket to wicket and would have hit it) is unchanged.",
  ST, "terminology", "high", "inferred",
  "Naming of the dismissal only. Rait Kerr 1884 entry (u6): 'the opportunity was not taken to revive the 1863 proposal to amend the “L.B.W.” Law' (serial 99).",
  ["S16"], date=D1884)
L("E033", "New Law 25 (Hit wicket): 'Or, if in playing at the ball he hit down his wicket with his bat or any part of his person or dress :—“Hit wicket.”'",
  ST, "consolidation_merge", "high", "inferred",
  "Merges old Law 18 (hit down his wicket 'in striking at the ball') and old Law 22 (dress knocks down the wicket). The dress case is now limited to 'in "
  "playing at the ball', a narrowing no source discusses. " + AIM, ["S16"], sec=UN, secsub="no_cause_stated", date=D1884)
L("E034", "Law 19 -> 26: 'either of the strikers prevent a ball from being caught, the striker of the ball is out' becomes 'either of the batsmen wilfully prevent a ball from "
  "being caught:—“Obstructing the field.”'",
  SW, "qualifier_scope", "medium", "inferred",
  "'Wilfully' is added, so an accidental obstruction of a catch is no longer out; this could change how umpires rule, but Rait Kerr's entry on obstruction "
  "(serial 107) concerns the separate new Law on obstructing any fieldsman, and no source discusses this qualifier. 'Strikers' becomes 'batsmen' and the dismissal is named.",
  ["S16", "S18"], date=D1884)
L("E035", "Old Law 27 removed: 'A striker being run out, that run which he and his partner were attempting shall not be reckoned.'",
  ST, "consolidation_merge", "high", "inferred",
  "Merged into new Law 32 with the caught rule ('A batsman being run out, that run which was being attempted shall not be scored'). " + AIM, ["S16"], date=D1884)
L("E036", "New Law 27 (Hit the ball twice): 'Or, if the ball be struck, or be stopped by any part of his person, and he wilfully strike it again, except it be done for the purpose of "
  "guarding his wicket, which he may do with his bat, or any part of his person, except his hands:—“Hit the ball twice.”'",
  ST, "consolidation_merge", "high", "inferred",
  "Merges old Law 20 (wilfully strike it again) and old Law 34 (may guard his wicket with bat or body except hands); also covers a ball first stopped by his "
  "person. " + AIM, ["S16"], date=D1884)
L("E037", "Law 21 -> 28 (Run out): 'if in running, the wicket be struck down with a throw, or by the hand or arm (with ball in hand), before his bat ... be grounded' becomes "
  "'If in running, or at any other time, while the ball is in play, he be out of his ground, and his wicket be struck down by the ball after touching any fieldsman, or by the "
  "hand or arm, with ball in hand, of any fieldsman : “Run out.”'; the clause 'But if both the bails be off, a stump must be struck out of the ground' moves to the wicket-down Law.",
  ST, "codification_definition", "medium", "inferred",
  "Merges old Law 17's 'at any other time' case into run out and states that the ball must have touched a fieldsman; Rait Kerr lists no change of intent. " + AIM,
  ["S16"], date=D1884)
L("E038", "Law 23 -> 29 (Handled the ball): 'if the striker touch or take up the ball while in play, unless at the request of the opposite party' becomes 'if he touch with his hands "
  "or take up the ball while in play, unless at the request of the opposite side :—“Handled the ball.”', now under the heading 'Either batsman is out'.",
  ST, "clarification_umpire_workability", "medium", "inferred",
  "'With his hands' makes explicit what old Law 34 implied (the body may be used, not the hands); placing the Law under 'Either batsman is out' extends it to "
  "the non-striker, which no source discusses. " + AIM, ["S16"], sec=UN, secsub="no_cause_stated", date=D1884)
L("E039", "Old Law 3 (The stumps: 'three in number; twenty-seven inches out of the ground; the bails eight inches in length ...') removed as a separate Law.",
  ST, "consolidation_merge", "high", "inferred",
  "Merged into the new Wickets Law 6 (which restates 27 in, three stumps, and adds the bail dimensions). " + AIM, ["S16"], date=D1884)
L("E040", "New Law 3: 'Before the commencement of the match two umpires shall be appointed, one for each end.'",
  ST, "codification_definition", "high", "inferred",
  "Rait Kerr serial 104: 'The umpires are to be appointed “one for each end”—a truly significant phrase'; he gives no cause. Part of the first reference to "
  "the appointment of umpires (u1a). " + AIM, ["S16"], date=D1884)
L("E041", "New Law 30: 'Or, if he wilfully obstruct any fieldsman:— “Obstructing the field.”' (under 'Either batsman is out').",
  UN, "no_cause_stated", "high", "none",
  "Rait Kerr serial 107: the Obstruction Law 'is extended to cover not only the obstruction of a catch but now any form of such tactics by either batsman'; "
  "listed among the 1884 code's 'only important alterations', with no reason given. Taylor 1901 notes the first mention of a batsman infringing this law in 1864, without a reason.",
  ["S16", "S34-02"], date=D1884)
L("E042", "Law 25 -> 31: 'If the players have crossed each other, he that runs for the wicket which is put down is out.' becomes 'If the batsmen have crossed each other, he that "
  "runs for the wicket which is put down is out; if they have not crossed, he that has left the wicket which is put down is out.'",
  ST, "drafting_omission", "high", "inferred",
  "Supplies the missing not-crossed case and uses 'batsmen'; this follows directly from the existing rule. " + AIM, ["S16"], date=D1884)
L("E043", "Law 26 -> 32: 'A ball being caught no runs shall be reckoned.' becomes 'The striker being caught no run shall be scored.' and 'A batsman being run out, that run which "
  "was being attempted shall not be scored.' is added (from old Law 27).",
  ST, "consolidation_merge", "high", "inferred",
  "Two old scoring-on-dismissal Laws merged into one; same effect. " + AIM, ["S16"], date=D1884)
L("E044", "New Law 33: 'A batsman being out from any cause, the ball shall be “dead.”'",
  ST, "codification_definition", "high", "inferred",
  "Rait Kerr 1884 entry (u1b): 'throughout the revision free use is made of the term “Dead ball” about which previously there were no very explicit instructions.'",
  ["S16"], date=D1884)
L("E045", "Old Law 34 removed: 'The ball having been hit, the striker may guard his wicket with his bat, or with any part of his body except his hands; that the 23d law may not be disobeyed.'",
  ST, "consolidation_merge", "high", "inferred",
  "Merged into the new 'Hit the ball twice' Law ('except it be done for the purpose of guarding his wicket ... except his hands'). " + AIM, ["S16"], date=D1884)
L("E046", "Law 28 -> 34 (Lost ball): 'If a lost ball be called, the striker shall be allowed six runs ...' becomes 'If a ball in play cannot be found or recovered, any fieldsman may "
  "call “lost ball,” when the ball shall be “dead;” six runs shall be added to the score, but if more than six runs have been run before “lost ball” has been called, as many runs "
  "as have been run shall be scored.'",
  ST, "clarification_umpire_workability", "medium", "inferred",
  "Says who may call lost ball, when, and that the ball is then dead; the six-run allowance is unchanged. Taylor 1901 remarks that 'or recovered' 'has done "
  "away with many disputes', which suggests the clarifying purpose but is his comment on the effect, not a stated cause.",
  ["S16", "S34-02"], date=D1884)
L("E047", "Law 29 -> 35: 'it shall be considered dead' -> 'it shall be “dead;”'; 'if the striker at his wicket go outside the popping-crease ... the said bowler may put him out, "
  "unless (with reference to the 21st law) his bat in hand, or some part of his person, be within the popping-crease' -> 'if the batsman at his wicket be out of his ground "
  "before actual delivery, the said bowler may run him out; but if the bowler throw at that wicket and any run result, it shall be scored “No-Ball.”'",
  ST, "codification_definition", "medium", "inferred",
  "Uses the new defined terms ('dead', 'out of his ground', 'run out'). The new clause scoring runs from a bowler's throw at the wicket as No-ball is a real "
  "addition with no source explaining it. " + AIM, ["S16"], sec=UN, secsub="no_cause_stated", date=D1884)
L("E048", "Law 30 -> 36: 'The striker shall not retire ... without the consent of the opposite party' becomes 'A batsman shall not retire ... without the consent of the opposite side'.",
  SW, "terminology_term", "high", "derived",
  "'Striker' -> 'batsman' and 'party' -> 'side', the 1884 code's general terms; the 1854 retirement rule is unchanged.", ["S18"])
L("E049", "New Law 37: 'A substitute shall be allowed to field or run between wickets for any player who may during the match be incapacitated from illness or injury, but for no "
  "other reason, except with the consent of the opposite side.' (old Law 31: 'No substitute shall in any case be allowed to stand out, or run between wickets for another "
  "person, without the consent of the opposite party').",
  UN, "no_cause_stated", "medium", "none",
  "A substitute for an ill or injured player becomes an entitlement instead of needing consent; consent is kept only for other reasons. Neither Rait Kerr's "
  "1884 entries nor Taylor 1901 (who says only that a substitute for a retiring player was 'generally granted') give a reason for writing this into the Law.",
  ["S16", "S34-02"], date=D1884)
L("E050", "Law 32 -> 38: 'the consent of the opposite party shall also be obtained as to the person to act as substitute' becomes 'the consent of the opposite side shall be obtained ...'.",
  SW, "terminology_term", "high", "derived",
  "'Party' -> 'side'; 'also' dropped because the preceding Law no longer requires consent in every case. The rule on choosing the substitute and his place is unchanged.",
  ["S18"])
L("E051", "Law 31 -> 39: the runner rule becomes 'In case any substitute shall be allowed to run between wickets, the striker may be run out if either he or his substitute be out of his "
  "ground.' with a new clause 'If the striker be out of his ground while the ball is in play, that wicket which he has left may be put down and the striker given out, although the "
  "other batsman may have made good the ground at that end, and the striker and his substitute at the other end.'",
  ST, "drafting_omission", "medium", "inferred",
  "Restates the 1854 runner liability (Rait Kerr serial 94b) with the defined term 'out of his ground' and supplies the case of the injured striker himself "
  "leaving his ground. " + AIM, ["S16"], date=D1884)
L("E052", "Law 1 -> 4 (Ball): 'must weigh not less than five ounces and a-half, nor more than five ounces and three-quarters' -> 'shall weigh not less than 5½oz., nor more than "
  "5¾oz.'; circumference '9in. ... 9¼in.'; 'either party may call for a new ball' -> 'either side may demand a new ball'.",
  SW, "modal_strength", "low", "derived",
  "Values unchanged. 'Must' -> 'shall' follows the 1884 code's uniform drafting and does not change the requirement; 'call for' -> 'demand' and 'party' -> "
  "'side' are terminology. The raw OCR shows the fractions illegibly ('5Joz', '5|oz', '9,iin'), but the same limits are in 1857 and in Taylor 1901, so the "
  "numbers are accepted.",
  ["S18", "S34-03"], date=D1884)
L("E053", "Old Law 40 removed: 'But if one of the bowler’s feet be not on the ground behind the bowling-crease, and within the return-crease, when he shall deliver the ball, the "
  "umpire at his wicket, unasked, must call “no ball.”'",
  ST, "consolidation_merge", "high", "inferred",
  "Merged into new Law 11 ('otherwise the umpire shall call “No-Ball.”'). " + AIM, ["S16"], date=D1884)
L("E054", "New Law 40: 'A batsman is liable to be out for any infringement of the laws by his substitute.'",
  UN, "no_cause_stated", "high", "none",
  "Rait Kerr serial 103: 'A striker becomes liable to be out for any infringement of the Laws by his runner—previously only his liability in respect of a run "
  "out had been mentioned'; one of the 1884 code's 'only important alterations', with no reason given.", ["S16"], date=D1884)
L("E055", "Law 33 -> 41: 'If any fieldsman stop the ball with his bat [sic, hat], the ball shall be considered dead, and the opposite party shall add five runs ...' becomes 'The "
  "fieldsman may stop the ball with any part of his person, but if he wilfully stop it otherwise the ball shall be “dead,” and five runs added to the score. Whatever runs may "
  "have been made five only shall be added.'",
  ST, "codification_definition", "medium", "inferred",
  "The penalty is widened from the hat (the 1857 'bat' is a misreading or misprint) to any wilful stop other than with the person. Taylor 1901 dates the "
  "widening to 1884 ('hat or any other article') with the present wording soon after; no source gives a reason, and Rait Kerr does not list it among the important 1884 changes.",
  ["S16", "S34-02"], sec=UN, secsub="no_cause_stated", date=D1884)
L("E056", "Law 35 -> 42 (Wicket-keeper): 'The wicket-keeper shall stand behind the wicket.' is added; 'he shall not move until the ball be out of the bowler’s hand' is dropped and "
  "'incommode the striker by any noise' becomes 'by any noise, or motion'; the striker is not out if the keeper offends, 'excepting under laws 26, 27, 28, 29, and 30'.",
  ST, "codification_definition", "medium", "inferred",
  "Reworded and completed; standing behind the wicket and the exceptions for other dismissals are new statements, and replacing the no-movement rule with "
  "'motion' that incommodes the striker is a small change no source explains. " + AIM, ["S16"], sec=UN, secsub="no_cause_stated", date=D1884)
L("E057", "New Law 43: 'The umpires are the sole judges of fair or unfair play, of the fitness of the ground, the weather, and the light for play; all disputes shall be determined by "
  "them, and if they disagree the actual state of things shall continue.'",
  ST, "codification_definition", "medium", "inferred",
  "Keeps old Law 36's 'sole judges of fair or unfair play' and adds the umpires' authority over ground, weather and light and a rule for disagreement, matters "
  "previously unwritten. Rait Kerr does not list it among the important 1884 changes. " + AIM, ["S16"], sec=UN, secsub="no_cause_stated", date=D1884)
L("E058", "Old Law 44 removed: 'After the delivery of four balls, the umpire must call “Over,” ... nevertheless if an idea be entertained that either of the strikers is out, a question "
  "may be put previously to, but not after the delivery of the next ball.'",
  ST, "reorganisation", "high", "inferred",
  "Split between the new overs Law and the new Law on appeals after 'Over'. The 1857 wording here is imputed from the 1835 text (missing pages). " + AIM,
  ["S16"], date=D1884, integrity="suspect", note="Old text imputed from 1835 by the data team (data_appendix.xlsx).")
L("E059", "Law 37 -> 44: 'The umpires in all matches shall pitch fair wickets; and the parties shall toss-up for choice of innings. The umpires shall change wickets after each party "
  "has had one innings.' becomes 'They shall pitch fair wickets, arrange boundaries where necessary, and the allowances to be made for them, and change ends after each side has had one innings.'",
  ST, "codification_definition", "high", "inferred",
  "Rait Kerr 1884 entry (u3): '“Boundaries” are officially mentioned for the first time, though they were in use many years earlier.' The toss moves to "
  "new Law 1. " + AIM, ["S16"], date=D1884)
L("E060", "Law 38 -> 45: 'When the umpire shall call “play,” the party refusing to play shall lose the match.' becomes 'When they shall call “play,” the side refusing to play shall lose the match.'",
  SW, "terminology_term", "high", "derived",
  "'The umpire' -> 'they' (the umpires) and 'party' -> 'side'; same rule.", ["S18"])
L("E061", "Law 39 -> 46: 'They are not to order a striker out unless appealed to by the adversaries' becomes 'They shall not order a batsman out unless appealed to by the other side.'",
  SW, "modal_strength", "medium", "derived",
  "'Are not to' -> 'shall not' (a firmer form of the same prohibition), 'striker' -> 'batsman' (covers both batsmen, as appeals already did in practice) "
  "and 'adversaries' -> 'other side'. No source records a change in the appeal rule.", ["S18"])
L("E062", "Old Law 47 removed: 'When one of the strikers shall have been put out, the use of the bat shall not be allowed to any person, until the next striker shall come in.' - "
  "in the 1857 segmentation this block also carries the whole old Single Wicket section.",
  NC, "segmentation_artefact", "medium", "derived",
  "The use-of-the-bat sentence is merged into new Law 18 (labelled with the event that pairs it with old Law 10); the single-wicket rules reappear in the new "
  "Single Wicket section and are matched rule by rule in other events. Old Law 47 and Single Wicket 1-5 of 1857 are imputed from 1835.",
  ["S18"], integrity="suspect", note="Old text partly imputed from 1835 (missing pp.10-11 of the 1857 scan).")
L("E063", "Law 36 -> 47: 'The umpires are the sole judges of fair or unfair play; and all disputes shall be determined by them, each at his own wicket; but in case of a catch which the "
  "umpire at the wicket bowled from cannot see sufficiently to decide upon, he may apply to the other umpire, whose opinion shall be conclusive.' becomes 'The umpire at the "
  "bowler’s wicket shall be appealed to before the other umpire in all cases except in those of stumping, hit wicket, run out at the striker’s wicket, or arising out of Law 42, "
  "but in any case in which an umpire is unable to give a decision he shall appeal to the other umpire, whose decision shall be final.'",
  ST, "clarification_umpire_workability", "medium", "inferred",
  "Spells out which umpire answers which appeal and extends the consult-the-other-umpire rule from catches to any case; the 'sole judges' clause moves to "
  "new Law 43. " + AIM, ["S16"], date=D1884)
L("E064", "The pipeline pairs old Law 14 (call of Play, no trial ball) with new Law 48: 'If the umpire at the bowler’s end be not satisfied of the absolute fairness of the delivery of "
  "any ball, he shall call “No ball.”'",
  NE, "tactic_abuse", "high", "stated",
  "Rait Kerr ch.3 and 1884 entry (u4): with 'throwing' widespread from 1882 (bowlers 'openly boasting that they could “throw” once an over without fear of "
  "detection'), Lord Harris at the Special General Meeting 'secured a last-minute addition to the Laws of a clause directing the umpire at the bowler’s end "
  "to call “No ball” if not satisfied with the absolute fairness of the delivery' - in effect a return to the 1845 formula. Old Law 14's content went to new Law 18.",
  ["S16"], date="Special General Meeting, 21 April 1884 (Rait Kerr ch.3-4).")
L("E065", "Law 45 -> 49: 'The umpire must take especial care to call “No Ball” instantly upon delivery, “Wide Ball” as soon as ever it shall pass the striker.' becomes 'The umpire shall "
  "take especial care ... “Wide ball” as soon as it shall have passed the striker.'",
  SW, "modal_strength", "low", "derived",
  "'Must' -> 'shall' (the 1884 code's uniform drafting) and 'as soon as ever it shall pass' -> 'as soon as it shall have passed'; the timing of the calls "
  "(Rait Kerr serial 80) is unchanged. Old text imputed from 1835 for the 1857 edition.", ["S18"], integrity="suspect",
  note="Old text imputed from 1835 (missing pp.10-11 of the 1857 scan).")
L("E066", "Law 2 -> 5 (Bat): 'The bat must not exceed four and a-quarter inches ... must not be more than thirty-eight inches' becomes 'The bat shall not exceed 4¼in. ... shall not be more than 38in.'",
  SW, "modal_strength", "low", "derived",
  "Values unchanged (4¼ in since 1771, 38 in since 1835 per Rait Kerr); 'must' -> 'shall' is uniform 1884 drafting. The raw OCR fraction is illegible "
  "('4|in.') but the width is the long-standing one, so the number is accepted.", ["S18", "S16"], date=D1884)
L("E067", "Law 41 -> 50: 'If either of the strikers run a short run, the umpire must call “one short.”' becomes 'If either batsman run a short run, the umpire shall call “One short,” and the run shall not be scored.'",
  ST, "codification_definition", "high", "inferred",
  "The consequence of the call (the short run is not scored) is stated for the first time; 'must' -> 'shall' and 'strikers' -> 'batsman' follow the "
  "1884 drafting. " + AIM, ["S16"], date=D1884)
L("E068", "New Law 51: 'After the umpire has called “Over,” the ball is “dead,” but an appeal may be made as to whether either batsman is out, such appeal, however, shall not be made "
  "after the delivery of the next ball, nor after any cessation of play.'",
  ST, "reorganisation", "medium", "inferred",
  "Carries over the appeal part of old Law 44 (1835 serial 81: appeal before the next ball) and adds 'nor after any cessation of play', a small extension "
  "no source explains. " + AIM, ["S16"], sec=UN, secsub="no_cause_stated", date=D1884)
L("E069", "Law 43 -> 53: 'No umpire is to be changed during a match, unless with the consent of both parties, except in case of violation of the 42d law; then either party may dismiss "
  "the transgressor.' becomes 'No umpire shall be changed ... unless with the consent of both sides, except in case of violation of Law 52, then either side may dismiss him.'",
  ST, "consequential", "high", "inferred",
  "Cross-reference renumbered (no-betting Law 42 -> 52), 'is to be' -> 'shall be', 'parties' -> 'sides'; the 1835 rule (Rait Kerr serial 76) is unchanged.",
  ["S16", "S18"], date=D1884)
L("E070", "Law 46 -> 54 (Follow on): 'The players who go in second shall follow their innings, if they have obtained one hundred runs less than their antagonist.' becomes 'The side which "
  "goes in second shall follow their innings, if they have scored eighty runs less than the opposite side.'",
  EN, "avoid_draws", "medium", "inferred",
  "Rait Kerr serial 95 (May 15th 1854): follow-on limit reduced to 80 runs (60 in one-day matches). He gives the purpose of the follow-on Law as a whole "
  "('designed to reduce the number of undecided matches', ch.3; follow-on and declaration Laws 'primarily directed towards reducing the number of drawn "
  "matches', ch.4), not of this reduction, so the cause is inferred.",
  ["S16"], date="Rait Kerr serial 95, 15 May 1854. The dataset shows it only in 1884 because the 1857 Law 46 is imputed from 1835.",
  integrity="suspect", note="Old text imputed from 1835 (missing pp.10-11 of the 1857 scan); the 1857 printing probably already had 80 runs.")
L("E071", "Law 6 (Wickets): 'The wickets must be pitched opposite to each other by the umpires, at the distance of twentytwo yards.' becomes 'The wickets shall be pitched opposite and "
  "parallel to each other, at a distance of 22 yards.' with added sentences: 'Each wicket shall be 8in. in width and consist of three stumps, with two bails upon the top.' "
  "'The stumps shall be of equal and sufficient size to prevent the ball from passing through, 27in. out of the ground.' 'The bails shall be each 4¾in. in length, and when in "
  "position, on the top of the stumps, shall not project more than ¾in. above them.' 'The wickets shall not be changed during a match, unless the ground between them become "
  "unfit for play, and then only by consent of both sides.'",
  ST, "clarification_umpire_workability", "high", "stated",
  "Rait Kerr 1884 entry (u2): 'The thickness of the bail is specified for the first time to remove doubts about the overall height of the wicket' (ch.4: "
  "'the only modification made in the new code in respect of the wicket'). The rest merges old Law 3 (stumps) and old Law 8 (changing wickets) into one Law. "
  "The processed '4¾in.' and '¾in.' are not supported: the raw OCR reads '4in.' and '^in.', Taylor 1901 gives two bails of 4 inches, and the 1890s "
  "editions read 'four inches' and 'half-an-inch'. The bail figures were most likely 4 in and ½ in; the AI clean-up invented the fractions.",
  ["S16", "S34-03", "S17"], date=D1884, integrity="suspect",
  note="Numeric values for bail length and projection in the processed 1884 text are clean-up inventions; see raw OCR lines 'The bails shall be each 4in.' and 'project more than ^in.'.")
L("E072", "Law 4 -> 7 (Bowling crease): 'must be in a line with the stumps; six feet eight inches in length; ... with a return crease at each end towards the bowler, at right angles' "
  "becomes 'shall be in a line with the stumps, 6ft. 8in. in length; ... with a return crease at each end, at right angles behind the wicket.'",
  SW, "clarifying_rewrite", "medium", "derived",
  "'Towards the bowler' -> 'behind the wicket' describes the same direction of the return crease from the other side; 'must' -> 'shall' and figures for "
  "words. Same 6 ft 8 in crease (Rait Kerr serial 69).", ["S18", "S16"])
L("E073", "Old Law 8 removed: 'After rain the wickets may be changed with the consent of both parties.'",
  ST, "consolidation_merge", "medium", "inferred",
  "Folded into the new Wickets Law as 'The wickets shall not be changed during a match, unless the ground between them become unfit for play, and then only "
  "by consent of both sides' - the rain case is generalised to any unfitness, still needing both sides' consent. " + AIM, ["S16"], date=D1884)
L("E074", "Law 5 -> 8 (Popping crease): 'must be four feet from the wicket, and parallel to it, unlimited in length, but not shorter than the bowling-crease' becomes 'shall be marked 4ft. "
  "from the wicket, parallel to it, and be deemed unlimited in length.'",
  SW, "clarifying_rewrite", "medium", "derived",
  "'Marked' and 'deemed unlimited' make the line notional beyond its marked length; the minimum 'not shorter than the bowling-crease' is dropped. The "
  "position (4 ft) is unchanged and no source records a change in how the crease is drawn or judged.", ["S18"])
L("E075", "Law 7 -> 9 (Rolling): 'It shall not be lawful for either party during a match without the consent of the other, to alter the ground by rolling ... except at the commencement of "
  "each innings, when the ground may be swept and rolled at the request of either party ... within one minute' becomes 'The ground shall not be rolled, watered, covered, mown or "
  "beaten during a match, except before the commencement of each innings and of each day’s play, when, unless the in-side object, the ground shall be swept and rolled for not "
  "more than ten minutes.' The sawdust proviso becomes 'nor the batsman nor bowler from using sawdust in order to obtain a proper foothold.'",
  UN, "no_cause_stated", "high", "none",
  "Combines Rait Kerr serial 98 (June 11th 1860: rolling between innings at the request of the side next to bat) and serial 102 (May 2nd 1883, promulgated in "
  "1884: rolling for 10 minutes before the start of play, which 'emanated from the County Secretaries'). Rait Kerr names who proposed the 1883 change but "
  "gives no reason for either; Taylor 1901 only dates the rule's first use to 1883. The sawdust wording (batsman as well as bowler, for a foothold) is undiscussed.",
  ["S16", "S34-03"], date="Rait Kerr serials 98 (11 June 1860) and 102 (decided 2 May 1883, promulgated in the 1884 code).")
