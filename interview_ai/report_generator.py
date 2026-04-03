def generate_report(candidate_name, answers, scores, behavior):

    report = {}

    report["candidate"] = candidate_name
    report["summary"] = summarize_answers(answers)
    report["strengths"] = extract_strengths(answers, scores, behavior)
    report["risks"] = extract_risks(answers, scores, behavior)
    report["missing"] = detect_missing(answers)
    report["salary"] = extract_salary(answers)
    report["availability"] = extract_availability(answers)
    report["skill_confirmation"] = extract_skills(answers)

    return report
def summarize_answers(answers):

    return [a["original"] for a in answers[:3]]
def extract_strengths(answers, scores, behavior):

    strengths = []

    for s in scores:
        if s["total_score"] >= 0.7:
            strengths.append("Good response quality")

    for b in behavior:
        if b["communication_score"] >= 0.8:
            strengths.append("Strong communication")

    return list(set(strengths))
def extract_risks(answers, scores, behavior):

    risks = []

    for s in scores:
        if s["total_score"] < 0.5:
            risks.append("Low answer quality")

    for b in behavior:
        if b["communication_score"] < 0.5:
            risks.append("Low confidence")

    return list(set(risks))
def detect_missing(answers):

    missing = []

    for a in answers:
        if a["vague"]:
            missing.append("Incomplete answer")

    return list(set(missing))
def extract_salary(answers):

    for a in answers:
        if a["salary"] != "not_specified":
            return a["salary"]

    return "Not mentioned"
def extract_availability(answers):

    for a in answers:
        if a["availability"] != "unknown":
            return a["availability"]

    return "Not mentioned"
def extract_skills(answers):

    skills = []

    for a in answers:
        skills.extend(a["skills"])

    return list(set(skills))