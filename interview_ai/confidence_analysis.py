def detect_hesitation(answer):

    hesitation_words = ["um", "uh", "maybe", "not sure", "i think"]

    for word in hesitation_words:
        if word in answer.lower():
            return True

    return False


def response_length(answer):

    words = len(answer.split())

    if words < 3:
        return "short"

    if words < 10:
        return "medium"

    return "long"

def response_pace(answer):

    words = len(answer.split())

    if words < 4:
        return "fast"

    if words < 12:
        return "normal"

    return "slow"
def sentiment_score(answer):

    positive = ["yes", "confident", "experienced", "skilled", "comfortable"]
    negative = ["no", "not", "don't", "lack", "weak"]

    pos = sum(1 for w in positive if w in answer.lower())
    neg = sum(1 for w in negative if w in answer.lower())

    if pos > neg:
        return "positive"

    if neg > pos:
        return "negative"

    return "neutral"
def detect_uncertainty(answer):

    uncertainty_words = ["maybe", "depends", "not sure", "approximately"]

    for word in uncertainty_words:
        if word in answer.lower():
            return True

    return False
def communication_strength(answer):

    hesitation = detect_hesitation(answer)
    uncertainty = detect_uncertainty(answer)
    sentiment = sentiment_score(answer)

    score = 1.0

    if hesitation:
        score -= 0.2

    if uncertainty:
        score -= 0.2

    if sentiment == "negative":
        score -= 0.2

    return round(score, 2)
def analyze_behavior(answer):

    return {
        "hesitation": detect_hesitation(answer),
        "length": response_length(answer),
        "pace": response_pace(answer),
        "sentiment": sentiment_score(answer),
        "uncertainty": detect_uncertainty(answer),
        "communication_score": communication_strength(answer)
    }