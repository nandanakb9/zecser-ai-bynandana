# Day 42 - Optimization & Stability Engine

def clamp_score(score):
    return max(0, min(100, score))


def smooth_score(scores):
    if not scores:
        return 0
    return sum(scores) / len(scores)


def reduce_false_positive(score):
    if score > 90:
        score -= 3
    return score


def reduce_false_negative(score):
    if score < 40:
        score += 5
    return score


def refine_scoring(ats, screening, hr):

    ats = clamp_score(ats)
    screening = clamp_score(screening)
    hr = clamp_score(hr)

    ats = reduce_false_positive(ats)
    screening = reduce_false_positive(screening)
    hr = reduce_false_positive(hr)

    ats = reduce_false_negative(ats)
    screening = reduce_false_negative(screening)
    hr = reduce_false_negative(hr)

    return ats, screening, hr


def stable_followup(answer):

    short_answers = ["ok", "yes", "no", "maybe"]

    if len(answer.split()) < 3 or answer.lower() in short_answers:
        return "Could you provide more details?"

    if "not sure" in answer.lower():
        return "Can you clarify your experience?"

    return None


def fast_text_cleanup(text):

    if not text:
        return ""

    fillers = ["um", "uh", "umm", "like", "you know"]

    words = text.lower().split()
    cleaned = [w for w in words if w not in fillers]

    return " ".join(cleaned)


def normalize_scores(ats, screening, hr):

    ats, screening, hr = refine_scoring(ats, screening, hr)

    final = (ats * 0.3) + (screening * 0.3) + (hr * 0.4)

    return round(final, 2)