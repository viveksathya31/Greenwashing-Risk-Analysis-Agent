
def generate_report(
    claims,
    verifiability_results,
    evidence_results,
    contradictions,
    risk_report
):

    report = {}

    report["total_claims"] = len(claims)

    report["unverifiable_claims"] = sum(
        1 for v in verifiability_results if v == "UNVERIFIABLE"
    )

    report["claims_without_evidence"] = sum(
        1 for e in evidence_results if e == "NO_EVIDENCE"
    )

    report["contradictions"] = len(contradictions)

    report["risk_score"] = risk_report["risk_score"]
    report["risk_level"] = risk_report["risk_level"]

    report["flagged_claims"] = [
        claim
        for claim, v in zip(claims, verifiability_results)
        if v == "UNVERIFIABLE"
    ]

    return report