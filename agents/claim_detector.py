from transformers import pipeline
import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')

classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)


def is_esg_claim(sentence):

    labels = [
        "environmental sustainability claim",
        "social responsibility claim",
        "corporate governance claim",
        "not a sustainability claim"
    ]

    result = classifier(sentence, labels)

    top_label = result["labels"][0]

    if top_label != "not a sustainability claim":
        return True

    return False


def extract_esg_claims(text):

    sentences = sent_tokenize(text)

    claims = []

    for sentence in sentences:

        if len(sentence) < 40:
            continue

        if is_esg_claim(sentence):
            claims.append(sentence)

    return claims