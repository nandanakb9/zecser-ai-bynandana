from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def generate_embedding(text: str):
    """
    Dummy embedding generator (simulation)
    """
    np.random.seed(len(text))
    return np.random.rand(1, 300)

def semantic_similarity(text1: str, text2: str):
    emb1 = generate_embedding(text1)
    emb2 = generate_embedding(text2)
    score = cosine_similarity(emb1, emb2)[0][0]
    return round(float(score), 2)