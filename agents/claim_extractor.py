from models.nlp_model import get_nlp_model

nlp = get_nlp_model()

ESG_KEYWORDS = [
    "emissions", "carbon", "energy", "sustainability",
    "climate", "water", "waste", "renewable",
    "biodiversity", "recycle", "deforestation"
]

CLAIM_VERBS = [
    "reduce", "reduced", "increase", "increased",
    "achieve", "achieved", "target", "commit",
    "committed", "invest", "invested", "improve",
    "improved", "eliminate", "eliminated"
]


def extract_claims(text):

    doc = nlp(text)
    claims = []

    for sent in doc.sents:

        sentence = sent.text.strip().lower()

        # ignore short sentences (likely headings)
        if len(sentence.split()) < 8:
            continue

        if (
            any(keyword in sentence for keyword in ESG_KEYWORDS)
            and any(verb in sentence for verb in CLAIM_VERBS)
        ):
            claims.append(sent.text.strip())

    return claims