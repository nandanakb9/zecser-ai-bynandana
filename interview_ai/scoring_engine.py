def score_clarity(answer_obj):

    if answer_obj["vague"]:
        return 0.3

    if len(answer_obj["original"].split()) > 5:
        return 1.0

    return 0.6


def score_relevance(answer_obj):

    if answer_obj["off_topic"]:
        return 0.0

    if answer_obj["intent"] != "general":
        return 1.0

    return 0.5


def score_completeness(answer_obj):

    filled = 0

    if answer_obj["skills"]:
        filled += 1
    if answer_obj["experience"] > 0:
        filled += 1
    if answer_obj["salary"] != "not_specified":
        filled += 1
    if answer_obj["availability"] != "unknown":
        filled += 1

    return filled / 4


def score_consistency(answer_obj):

    if answer_obj["vague"] and answer_obj["off_topic"]:
        return 0.2

    return 1.0


def score_answer(answer_obj):

    clarity = score_clarity(answer_obj)
    relevance = score_relevance(answer_obj)
    completeness = score_completeness(answer_obj)
    consistency = score_consistency(answer_obj)

    total = (clarity + relevance + completeness + consistency) / 4

    return {
        "clarity": clarity,
        "relevance": relevance,
        "completeness": completeness,
        "consistency": consistency,
        "total_score": total   # ⭐ FIXED KEY
    }