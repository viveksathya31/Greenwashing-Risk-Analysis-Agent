from utils.text_preprocessing import preprocess_text
from agents.claim_extractor import extract_claims
from agents.verifiability_agent import check_verifiability
from agents.evidence_agent import check_evidence
from agents.contradiction_agent import detect_contradictions
from agents.risk_scoring_agent import calculate_risk_score
from agents.report_agent import generate_report


def run_esg_analysis(text):

    clean_text = preprocess_text(text)

    claims = extract_claims(clean_text)

    verifiability_results = []
    evidence_results = []

    for claim in claims:

        verifiability_results.append(check_verifiability(claim))
        evidence_results.append(check_evidence(claim))

    contradictions = detect_contradictions(claims)

    risk_report = calculate_risk_score(
        claims,
        verifiability_results,
        contradictions
    )

    report = generate_report(
        claims,
        verifiability_results,
        evidence_results,
        contradictions,
        risk_report
    )

    return report