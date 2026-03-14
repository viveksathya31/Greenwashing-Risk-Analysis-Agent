def generate_report(
    claims,
    verifiability_results,
    evidence_results,
    contradictions,
    risk_report
):
    """
    Generate the final ESG analysis report
    """

    report = {}

    # Basic counts
    report["total_claims"] = len(claims)

    report["unverifiable_claims"] = verifiability_results.count("UNVERIFIABLE")

    report["claims_without_evidence"] = evidence_results.count("NO_EVIDENCE")

    report["contradictions"] = len(contradictions)

    # Risk scoring
    report["risk_score"] = risk_report.get("risk_score", 0)
    report["risk_level"] = risk_report.get("risk_level", "LOW")

    # Detailed flagged claims
    flagged_claims = []

    for i, claim in enumerate(claims):

        reasons = []

        if i < len(verifiability_results):
            if verifiability_results[i] == "UNVERIFIABLE":
                reasons.append("UNVERIFIABLE")

        if i < len(evidence_results):
            if evidence_results[i] == "NO_EVIDENCE":
                reasons.append("NO_EVIDENCE")

        if reasons:
            flagged_claims.append({
                "claim": claim,
                "reason": reasons
            })

    report["flagged_claims"] = flagged_claims

    return report