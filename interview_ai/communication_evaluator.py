import re


def detect_filler_words(text):

    fillers = ["um", "uh", "like", "you know", "basically", "actually"]

    count = 0
    for f in fillers:
        count += text.lower().count(f)

    return count


def measure_fluency(text):

    sentences = re.split(r'[.!?]', text)
    sentences = [s for s in sentences if s.strip()]

    if len(sentences) == 0:
        return 0

    avg_len = sum(len(s.split()) for s in sentences) / len(sentences)

    return min(avg_len / 15, 1.0)
def measure_grammar(text):

    words = text.split()

    if len(words) < 3:
        return 0.4

    capital = text[0].isupper()
    proper_end = text.strip().endswith((".", "!"))

    score = 0.5

    if capital:
        score += 0.25
    if proper_end:
        score += 0.25

    return score
def measure_vocabulary(text):

    words = text.lower().split()
    unique = len(set(words))

    if len(words) == 0:
        return 0

    ratio = unique / len(words)

    return min(ratio, 1.0)
def measure_clarity(text):

    if len(text.split()) > 6:
        return 1.0

    if len(text.split()) > 3:
        return 0.7

    return 0.4
def measure_structure(text):

    if "because" in text.lower() or "for example" in text.lower():
        return 1.0

    if len(text.split()) > 5:
        return 0.7

    return 0.4
def communication_score(text):

    fluency = measure_fluency(text)
    grammar = measure_grammar(text)
    vocab = measure_vocabulary(text)
    clarity = measure_clarity(text)
    structure = measure_structure(text)

    fillers = detect_filler_words(text)

    filler_penalty = min(fillers * 0.05, 0.2)

    score = (
        fluency +
        grammar +
        vocab +
        clarity +
        structure
    ) / 5

    score = score - filler_penalty

    return round(score * 100, 2)