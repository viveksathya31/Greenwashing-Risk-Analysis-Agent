import spacy

# Load NLP model
nlp = spacy.load("en_core_web_sm")

# ESG keywords
ESG_KEYWORDS = [
    "carbon",
    "emission",
    "sustainability",
    "renewable",
    "energy",
    "climate",
    "net zero",
    "environment",
    "water",
    "waste"
]

def extract_claims(text):
    """
    Extract ESG-related claims from text
    """

    doc = nlp(text)
    claims = []

    for sent in doc.sents:
        sentence = sent.text.strip()

        if any(keyword in sentence.lower() for keyword in ESG_KEYWORDS):
            claims.append(sentence)

    return claims