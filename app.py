import json
from utils.document_loader import load_document
from pipeline.esg_pipeline import run_esg_analysis

def save_report(report):

    with open("reports/esg_report.json", "w") as f:
        json.dump(report, f, indent=4)

    print("\nReport saved to reports/esg_report.json")


def display_report(report):

    print("\n==============================")
    print(" ESG GREENWASHING ANALYSIS")
    print("==============================\n")

    print(f"Total Claims: {report['total_claims']}")
    print(f"Unverifiable Claims: {report['unverifiable_claims']}")
    print(f"Claims Without Evidence: {report['claims_without_evidence']}")
    print(f"Contradictions: {report['contradictions']}\n")

    print("Greenwashing Risk Score:", report["risk_score"])
    print("Risk Level:", report["risk_level"], "\n")

    print("Flagged Claims:")
    for claim in report["flagged_claims"]:
        print("-", claim)


file_path = input("Enter document path: ")

text = load_document(file_path)

report = run_esg_analysis(text)

display_report(report)
save_report(report)