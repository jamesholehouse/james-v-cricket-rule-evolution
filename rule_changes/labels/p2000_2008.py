"""Labels for the 2000 -> 2008 edition pair: the 2000 Code 2nd edition (2003) and 3rd edition (2008). No MCC list of the
amendments in these two editions was found; labels therefore describe the change from the text and cite evidence only where it
exists (the 2008 bat Law, S22)."""
from _h import make
PAIR = "2000_2008"
L, LABELS = make(PAIR)
ST, UN, NC, NE = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE", "NOVEL_EVENT"
D = "Between the 2000 Code and its 3rd edition of 2008 (2nd edition 2003); individual amendment dates not documented in the sources found."


def pol(eid, what, why="An amendment between the 2000 Code and its 3rd edition (2008); no source found states a reason.", note=""):
    L(eid, what, UN, "no_cause_stated", "low", "none", why, ["S01"], date=D, note=note)


def art(eid, what, why, sub="segmentation_artefact", ev=None, conf="medium", integrity="ok", note=""):
    L(eid, what, NC, sub, conf, "derived", why, ev or ["S18"], integrity=integrity, note=note)


pol("E001", "New definition (Appendix A): 'Conduct of the game includes any action relevant to the match at any time on any day of the match.'")
L("E003", "New bat Law 6 and Appendix: bats are graded A, B and C (conforming to Law 6 sections 1 to 8); other bats are not recognised in the Laws; Grade A bats may be used at any level, lower grades only at levels set by the national governing body; the blade, handle (upper and lower portions), face, back, shoulders, sides and toe are each defined.",
  UN, "no_cause_stated", "low", "none",
  "New, much more prescriptive Law 6 with a new Appendix E, effective 1 October 2008. S22 (an anonymous forum post, 23 Mar 2010) says only that the Mongoose bats 'conform to the new version of Law 6 and Appendix E, which came into force on 1st October 2008'; MCC tested and approved the Mongoose in 2009, after the new Law, so it cannot have caused it. No source states why the Law was rewritten.",
  ["S22"], date="Effective 1 October 2008 (S22, anonymous forum post: low reliability).", sec=ST, secsub="codification_definition")
L("E048", "Law 6 (The bat) rewritten: 'The bat consists of two parts, a handle and a blade'; measurements are set in the new Appendix E; separate sections on the handle, the blade, grades of bat and the covering/damage provisions replace the old 'Width and length' paragraph (38 in length; blade of wood not exceeding 4 1/4 in).",
  UN, "no_cause_stated", "low", "none", "Same new Law 6 and Appendix E as E003. S22 (an anonymous forum post, 23 Mar 2010) says only that the Mongoose bats 'conform to the new version of Law 6 and Appendix E, which came into force on 1st October 2008'; MCC tested and approved the Mongoose in 2009, after the new Law, so it cannot have caused it. No source states why the Law was rewritten.", ["S22"], date="Effective 1 October 2008 (S22, anonymous forum post: low reliability).", sec=ST, secsub="codification_definition",
  integrity="suspect", note="The apparent loss of the 4 1/4 in. width limit is not shown: it moves into Appendix E.")
pol("E005", "Law 15 (Intervals): tea interval with nine wickets down restated ('If either 9 wickets are already down when 2 minutes remain to the agreed time for tea or the 9th wicket falls within these 2 minutes ...').",
    note="Some of the text also exists elsewhere in the 2000 edition (moved).")
pol("E007", "Law 17 (Practice on the field): the penalty for a bowler who contravenes the practice rules changes from 'not allowed to bowl until at least 5 complete overs have been bowled by his side' to 'until either at least one hour has elapsed or there has been at least 30 minutes of playing time since the contravention'; the part-over provision is dropped.")
pol("E009", "Law 18 (Deliberate short running): the warning to the batsmen 'shall continue to apply throughout the innings' and the umpire 'shall so inform each incoming batsman'.")
pol("E010", "Law 18: a further instance of deliberate short running is now by 'any batsman' (previously 'either of the same batsmen') in that innings.")
L("E011", "Cross-reference 'Note, however, Law 42.17(b) (Penalty runs)' removed from Law 18.", ST, "wording_only", "medium", "derived", "A cross-reference only; the penalty-run Law itself is unchanged here.", ["S18"])
pol("E016", "Law 2: the sentence 'The ball shall not count as one of the over' added to a substitute/runner provision.")
pol("E019", "Law 21 (The result): 'Nothing that happens thereafter, except as in Law 42.17(b) (Penalty runs), shall be regarded as part of it.'")
pol("E020", "Law 21: statement of result: a side batting last that wins without losing all wickets wins by wickets in hand; new provision where the side batting last has lost all its wickets but wins through an award of 5 penalty runs at the end of the match.")
pol("E021", "Law 22 (The over): the cases in which a ball does not count in the over are restated (called dead under Law 23.3(b); 5 penalty runs awarded under Laws 2.6, etc.).")
L("E022", "Law 22: 'suspended under any of Laws ...' becomes 'suspended under any of the Laws': a closed list of Laws is replaced by all Laws, which broadens the rule.", UN, "no_cause_stated", "low", "none", "A reference to specific Laws is generalised to any Law, broadening the rule; no source states a reason.", ["S01"])
pol("E024", "Law 26 (Leg byes): runs from a ball first striking the striker's person are scored only if the umpire is satisfied the striker attempted to play the ball with his bat or tried to avoid being hit; if satisfied, and the ball makes no subsequent contact with the bat, runs completed or a boundary allowance are credited as leg byes.")
art("E025", "Law 28 (Wicket is down): the 'Dispensing with bails' provision is already in the 2000 text; only the segmentation and a stray '4.' differ.", "Old record: 'Dispensing with bails ... (a) After a decision ... (b) If the wicket has already been broken ...' is in the 2000 text.")
art("E031", "Law 32 (Caught): cross-reference '19 4' corrected to '19.4'.", "A typographical correction of a Law number.", sub="format_artefact", conf="high")
pol("E033", "Law 35 (Hit wicket): the striker is out only if 'after the bowler has entered his delivery stride and while the ball is in play' his wicket is put down (previously 'while the ball is in play').", note="Related to the 'delivery stride' definition, which also appears in later no-ball changes.")
pol("E034", "Law 35: the bowler 'after entering his delivery stride' (previously 'after starting his run up, or his bowling action if he has no run up') not delivering the ball.")
pol("E036", "Law 40 (Wicket-keeper): gloves provision restated: 'If, as permitted under 1 above, the wicket-keeper wears gloves, they shall have no webbing between the fingers except joining index finger and thumb'; added 'If used, the webbing shall be ...'.")
pol("E037", "Law 40: 'If, in the opinion of either umpire, the wicket-keeper interferes with the striker's right to play the ball' Law 23.3(b)(vi) applies; if the interference was wilful Law 42.4 (Deliberate attempt to distract striker) applies.")
pol("E038", "Law 41: 'The ball shall not count as one of the over' added to a fielder provision.")
pol("E039", "Law 42: when a ball is called dead for certain unfair acts, 'the ball shall not count as one of the over' and 'the batsmen at the wicket shall decide which of them is to face the next delivery'.")
pol("E040", "Law 42: deliveries passing over head height after pitching are 'included with' (treated as) other unfair deliveries; wording extended.")
art("E042", "Law 42: 'See 17 below' reference attached to the following unit; no change.", "The same words are present in both editions.", ev=["S18"])
pol("E043", "Law 42: after certain penalty cases 'The batsmen shall return to their original ends.'")
pol("E044", "Law 42.17 (Penalty runs): the 2000 rule that penalty runs are not awarded once the match is concluded becomes 'Notwithstanding the provisions of Law 21.6 (Winning hit or extras), penalty runs shall be awarded in each case where the Laws require the award', with a list of exceptions (Laws 26.3, 34.4(d), 41.4 ...).")
art("E046", "Ball size appears to change from 8 3/4 to 8 13/16 inches: the 2000 text's '8 3/4 in' is an AI clean-up slip; the lower size limit has been 8 13/16 in/22.4 cm throughout.",
    "The raw OCR of the 2000 edition has no matching figure; MCC's own 4th edition (2010) text gives 8 13/16 in/22.4 cm, as do the 1947 and 1980 Codes.", sub="cleaning_artefact_numeric", ev=["S17", "S01", "S11"], conf="high", integrity="suspect")
art("E047", "Women's and junior ball specifications appear to change (e.g. women's weight '4 7/8 to 5 5/8 oz' becomes '4 15/16 to 5 5/16 oz'): not real. The 2000 text's fractions are wrong; the 2008 values (4 15/16 oz = 140 g; 5 5/16 oz = 151 g) are consistent with the gram figures given in both editions.",
    "The 2000 text pairs '4 7/8 oz' with '140 g', but 140 g is 4 15/16 oz; the same internal inconsistency does not occur in the 2008 text.", sub="cleaning_artefact_numeric", ev=["S17", "S01"], conf="medium", integrity="suspect")
art("E050", "Bails projection '1/2 inch' written as '1/2' instead of the glyph: notation only.", "Same value, different fraction notation.", sub="format_artefact", conf="high")
art("E051", "Wicket bail/spigot specification: the 2000 text lists 'Overall length:- Length of barrel:- Longer spigot:- Shorter spigot:-' with no figures next to them; the 2008 text gives them (4 5/16, 2 1/8, 1 3/8, 13/16 in).",
    "Table-layout displacement: raw and processed 2000 both carry the figures, displaced into the next table block (raw/2000_raw.txt l.697-727); they were not lost. The 4th edition (2010) text has the same specification.", ev=["S18", "S01"], conf="medium")
