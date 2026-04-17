# Day 50 – Machine Test AI Design

TASK_TYPES = [
    "coding",
    "debugging",
    "file_task",
    "system_design"
]


SCORING_WEIGHTS = {
    "correctness": 0.35,
    "efficiency": 0.25,
    "code_quality": 0.20,
    "problem_solving": 0.20
}


TIME_LIMITS = {
    "coding": 30,
    "debugging": 20,
    "file_task": 25,
    "system_design": 40
}


def evaluate_correctness(passed, total):

    if total == 0:
        return 0

    return (passed / total) * 100


def evaluate_efficiency(time_taken, task_type):

    limit = TIME_LIMITS.get(task_type, 30)

    if time_taken <= limit:
        return 100
    else:
        penalty = ((time_taken - limit) / limit) * 100
        return max(100 - penalty, 20)


def evaluate_code_quality(code):

    lines = len(code.split("\n"))
    comments = code.count("#")

    score = 70

    if comments > 0:
        score += 10

    if lines < 50:
        score += 10

    return min(score, 100)


def evaluate_problem_solving(approach):

    keywords = ["optimize", "edge", "test", "logic", "handle"]

    score = 0

    for word in keywords:
        if word in approach.lower():
            score += 1

    return (score / len(keywords)) * 100


def time_score(time_taken, task_type):

    limit = TIME_LIMITS.get(task_type, 30)

    return max(100 - (time_taken / limit) * 50, 50)


def machine_test_score(task_type, passed, total, time_taken, code, approach):

    correctness = evaluate_correctness(passed, total)
    efficiency = evaluate_efficiency(time_taken, task_type)
    code_quality = evaluate_code_quality(code)
    problem_solving = evaluate_problem_solving(approach)

    final_score = (
        correctness * SCORING_WEIGHTS["correctness"] +
        efficiency * SCORING_WEIGHTS["efficiency"] +
        code_quality * SCORING_WEIGHTS["code_quality"] +
        problem_solving * SCORING_WEIGHTS["problem_solving"]
    )

    return {
        "task_type": task_type,
        "correctness": round(correctness, 2),
        "efficiency": round(efficiency, 2),
        "code_quality": round(code_quality, 2),
        "problem_solving": round(problem_solving, 2),
        "final_score": round(final_score, 2)
    }


def machine_test_report(candidate, data):

    score = machine_test_score(
        data["task_type"],
        data["passed"],
        data["total"],
        data["time_taken"],
        data["code"],
        data["approach"]
    )

    return {
        "candidate": candidate,
        "evaluation": score,
        "verdict": "Pass" if score["final_score"] > 70 else "Needs Improvement"
    }