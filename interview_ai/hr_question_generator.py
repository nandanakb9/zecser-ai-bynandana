def get_hr_questions(role_type="fresher", domain="non_technical"):

    fresher_questions = [
        "Tell me about yourself",
        "Why did you choose this career?",
        "What are your strengths?",
        "What are your weaknesses?",
        "Where do you see yourself in 5 years?"
    ]

    experienced_questions = [
        "Tell me about your career journey",
        "Describe your leadership experience",
        "What challenges have you handled?",
        "Why are you switching jobs?",
        "What are your career goals?"
    ]

    technical_addon = [
        "How do you handle technical deadlines?",
        "Explain a challenging project"
    ]

    non_technical_addon = [
        "How do you handle clients?",
        "Describe your communication style"
    ]

    if role_type == "experienced":
        base = experienced_questions
    else:
        base = fresher_questions

    if domain == "technical":
        base += technical_addon
    else:
        base += non_technical_addon

    return base