from models.embedding_model import get_embedding_model
from sklearn.metrics.pairwise import cosine_similarity

model = get_embedding_model()


def detect_contradictions(claims, threshold=0.75):

    contradictions = []

    if len(claims) < 2:
        return contradictions

    embeddings = model.encode(claims)

    for i in range(len(claims)):
        for j in range(i + 1, len(claims)):

            similarity = cosine_similarity(
                [embeddings[i]], [embeddings[j]]
            )[0][0]

            if similarity > threshold:

                numbers_i = set(filter(str.isdigit, claims[i]))
                numbers_j = set(filter(str.isdigit, claims[j]))

                if numbers_i != numbers_j:
                    contradictions.append((claims[i], claims[j]))

    return contradictions