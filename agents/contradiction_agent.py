from transformers import pipeline

nli = pipeline("text-classification", model="facebook/bart-large-mnli")


def detect_contradictions(claims):

    contradictions = []

    for i in range(len(claims)):
        for j in range(i + 1, len(claims)):

            pair = claims[i] + " </s> " + claims[j]

            result = nli(pair)

            label = result[0]["label"]

            if label == "CONTRADICTION":
                contradictions.append((claims[i], claims[j]))

    return contradictions