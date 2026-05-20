# API Authentication & Security

SECURITY_CONFIG = {

    "authentication": "JWT Token",

    "encryption": "AES-256",

    "rate_limiting": True,

    "access_control": [
        "admin",
        "recruiter",
        "hr_manager"
    ],

    "secure_storage": True
}