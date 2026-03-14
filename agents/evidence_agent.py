import re

EVIDENCE_KEYWORDS = [
    "report",
    "audit",
    "verified",
    "third-party",
    "assurance",
    "certified",
    "data",
    "study"
]


def check_evidence(claim, document_text):

    claim_words = claim.lower().split()

    for keyword in EVIDENCE_KEYWORDS:

        if keyword in claim.lower():
            return "EVIDENCE_PRESENT"

    # search in whole document
    for keyword in EVIDENCE_KEYWORDS:

        if keyword in document_text.lower():
            return "LIKELY_EVIDENCE"

    return "NO_EVIDENCE"