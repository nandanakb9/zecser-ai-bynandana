# Day 43 – Ethics & Compliance Review

import datetime


CONSENT_TEMPLATE = {
    "consent_required": True,
    "consent_text": "Candidate consent required before AI interview recording and analysis.",
    "consent_obtained": False
}


FAIRNESS_RULES = {
    "ignore_fields": [
        "gender",
        "age",
        "religion",
        "marital_status",
        "nationality"
    ]
}


DATA_RETENTION_DAYS = 30


def check_consent(consent_given):
    consent = CONSENT_TEMPLATE.copy()
    consent["consent_obtained"] = consent_given
    return consent


def fairness_review(candidate_data):

    cleaned_data = candidate_data.copy()

    for field in FAIRNESS_RULES["ignore_fields"]:
        if field in cleaned_data:
            cleaned_data.pop(field)

    return cleaned_data


def explainability_notes(scores):

    notes = {
        "ats": "ATS score based on resume-job match",
        "screening": "Screening score based on HR questionnaire responses",
        "hr": "HR score based on communication and confidence",
        "final": "Final score computed using weighted average"
    }

    return {
        "scores": scores,
        "explanation": notes
    }


def compliance_data_retention(timestamp):

    created_date = datetime.datetime.strptime(timestamp, "%Y-%m-%d")
    current_date = datetime.datetime.now()

    days = (current_date - created_date).days

    if days > DATA_RETENTION_DAYS:
        return "Delete"
    else:
        return "Retain"


def ethics_report(candidate, scores, consent=True):

    consent_info = check_consent(consent)
    fairness_data = fairness_review(candidate)
    explain = explainability_notes(scores)

    return {
        "candidate": fairness_data,
        "consent": consent_info,
        "explainability": explain,
        "compliance": "Aligned with ethical AI standards"
    }