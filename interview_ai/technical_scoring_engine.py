# Day 47 – Technical Skill Scoring Model

import math


SCORING_WEIGHTS = {
    "accuracy": 0.30,
    "depth": 0.25,
    "reasoning": 0.25,
    "applicability": 0.20
}


DIFFICULTY_MULTIPLIER = {
    "easy": 1.0,
    "medium": 1.1,
    "hard": 1.25,
    "system_design": 1.4
}


def detect_depth(answer):

    keywords = ["because", "architecture", "performance", "scalability", "tradeoff"]

    score = 0
    for word in keywords:
        if word in answer.lower():
            score += 1

    return min(score / len(keywords) * 100, 100)


def detect_reasoning(answer):

    reasoning_words = ["if", "then", "else", "therefore", "so"]

    score = 0
    for word in reasoning_words:
        if word in answer.lower():
            score += 1

    return min(score / len(reasoning_words) * 100, 100)


def detect_applicability(answer):

    real_world_words = ["production", "real", "project", "client", "deploy"]

    score = 0
    for word in real_world_words:
        if word in answer.lower():
            score += 1

    return min(score / len(real_world_words) * 100, 100)


def detect_accuracy(answer):

    if len(answer.split()) > 5:
        return 80
    elif len(answer.split()) > 2:
        return 60
    else:
        return 30


def detect_shallow(answer):

    return len(answer.split()) < 5


def normalize_score(score, difficulty):

    multiplier = DIFFICULTY_MULTIPLIER.get(difficulty, 1)
    return min(score * multiplier, 100)


def technical_score(answer, difficulty):

    accuracy = detect_accuracy(answer)
    depth = detect_depth(answer)
    reasoning = detect_reasoning(answer)
    applicability = detect_applicability(answer)

    weighted_score = (
        accuracy * SCORING_WEIGHTS["accuracy"] +
        depth * SCORING_WEIGHTS["depth"] +
        reasoning * SCORING_WEIGHTS["reasoning"] +
        applicability * SCORING_WEIGHTS["applicability"]
    )

    final_score = normalize_score(weighted_score, difficulty)

    return {
        "accuracy": round(accuracy, 2),
        "depth": round(depth, 2),
        "reasoning": round(reasoning, 2),
        "applicability": round(applicability, 2),
        "final_score": round(final_score, 2),
        "shallow": detect_shallow(answer)
    }


def technical_evaluation_report(answer, difficulty):

    score = technical_score(answer, difficulty)

    return {
        "answer": answer,
        "difficulty": difficulty,
        "evaluation": score,
        "verdict": "Strong" if score["final_score"] > 75 else "Average"
    }