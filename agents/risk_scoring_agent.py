def calculate_risk_score(claims, verifiability, contradictions):

    total = len(claims)

    unverifiable = verifiability.count("UNVERIFIABLE")
    contradiction_count = len(contradictions)

    score = (
        (unverifiable * 2) +
        (contradiction_count * 5)
    ) / max(total, 1) * 100

    score = min(round(score), 100)

    if score < 30:
        level = "LOW"
    elif score < 60:
        level = "MEDIUM"
    else:
        level = "HIGH"

    return {
        "risk_score": score,
        "risk_level": level
    }