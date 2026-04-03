def normalize_scores(scores):
    """
    Normalize scores between 0 and 1
    """
    if not scores:
        return scores

    min_score = min(scores)
    max_score = max(scores)

    if max_score - min_score == 0:
        return scores

    normalized = [
        (s - min_score) / (max_score - min_score)
        for s in scores
    ]

    return normalized


def apply_fairness_adjustment(score):
    """
    Slight smoothing to reduce extreme bias
    """
    return round((score * 0.9) + 0.05, 3)