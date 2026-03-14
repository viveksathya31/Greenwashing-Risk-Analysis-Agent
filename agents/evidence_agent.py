EVIDENCE_KEYWORDS = [
    "report",
    "study",
    "data",
    "analysis",
    "source",
    "according to",
    "research"
]


def check_evidence(claim):
    """
    Detect if claim references evidence
    """

    claim_lower = claim.lower()

    if any(word in claim_lower for word in EVIDENCE_KEYWORDS):
        return "EVIDENCE_PRESENT"

    return "NO_EVIDENCE"