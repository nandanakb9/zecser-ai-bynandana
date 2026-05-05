import os
import random
from datetime import datetime

# Simulated modules (replace later with real integrations if needed)

def ats_score():
    return random.randint(60, 95)

def screening_score():
    return random.randint(55, 90)

def hr_score():
    return random.randint(60, 95)

def technical_score():
    return random.randint(50, 95)

def machine_test_score():
    return random.randint(50, 100)


# 🔹 Decision Logic
def final_decision(score):
    if score >= 80:
        return "Selected"
    elif score >= 65:
        return "Consider"
    return "Rejected"


# 🔹 Hiring Fit Calculation
def calculate_hiring_fit(scores):
    weights = {
        "ats": 0.15,
        "screening": 0.2,
        "hr": 0.2,
        "technical": 0.25,
        "machine_test": 0.2
    }

    final = (
        scores["ats"] * weights["ats"] +
        scores["screening"] * weights["screening"] +
        scores["hr"] * weights["hr"] +
        scores["technical"] * weights["technical"] +
        scores["machine_test"] * weights["machine_test"]
    )

    return round(final, 2)


# 🔹 Full Pipeline Simulation
def run_full_simulation(resume_folder, jd_folder):

    resumes = os.listdir(resume_folder)
    jds = os.listdir(jd_folder)

    results = []

    for resume in resumes:

        candidate_name = resume.replace(".pdf", "")

        # Assign random job role
        role = random.choice(jds).replace(".pdf", "")

        scores = {
            "ats": ats_score(),
            "screening": screening_score(),
            "hr": hr_score(),
            "technical": technical_score(),
            "machine_test": machine_test_score()
        }

        hiring_fit = calculate_hiring_fit(scores)

        decision = final_decision(hiring_fit)

        result = {
            "candidate": candidate_name,
            "role": role,
            "scores": scores,
            "hiring_fit_percentage": hiring_fit,
            "decision": decision,
            "timestamp": str(datetime.now())
        }

        results.append(result)

    return results


# 🔹 Performance Analysis
def analyze_performance(results):

    selected = [r for r in results if r["decision"] == "Selected"]
    rejected = [r for r in results if r["decision"] == "Rejected"]
    consider = [r for r in results if r["decision"] == "Consider"]

    analysis = {
        "total_candidates": len(results),
        "selected": len(selected),
        "consider": len(consider),
        "rejected": len(rejected),
        "selection_rate": round(len(selected) / len(results) * 100, 2)
    }

    return analysis


# 🔹 Improvement Suggestions
def generate_improvements(results):

    suggestions = []

    for r in results:
        if r["scores"]["technical"] < 60:
            suggestions.append("Improve technical evaluation accuracy")

        if r["scores"]["hr"] < 60:
            suggestions.append("Improve HR communication scoring")

    if not suggestions:
        suggestions.append("System performing well")

    return list(set(suggestions))