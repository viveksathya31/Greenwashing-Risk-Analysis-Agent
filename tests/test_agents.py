import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.text_preprocessing import preprocess_text
from agents.claim_extractor import extract_claims
from agents.verifiability_agent import check_verifiability
from agents.contradiction_agent import detect_contradictions
from agents.evidence_agent import check_evidence
from agents.risk_scoring_agent import calculate_risk_score
from agents.report_agent import generate_report


text = """
Our company reduced carbon emissions by 30% in 2023 according to the 2023 sustainability report.
We strongly support sustainability initiatives.
We became carbon neutral in 2022.
We plan to become carbon neutral by 2030.
"""

# 1️⃣ Text Processing
clean_text = preprocess_text(text)

# 2️⃣ Claim Extraction
claims = extract_claims(clean_text)

verifiability_results = []
evidence_results = []

# 3️⃣ Verifiability + Evidence
for claim in claims:

    verifiability_results.append(check_verifiability(claim))
    evidence_results.append(check_evidence(claim))

# 4️⃣ Contradiction Detection
contradictions = detect_contradictions(claims)

# 5️⃣ Risk Score
risk_report = calculate_risk_score(
    claims,
    verifiability_results,
    contradictions
)

# 6️⃣ Generate Final Report
report = generate_report(
    claims,
    verifiability_results,
    evidence_results,
    contradictions,
    risk_report
)

print("\nESG ANALYSIS REPORT\n")

for key, value in report.items():
    print(f"{key}: {value}")