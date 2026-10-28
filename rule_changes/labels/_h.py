"""Helper for hand-written event labels. One module per edition pair in rule_changes/labels/."""


def make(pair):
    labels = []

    def L(event, what, cat, sub, conf, basis, why, ev, sec="", secsub="", date="", integrity="ok", note=""):
        """event: 'E003' (this module's pair). cat/sub from schema/taxonomy_v0.json; basis one of
        stated, inferred, conjecture, attributed, derived, none; ev: list of source ids (data/evidence/sources.csv);
        date: dating evidence for when the change was made; integrity: ok | suspect (source text doubtful)."""
        labels.append(dict(pair=pair, event=event, what_changed=what, category=cat, subtype=sub, confidence=conf,
                           basis=basis, rationale=why, evidence=ev, secondary_category=sec, secondary_subtype=secsub,
                           date_evidence=date, integrity=integrity, notes=note))

    return L, labels
