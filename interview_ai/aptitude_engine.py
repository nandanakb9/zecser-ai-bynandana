REASONING_QUESTIONS = [
    "If a project deadline is suddenly reduced, how would you handle it?",
    "Describe a time you solved a difficult problem.",
    "How would you prioritize multiple urgent tasks?"
]

SCENARIO_QUESTIONS = [
    "Your teammate is not contributing. What will you do?",
    "Client changes requirements at last minute. How do you react?",
    "You made a mistake in work. How will you handle it?"
]
IDEAL_KEYWORDS = [
    "analyze",
    "plan",
    "discuss",
    "prioritize",
    "solution",
    "evaluate",
    "communicate",
    "resolve"
]
def logical_reasoning_score(answer):

    score = 0
    words = answer.lower().split()

    for keyword in IDEAL_KEYWORDS:
        if keyword in words:
            score += 1

    normalized = min(score / len(IDEAL_KEYWORDS), 1.0)

    return round(normalized * 100, 2)
def problem_solving_clarity(answer):

    if len(answer.split()) > 15:
        return 100

    if len(answer.split()) > 8:
        return 75

    if len(answer.split()) > 4:
        return 50

    return 30
def scenario_score(answer):

    logic = logical_reasoning_score(answer)
    clarity = problem_solving_clarity(answer)

    final = (logic * 0.6) + (clarity * 0.4)

    return round(final, 2)
def aptitude_evaluation(answer):

    return {
        "logical_reasoning": logical_reasoning_score(answer),
        "problem_solving_clarity": problem_solving_clarity(answer),
        "scenario_score": scenario_score(answer)
    }