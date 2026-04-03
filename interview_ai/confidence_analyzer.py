def detect_hesitation(text):

    hesitation_words = ["um", "uh", "hmm", "..."]

    for w in hesitation_words:
        if w in text.lower():
            return True

    return False


def detect_uncertainty(text):

    uncertain = ["maybe", "not sure", "i think", "possibly", "depends"]

    for u in uncertain:
        if u in text.lower():
            return True

    return False
def detect_repetition(text):

    words = text.lower().split()

    for i in range(len(words) - 1):
        if words[i] == words[i + 1]:
            return True

    return False
def sentiment_score(text):

    positive = ["achieved", "improved", "success", "led", "confident"]
    negative = ["difficult", "problem", "failed", "stress", "issue"]

    score = 0

    for p in positive:
        if p in text.lower():
            score += 1

    for n in negative:
        if n in text.lower():
            score -= 1

    if score > 0:
        return "positive"
    if score < 0:
        return "negative"

    return "neutral"
def detect_contradiction(text):

    if "but" in text.lower() and "however" in text.lower():
        return True

    return False
def stress_indicator(text):

    stress_words = ["pressure", "stress", "overwhelmed", "difficult"]

    for s in stress_words:
        if s in text.lower():
            return True

    return False
def confidence_score(text):

    score = 1.0

    if detect_hesitation(text):
        score -= 0.2

    if detect_uncertainty(text):
        score -= 0.2

    if detect_repetition(text):
        score -= 0.1

    if stress_indicator(text):
        score -= 0.2

    if detect_contradiction(text):
        score -= 0.1

    sentiment = sentiment_score(text)

    if sentiment == "positive":
        score += 0.1
    elif sentiment == "negative":
        score -= 0.1

    score = max(min(score, 1.0), 0)

    return round(score * 100, 2)