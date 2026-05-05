# Day 52 – Final Recommendation AI

def normalize(value):
    if value is None:
        return 0
    return max(0, min(value, 100))


def calculate_confidence(hiring_fit, risk_score):
    """
    Higher risk reduces confidence
    """
    confidence = hiring_fit - (risk_score * 0.3)
    return round(max(min(confidence, 100), 0), 2)


def detect_risk(behavior_score=100, integrity_risk=0):
    """
    Combine behavioral + integrity signals
    """
    risk = 0

    # Low behavior score → risk
    if behavior_score < 60:
        risk += 30
    elif behavior_score < 75:
        risk += 15

    # Integrity risk (from Day 49)
    risk += integrity_risk

    return min(risk, 100)


def make_decision(hiring_fit, risk_score):

    if risk_score > 70:
        return "Rejected"

    if hiring_fit >= 80 and risk_score < 30:
        return "Selected"

    if hiring_fit >= 65:
        return "Hold / Review"

    return "Rejected"


def explain_decision(hiring_fit, risk_score, confidence):
    return {
        "hiring_fit": hiring_fit,
        "risk_score": risk_score,
        "confidence_score": confidence,
        "logic": "Decision based on hiring fit + risk analysis"
    }


def build_final_decision(candidate_name, role, scores, behavior_score=100, integrity_risk=0):

    hiring_fit = normalize(scores.get("hiring_fit_percentage"))

    # Step 1: risk calculation
    risk_score = detect_risk(behavior_score, integrity_risk)

    # Step 2: confidence
    confidence = calculate_confidence(hiring_fit, risk_score)

    # Step 3: final decision
    decision = make_decision(hiring_fit, risk_score)

    # Step 4: explainability
    explanation = explain_decision(hiring_fit, risk_score, confidence)

    return {
        "candidate": candidate_name,
        "role": role,
        "final_decision": decision,
        "hiring_fit_percentage": hiring_fit,
        "confidence_score": confidence,
        "risk_score": risk_score,
        "explanation": explanation
    }