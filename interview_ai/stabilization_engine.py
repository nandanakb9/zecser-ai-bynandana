import math


# 🔹 Fix score boundaries
def normalize_score(value):
    if value is None:
        return 0
    return max(0, min(100, value))


# 🔹 Fix inconsistencies across stages
def fix_inconsistent_scores(scores):

    fixed = {}

    for k, v in scores.items():
        fixed[k] = normalize_score(v)

    # 🔹 Example rule: ATS high but technical very low
    if fixed["ats"] > 85 and fixed["technical"] < 50:
        fixed["technical"] += 10  # slight correction

    return fixed


# 🔹 Handle missing or invalid answers
def safe_value(val, default=0):
    if val is None or val == "":
        return default
    return val


# 🔹 Conversation stabilization
def stabilize_response(answer):

    if not answer or answer.strip() == "":
        return "No response provided"

    if len(answer.split()) < 2:
        return "Insufficient response"

    return answer.strip()


# 🔹 API Output Stabilizer
def stabilize_output(result):

    result["candidate"] = result.get("candidate", "Unknown")
    result["role"] = result.get("role", "Unknown")

    result["hiring_fit_percentage"] = normalize_score(
        result.get("hiring_fit_percentage", 0)
    )

    if "decision" not in result:
        result["decision"] = "Consider"

    return result


# 🔹 Edge Case Validator
def validate_edge_cases(result):

    issues = []

    if result["hiring_fit_percentage"] == 0:
        issues.append("Zero score detected")

    if result["decision"] == "Selected" and result["hiring_fit_percentage"] < 70:
        issues.append("Incorrect selection logic")

    if result["decision"] == "Rejected" and result["hiring_fit_percentage"] > 75:
        issues.append("Incorrect rejection logic")

    return issues


# 🔹 Main Stabilization Pipeline
def correct_decision(hiring_fit):

    if hiring_fit >= 80:
        return "Selected"
    elif hiring_fit >= 65:
        return "Consider"
    return "Rejected"


def stabilize_system(candidate_data):

    scores = candidate_data["scores"]

    # Step 1: Fix score inconsistencies
    fixed_scores = fix_inconsistent_scores(scores)
    candidate_data["scores"] = fixed_scores

    # Step 2: Normalize output
    candidate_data = stabilize_output(candidate_data)

    # 🔥 Step 3: AUTO-CORRECT DECISION (VERY IMPORTANT)
    correct = correct_decision(candidate_data["hiring_fit_percentage"])

    if candidate_data["decision"] != correct:
        candidate_data["decision"] = correct

    # Step 4: Validate after fixing
    issues = validate_edge_cases(candidate_data)

    return {
        "stabilized_data": candidate_data,
        "issues": issues
    }