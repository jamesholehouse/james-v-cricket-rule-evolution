"""Labels for 1774 -> 1785.

Edition note: the dataset's '1774' text is a later printing. Its marks (two bails, the Hit wicket law, the single-wicket 'unless he
returns' clause, the 'subsequent meeting' three-stump note) match Rait Kerr's description of Blake's Maidstone edition c.1786 (App.
III), and the ACS transcription of the 1774 code (S31-02) has none of them. The '1785' text is the Wallis broadsheet of 1 Sept 1785,
which Rait Kerr says reproduces the 1774 code plus a note on the third stump. So most differences in this pair run backwards in time:
they are features of the c.1786 printing that the 1785 text does not yet have, not changes to the Laws between 1774 and 1785."""
from _h import make
PAIR = "1774_1785"
L, LABELS = make(PAIR)
ST, UN, NC, SW = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE", "SEMANTIC_WORDING"
ED = ("Edition artefact: dataset '1774' = later printing (Blake, Maidstone c.1786 by Rait Kerr's description); '1785' = Wallis broadsheet "
      "1 Sept 1785 (1774 code + third-stump note).")
EV = ["S16", "S31-02", "S31-04"]

L("E001",
  "A block of strikers' provisions (L.B.W., crossing, running before delivery, hindering a catch, guarding the wicket, the single-wicket "
  "no-notch rule) appears under a different pseudo-Law. The wording is the same as before, except 'Legs' for 'leg' and 'the Wicket' for "
  "'his wicket' in the L.B.W. rule. The single-wicket rule is printed inside this block without the 'unless he returns to his ground' clause; "
  "that clause is covered by the event removing the separate SINGLE WICKET heading.",
  NC, "segmentation_artefact", "high", "derived",
  "Every provision is in the 1774 text. Pre-1884 texts are segmented by headings, and the Wallis print has no heading where the 1774 printing "
  "had one, so the block counts as a new Law. 'Legs' and 'the Wicket' are Wallis's own readings (raw OCR 1785 line 68). The ACS 1774 text has 'leg' "
  "and 'his wicket'. No rule changed.",
  ["S18", "S31-02"], date=ED)
L("E002",
  "The same five strikers' provisions are moved between pseudo-Laws. They differ only in capitalisation and punctuation, plus 'Legs'/'the "
  "Wicket' in the L.B.W. rule.",
  NC, "segmentation_artefact", "high", "derived",
  "Relocation produced by heading-based segmentation; wording unchanged.", ["S18", "S31-02"], date=ED)
L("E003",
  "Wicket-keeper: 'though the ball hit it' -> 'though the Ball touch it', otherwise identical.",
  NC, "", "medium", "derived",
  "A printer's variant: the 1785 Wallis broadsheet reads 'touch', while the ACS 1774 code and every later edition read 'hit' (raw OCR 1785 line "
  "95 confirms 'touch'). The meaning is unchanged and the 1774 committee was not a standing one (Rait Kerr ch.2), so there was no body to "
  "revise the Law at this point.",
  ["S16", "S31-02", "S31-04"], date=ED, note="Edition/printer variant; no NOT_A_CHANGE subtype fits (proposed: edition_artefact)")
L("E004",
  "Umpires: a sentence is re-split. 'the person hurt shall have his place in any part of that innings' (c.1786 printing) vs 'the Person "
  "hurt, shall have his Hands in any part of that Innings' (1785, the 1774 code's wording). 'the umpire, unasked, must call no ball' -> 'the "
  "Umpires unasked must call No Ball'.",
  NC, "", "medium", "derived",
  "ACS 1774 has 'shall have his hands' and 'the Umpire unasked must call No Ball'. 'his place' is the later printing's reading and "
  "'Umpires' is Wallis's. Neither is a change to the Laws.",
  EV, date=ED, integrity="suspect", note="Edition artefact (proposed subtype edition_artefact)")
L("E005",
  "The separate SINGLE WICKET heading disappears. The rule continues inside the strikers' block without the clause 'unless he returns to his "
  "ground after he has struck the ball'.",
  NC, "", "medium", "derived",
  "The 1774 code (ACS) has the rule without the 'unless he returns' clause. Rait Kerr says Blake's c.1786 edition contains 'a minor alteration "
  "... in a rule for the Single Wicket game'. The clause belongs to the later printing placed at '1774'. Its absence in 1785 is not a repeal.",
  EV, date=ED, integrity="suspect", note="Edition artefact (proposed subtype edition_artefact)")
L("E006",
  "Bets: 'But if the party goes in a second time ... number on the score' -> 'But if the other Party goes in a second Time ... Numbers on "
  "the Score'.",
  NC, "", "medium", "derived",
  "ACS 1774 reads 'if the other party goes in a second time ... number on the score'. The dataset's 1774 printing omitted 'other', and 'Numbers' "
  "is Wallis's variant. No change to the Laws.",
  ["S31-02", "S31-04"], date=ED, note="Edition/printer variant (proposed subtype edition_artefact)")
L("E007",
  "Stumps: the note 'but by a subsequent meeting it is settled for to use three stumps instead of two, to each wicket, and the two bails not "
  "to exceed six inches' (dataset 1774) -> 'N.B. It is lately settled to use three Stumps instead of two to each Wicket, the Ball [Bail] the "
  "same Length as above' (Wallis 1785). The three stumps remain; the second bail disappears.",
  NC, "", "medium", "derived",
  "Rait Kerr App. III quotes the Wallis note as 'the Bail the same length as above'. The processed and raw 1785 'Ball' is a misreading of "
  "'Bail'. Two bails are first recorded c.1786 in the Maidstone edition (serial 36), so the 'two bails' wording comes from that later "
  "printing and its absence in 1785 is not a change. The third stump (serial 34, c.1775) is in both texts; Rait Kerr says the 1785 Wallis "
  "print is the first dated edition to mention it (serial 35).",
  EV, date=ED + " Third stump c.1775 (serials 34-35); two bails c.1786 (serial 36).", integrity="suspect",
  note="Edition artefact plus OCR 'Ball' for 'Bail' in 1785")
L("E008",
  "Bowling crease: capitalisation, hyphenation and the misprint 'parallal'.",
  NC, "format_artefact", "high", "derived", "Same words apart from spelling/capitalisation.", ["S18"])
L("E009",
  "Visiting side's choice: the heading words 'which goes from home' are now inside the provision text; otherwise identical.",
  NC, "segmentation_artefact", "high", "derived", "Heading/body split differs between printings; same wording.", ["S18"])
L("E010",
  "Bowler: capitalisation and punctuation only.",
  NC, "format_artefact", "high", "derived", "Same words.", ["S18"])
L("E011",
  "Striker out: 'If either of the bails are bowled off' (dataset 1774) -> 'If the Bail is bowled off' (1785). Also heading fragment 'is "
  "out', 'strike' -> 'strikes', 'a ball' -> 'the Ball', and the run-out record truncated at 'by' by segmentation.",
  NC, "", "medium", "derived",
  "The 1774 code (ACS) reads 'if the bail is bowled off'. The two-bail wording belongs to the later Maidstone printing (Rait Kerr serial 36, "
  "c.1786, 'references to two bails ... in two places'). The other differences are format.",
  EV, date=ED, integrity="suspect", note="Edition artefact (proposed subtype edition_artefact)")
L("E012",
  "Hit wicket removed: 'If he strikes, or treads down, or falls himself upon his wicket in striking (but not in over-running), its out.' "
  "is absent from the 1785 text.",
  ST, "drafting_omission", "medium", "conjecture",
  "Rait Kerr serial 32a: in the 1774 code 'The \"Hit wicket\" Law disappears temporarily'. He counts it among the 'five omissions from the "
  "previous code which may well have resulted from careless drafting' (ch.2), which is his conjecture. The 1785 Wallis print reproduces the "
  "1774 code (ACS 1774 also has no Hit wicket). The dataset's '1774' printing still has the rule because it is the c.1786 Maidstone edition, "
  "which reintroduced it (serial 37). In the real chronology the omission dates from 25 Feb 1774, not 1774-85.",
  EV, date="Omitted from the 25 Feb 1774 code (serial 32a); restored c.1786 (serial 37) and in the 1788 MCC code (serial 42). " + ED)
L("E013",
  "'Or if the Striker touches or takes up the Ball before it has lain still, unless at the Request of the Opposite [Party]' counted as a new "
  "pseudo-Law (segment truncated).",
  NC, "segmentation_artefact", "high", "derived",
  "The provision is in the 1774 text; its position differs (Rait Kerr notes 'two changes of sequence' in the Maidstone printing).",
  ["S16", "S18"], date=ED)
L("E014",
  "The handling-the-ball provision is moved within the striker-out list; wording unchanged.",
  NC, "segmentation_artefact", "high", "derived", "Change of sequence only.", ["S18"], date=ED)
