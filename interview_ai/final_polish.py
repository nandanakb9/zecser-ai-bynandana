from datetime import datetime


# 🔹 Normalize scores
def normalize_score(score):

    if score < 0:
        return 0

    if score > 100:
        return 100

    return round(score, 2)


# 🔹 Improve score consistency
def improve_scoring_consistency(scores):

    fixed_scores = {}

    for key, value in scores.items():
        fixed_scores[key] = normalize_score(value)

    avg = sum(fixed_scores.values()) / len(fixed_scores)

    # Reduce major fluctuations
    for key in fixed_scores:

        if fixed_scores[key] < avg - 35:
            fixed_scores[key] += 10

    return fixed_scores


# 🔹 Improve recruiter readability
def recruiter_readable_output(candidate):

    return {
        "Candidate": candidate["candidate"],
        "Role": candidate["role"],
        "ATS Score": candidate["scores"]["ats"],
        "HR Score": candidate["scores"]["hr"],
        "Technical Score": candidate["scores"]["technical"],
        "Final Decision": candidate["decision"],
        "Hiring Strength": f"{candidate['hiring_fit_percentage']}%"
    }


# 🔹 Improve report clarity
def generate_clear_report(candidate):

    report = f"""
=============================
Zecpath AI Hiring Report
=============================

Candidate Name : {candidate['candidate']}
Applied Role   : {candidate['role']}

ATS Score      : {candidate['scores']['ats']}
Screening      : {candidate['scores']['screening']}
HR Interview   : {candidate['scores']['hr']}
Technical      : {candidate['scores']['technical']}
Machine Test   : {candidate['scores']['machine_test']}

Hiring Fit     : {candidate['hiring_fit_percentage']}%
Decision       : {candidate['decision']}

Generated At   : {datetime.now()}

=============================
"""

    return report


# 🔹 Improve usability
def usability_fixes():

    return {
        "dashboard_readability": True,
        "clean_reports": True,
        "simplified_outputs": True,
        "consistent_scoring": True
    }


# 🔹 Better error handling
def enhanced_error_handling(data):

    errors = []

    required = [
        "candidate",
        "role",
        "scores",
        "decision"
    ]

    for field in required:

        if field not in data:
            errors.append(f"Missing field: {field}")

    return {
        "errors_found": len(errors),
        "errors": errors
    }


# 🔹 Final production-ready pipeline
def production_ready_output(candidate):

    candidate["scores"] = improve_scoring_consistency(
        candidate["scores"]
    )

    candidate["hiring_fit_percentage"] = normalize_score(
        candidate["hiring_fit_percentage"]
    )

    recruiter_output = recruiter_readable_output(candidate)

    report = generate_clear_report(candidate)

    usability = usability_fixes()

    validation = enhanced_error_handling(candidate)

    return {
        "recruiter_output": recruiter_output,
        "report": report,
        "usability": usability,
        "validation": validation,
        "status": "Production-ready output generated"
    }