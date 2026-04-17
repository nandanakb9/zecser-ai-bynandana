# Day 48 – Behavioral AI Research & Design

BEHAVIOR_SIGNALS = [
    "eye_movement",
    "head_movement",
    "facial_engagement",
    "attention_pattern"
]


MEASURABLE_INDICATORS = {
    "focus_level": 0,
    "distraction_frequency": 0,
    "nervous_gestures": 0
}


SIGNAL_TO_SCORE = {
    "eye_movement": {
        "stable": 90,
        "moderate": 70,
        "frequent": 40
    },
    "head_movement": {
        "steady": 85,
        "normal": 70,
        "restless": 45
    },
    "facial_engagement": {
        "active": 90,
        "neutral": 65,
        "low": 35
    },
    "attention_pattern": {
        "focused": 95,
        "partial": 60,
        "distracted": 30
    }
}


def calculate_focus(signals):

    focus = (
        SIGNAL_TO_SCORE["eye_movement"][signals["eye_movement"]] +
        SIGNAL_TO_SCORE["facial_engagement"][signals["facial_engagement"]] +
        SIGNAL_TO_SCORE["attention_pattern"][signals["attention_pattern"]]
    ) / 3

    return round(focus, 2)


def calculate_distraction(signals):

    distraction = 100 - SIGNAL_TO_SCORE["attention_pattern"][signals["attention_pattern"]]
    return round(distraction, 2)


def calculate_nervousness(signals):

    nervous = 100 - SIGNAL_TO_SCORE["head_movement"][signals["head_movement"]]
    return round(nervous, 2)


def behavioral_score(signals):

    focus = calculate_focus(signals)
    distraction = calculate_distraction(signals)
    nervous = calculate_nervousness(signals)

    overall = (focus * 0.5) + ((100 - distraction) * 0.3) + ((100 - nervous) * 0.2)

    return {
        "focus_level": focus,
        "distraction_frequency": distraction,
        "nervous_gestures": nervous,
        "behavioral_score": round(overall, 2)
    }


def behavioral_analysis_report(candidate, signals):

    score = behavioral_score(signals)

    return {
        "candidate": candidate,
        "signals": signals,
        "analysis": score,
        "verdict": "Attentive" if score["behavioral_score"] > 70 else "Needs Monitoring"
    }