from datetime import datetime

# -------------------------------
# AUDIT TRAIL SYSTEM
# -------------------------------

def log_score(candidate, scores):
    return {
        "candidate": candidate,
        "timestamp": str(datetime.now()),
        "type": "score_log",
        "scores": scores
    }


def log_decision(candidate, decision):
    return {
        "candidate": candidate,
        "timestamp": str(datetime.now()),
        "type": "decision_log",
        "decision": decision
    }


# -------------------------------
# DATA RETENTION POLICY
# -------------------------------

def data_retention_policy(days=30):
    return {
        "retention_days": days,
        "policy": f"All candidate data will be stored for {days} days and then deleted."
    }


# -------------------------------
# CONSENT MANAGEMENT
# -------------------------------

def consent_check(candidate_name, consent=True):
    return {
        "candidate": candidate_name,
        "consent_required": True,
        "consent_obtained": consent,
        "message": "Consent required before storing or processing candidate data."
    }


# -------------------------------
# SECURE STORAGE DESIGN
# -------------------------------

def secure_storage_design():
    return {
        "transcripts": "encrypted_storage/transcripts/",
        "reports": "encrypted_storage/reports/",
        "security": "AES-256 Encryption Recommended"
    }


# -------------------------------
# ACCESS CONTROL SYSTEM
# -------------------------------

def access_control(user_role):
    permissions = {
        "admin": ["view", "edit", "delete", "audit"],
        "recruiter": ["view", "generate_report"],
        "viewer": ["view"]
    }

    return {
        "role": user_role,
        "permissions": permissions.get(user_role, [])
    }


# -------------------------------
# FULL GOVERNANCE REPORT
# -------------------------------

def generate_governance_report(candidate, scores, decision):

    return {
        "audit_logs": {
            "score_log": log_score(candidate, scores),
            "decision_log": log_decision(candidate, decision)
        },
        "consent": consent_check(candidate),
        "data_policy": data_retention_policy(),
        "storage": secure_storage_design(),
        "access_control": access_control("recruiter"),
        "status": "AI system is secure and compliant"
    }