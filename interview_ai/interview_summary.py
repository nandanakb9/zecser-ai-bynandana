def generate_strengths(communication, confidence, aptitude):

    strengths = []

    if communication > 75:
        strengths.append("Strong communication skills")

    if confidence > 75:
        strengths.append("Confident responses")

    if aptitude > 70:
        strengths.append("Good logical thinking ability")

    return strengths
def generate_weaknesses(communication, confidence, aptitude):

    weaknesses = []

    if communication < 60:
        weaknesses.append("Needs improvement in communication")

    if confidence < 60:
        weaknesses.append("Low confidence indicators")

    if aptitude < 60:
        weaknesses.append("Limited problem-solving clarity")

    return weaknesses
def cultural_fit(confidence, consistency):

    fit = []

    if confidence > 70:
        fit.append("Positive attitude")

    if consistency > 70:
        fit.append("Consistent responses")

    return fit
def risk_flags(confidence, inconsistencies):

    risks = []

    if confidence < 50:
        risks.append("Low confidence risk")

    if inconsistencies:
        risks.append("Response inconsistency detected")

    return risks
def overall_summary(score):

    if score > 80:
        return "Candidate demonstrates strong HR interview performance."

    if score > 60:
        return "Candidate shows moderate HR interview performance."

    return "Candidate performance requires improvement."
def interview_report(data):

    strengths = generate_strengths(
        data["communication"],
        data["confidence"],
        data["aptitude"]
    )

    weaknesses = generate_weaknesses(
        data["communication"],
        data["confidence"],
        data["aptitude"]
    )

    fit = cultural_fit(
        data["confidence"],
        data["consistency"]
    )

    risks = risk_flags(
        data["confidence"],
        data["inconsistencies"]
    )

    summary = overall_summary(data["final_score"])

    return {
        "strengths": strengths,
        "weaknesses": weaknesses,
        "cultural_fit": fit,
        "risk_flags": risks,
        "overall_summary": summary
    }