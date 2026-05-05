# Day 54 – Optimization & Refinement

def adjust_thresholds(score):
    """
    Improve decision thresholds to reduce false results
    """
    if score >= 80:
        return "high"
    elif score >= 65:
        return "medium"
    else:
        return "low"


def normalize_scores(scores):
    """
    Normalize all scores to ensure consistency
    """
    normalized = {}

    for key, value in scores.items():
        normalized[key] = max(0, min(value, 100))

    return normalized


def detect_anomalies(scores):
    """
    Detect unusual score patterns
    Example: high ATS but very low technical
    """
    anomalies = []

    if scores.get("ats", 0) > 80 and scores.get("technical", 0) < 50:
        anomalies.append("High ATS but low technical performance")

    if scores.get("hr", 0) > 80 and scores.get("behavior", 0) < 50:
        anomalies.append("Good HR score but poor behavioral signals")

    return anomalies


def refine_intent(answer):
    """
    Improved intent detection (fix vague misclassification)
    """
    answer = answer.lower()

    if len(answer.split()) < 3:
        return "unclear"

    if "experience" in answer:
        return "experience"

    if "skill" in answer or "excel" in answer or "python" in answer:
        return "skills"

    if "salary" in answer or "lpa" in answer:
        return "salary"

    if "join" in answer or "available" in answer:
        return "availability"

    return "general"


def optimize_processing(text):
    """
    Faster text cleaning (lightweight)
    """
    return text.lower().strip()


def improve_consistency(scores):
    """
    Smooth score differences across rounds
    """
    avg = sum(scores.values()) / len(scores)

    adjusted = {}
    for k, v in scores.items():
        adjusted[k] = (v + avg) / 2

    return adjusted


def optimize_system(data):
    """
    Main optimization pipeline
    """

    scores = data["scores"]

    # Step 1: normalize
    normalized = normalize_scores(scores)

    # Step 2: detect anomalies
    anomalies = detect_anomalies(normalized)

    # Step 3: consistency improvement
    consistent_scores = improve_consistency(normalized)

    return {
        "normalized_scores": normalized,
        "consistent_scores": consistent_scores,
        "anomalies": anomalies
    }