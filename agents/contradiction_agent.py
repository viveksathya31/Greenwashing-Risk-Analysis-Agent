from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


def detect_contradictions(claims, threshold=0.75):
    """
    Detect potential contradictions between ESG claims.
    """

    contradictions = []

    if len(claims) < 2:
        return contradictions

    embeddings = model.encode(claims)

    for i in range(len(claims)):
        for j in range(i + 1, len(claims)):

            similarity = cosine_similarity(
                [embeddings[i]], [embeddings[j]]
            )[0][0]

            # If claims are very similar but contain different numbers → possible contradiction
            if similarity > threshold:

                numbers_i = set(filter(str.isdigit, claims[i]))
                numbers_j = set(filter(str.isdigit, claims[j]))

                if numbers_i != numbers_j:
                    contradictions.append((claims[i], claims[j]))

    return contradictions