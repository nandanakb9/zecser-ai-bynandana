# Day 49 – Malpractice & Integrity Detection Design

MALPRACTICE_SIGNALS = [
    "tab_switching",
    "screen_focus_loss",
    "external_voice",
    "looking_away"
]


THRESHOLDS = {
    "tab_switching": 3,
    "screen_focus_loss": 2,
    "external_voice": 1,
    "looking_away": 4
}


RISK_WEIGHTS = {
    "tab_switching": 0.25,
    "screen_focus_loss": 0.25,
    "external_voice": 0.30,
    "looking_away": 0.20
}


def detect_flags(signals):

    flags = {}

    for key, value in signals.items():
        threshold = THRESHOLDS.get(key, 0)
        flags[key] = value >= threshold

    return flags


def calculate_risk(signals):

    risk_score = 0

    for key, value in signals.items():
        threshold = THRESHOLDS.get(key, 1)
        weight = RISK_WEIGHTS.get(key, 0)

        normalized = min(value / threshold, 1)
        risk_score += normalized * weight * 100

    return round(risk_score, 2)


def risk_level(score):

    if score > 75:
        return "High Risk"
    elif score > 40:
        return "Medium Risk"
    else:
        return "Low Risk"


def integrity_report(candidate, signals):

    flags = detect_flags(signals)
    score = calculate_risk(signals)
    level = risk_level(score)

    return {
        "candidate": candidate,
        "signals": signals,
        "flags": flags,
        "risk_score": score,
        "risk_level": level,
        "alert": level != "Low Risk"
    }