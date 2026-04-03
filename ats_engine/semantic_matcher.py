from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')


def get_embedding(text):
    """
    Convert text into embedding vector
    """
    if not text:
        text = ""
    return model.encode([text])[0]


def compute_similarity(text1, text2):
    """
    Compute cosine similarity between two texts
    """
    emb1 = get_embedding(text1)
    emb2 = get_embedding(text2)

    score = cosine_similarity(
        [emb1],
        [emb2]
    )[0][0]

    return float(score)


def section_similarity(resume_sections, jd_text):
    """
    Compute similarity for each resume section
    """
    scores = {}

    for section, content in resume_sections.items():

        if isinstance(content, list):
            content = " ".join(content)

        scores[section] = compute_similarity(content, jd_text)

    return scores


SECTION_WEIGHTS = {
    "skills": 0.4,
    "experience": 0.3,
    "projects": 0.2,
    "education": 0.1
}


def semantic_match_score(resume_sections, jd_text):
    """
    Calculate weighted semantic match score
    """
    scores = section_similarity(resume_sections, jd_text)

    final_score = 0

    for section, weight in SECTION_WEIGHTS.items():
        if section in scores:
            final_score += scores[section] * weight

    return round(final_score, 3)


def match_label(score):
    if score >= 0.75:
        return "Strong Match"
    elif score >= 0.55:
        return "Good Match"
    elif score >= 0.35:
        return "Moderate Match"
    else:
        return "Low Match"