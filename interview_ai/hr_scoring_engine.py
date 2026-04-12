def answer_relevance_score(answer):

    if len(answer.split()) > 8:
        return 1.0

    if len(answer.split()) > 4:
        return 0.7

    return 0.4
def consistency_score(answers):

    if len(answers) < 2:
        return 1.0

    repeated = 0

    for i in range(len(answers) - 1):
        if answers[i] == answers[i + 1]:
            repeated += 1

    score = 1 - (repeated / len(answers))

    return max(score, 0.5)
WEIGHTS = {
    "relevance": 0.30,
    "communication": 0.25,
    "confidence": 0.25,
    "consistency": 0.20
}
def calculate_hr_score(answers, communication_scores, confidence_scores):

    relevance_scores = [answer_relevance_score(a) for a in answers]

    relevance = sum(relevance_scores) / len(relevance_scores)
    communication = sum(communication_scores) / len(communication_scores) / 100
    confidence = sum(confidence_scores) / len(confidence_scores) / 100
    consistency = consistency_score(answers)

    final_score = (
        relevance * WEIGHTS["relevance"] +
        communication * WEIGHTS["communication"] +
        confidence * WEIGHTS["confidence"] +
        consistency * WEIGHTS["consistency"]
    )

    return round(final_score * 100, 2)
def hr_score_report(answers, communication_scores, confidence_scores):

    relevance_scores = [answer_relevance_score(a) for a in answers]

    relevance = sum(relevance_scores) / len(relevance_scores)
    communication = sum(communication_scores) / len(communication_scores)
    confidence = sum(confidence_scores) / len(confidence_scores)
    consistency = consistency_score(answers) * 100

    final = calculate_hr_score(answers, communication_scores, confidence_scores)

    return {
        "relevance": round(relevance * 100, 2),
        "communication": round(communication, 2),
        "confidence": round(confidence, 2),
        "consistency": round(consistency, 2),
        "final_hr_score": final
    }