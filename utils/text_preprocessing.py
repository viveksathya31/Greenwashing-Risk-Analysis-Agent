import re

def preprocess_text(text):
    """
    Clean ESG text before analysis
    """

    # remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    # remove special characters except punctuation
    text = re.sub(r'[^a-zA-Z0-9.,% ]', '', text)

    # normalize
    text = text.strip()

    return text