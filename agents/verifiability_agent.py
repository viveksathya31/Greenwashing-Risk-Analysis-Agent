import re

# words that usually indicate measurable claims
METRIC_KEYWORDS = [
    "%",
    "percent",
    "tons",
    "tonnes",
    "kg",
    "kwh",
    "mw",
    "million",
    "billion",
    "year",
    "since",
    "by",
    "target",
]

def check_verifiability(claim):
    """
    Determines whether an ESG claim is verifiable.
    """

    claim_lower = claim.lower()

    # Check if numbers exist
    numbers = re.findall(r"\d+", claim)

    # Check metric keywords
    has_metric = any(metric in claim_lower for metric in METRIC_KEYWORDS)

    if numbers and has_metric:
        return "VERIFIABLE"

    if numbers:
        return "LIKELY_VERIFIABLE"

    return "UNVERIFIABLE"