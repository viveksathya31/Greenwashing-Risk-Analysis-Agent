import spacy

# Load once
nlp = spacy.load("en_core_web_sm")

def get_nlp_model():
    return nlp