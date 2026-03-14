def calculate_risk_score(claims, verifiability_results, contradictions):
    """
    Calculate greenwashing risk score
    """

    total_claims = len(claims)

    unverifiable_count = sum(
        1 for status in verifiability_results if status == "UNVERIFIABLE"
    )

    contradiction_count = len(contradictions)

    # scoring logic
    risk_score = 0

    risk_score += unverifiable_count * 25
    risk_score += contradiction_count * 40

    # normalize score
    risk_score = min(risk_score, 100)

    if risk_score >= 70:
        risk_level = "HIGH"
    elif risk_score >= 40:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    return {
        "total_claims": total_claims,
        "unverifiable_claims": unverifiable_count,
        "contradictions": contradiction_count,
        "risk_score": risk_score,
        "risk_level": risk_level,
    }