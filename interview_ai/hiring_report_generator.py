# Day 53 – Hiring Intelligence Report Generator

def generate_strengths(scores, behavior_score, technical_score):
    strengths = []

    if scores.get("ats", 0) > 75:
        strengths.append("Strong resume-job match")

    if scores.get("screening", 0) > 70:
        strengths.append("Good screening performance")

    if scores.get("hr", 0) > 75:
        strengths.append("Strong HR communication")

    if technical_score > 75:
        strengths.append("Good technical knowledge")

    if behavior_score > 80:
        strengths.append("High confidence and clarity")

    return strengths


def generate_weaknesses(scores, behavior_score, technical_score):
    weaknesses = []

    if scores.get("screening", 0) < 60:
        weaknesses.append("Weak screening responses")

    if scores.get("hr", 0) < 60:
        weaknesses.append("Poor communication")

    if technical_score < 60:
        weaknesses.append("Low technical depth")

    if behavior_score < 60:
        weaknesses.append("Low confidence / hesitation")

    return weaknesses


def generate_risks(risk_score):
    risks = []

    if risk_score > 70:
        risks.append("High integrity or behavioral risk")

    elif risk_score > 40:
        risks.append("Moderate risk signals detected")

    return risks


def generate_summary(candidate, decision):
    if decision == "Selected":
        return f"{candidate} is a strong candidate suitable for hiring."

    if decision == "Hold / Review":
        return f"{candidate} requires further evaluation before final decision."

    return f"{candidate} is not recommended based on current evaluation."


def generate_hiring_report(data):
    """
    data should contain:
    - candidate
    - role
    - scores (ats, screening, hr, technical, machine_test)
    - behavior_score
    - risk_score
    - final_decision
    - hiring_fit_percentage
    """

    scores = data["scores"]

    technical_score = scores.get("technical", 0)
    behavior_score = data.get("behavior_score", 100)
    risk_score = data.get("risk_score", 0)

    strengths = generate_strengths(scores, behavior_score, technical_score)
    weaknesses = generate_weaknesses(scores, behavior_score, technical_score)
    risks = generate_risks(risk_score)

    summary = generate_summary(data["candidate"], data["final_decision"])

    report = {
        "candidate": data["candidate"],
        "role": data["role"],

        "scores": {
            "ATS": scores.get("ats"),
            "Screening": scores.get("screening"),
            "HR": scores.get("hr"),
            "Technical": scores.get("technical"),
            "Machine Test": scores.get("machine_test"),
            "Hiring Fit %": data.get("hiring_fit_percentage")
        },

        "analysis": {
            "strengths": strengths,
            "weaknesses": weaknesses,
            "risk_indicators": risks
        },

        "final_decision": data["final_decision"],
        "confidence_score": data.get("confidence_score"),
        "summary": summary
    }

    return report