def detect_poor_audio(text):

    noise_patterns = ["...", "???", "***", "mmm", "uhhh"]

    for p in noise_patterns:
        if p in text.lower():
            return True

    return False


def detect_language_mix(text):

    mix_words = ["hai", "haan", "acha", "okey", "nahi"]

    for word in mix_words:
        if word in text.lower():
            return True

    return False


def detect_missing_answer(text):

    if not text.strip():
        return True

    if text.lower() in ["skip", "no answer"]:
        return True

    return False


def detect_background_noise(text):

    noise_words = ["noise", "background", "disturbance"]

    for word in noise_words:
        if word in text.lower():
            return True

    return False

def retry_logic():

    return "I'm sorry, I couldn't clearly understand. Could you please repeat?"

def clarification_logic():

    return "Could you please clarify your answer?"

def safety_fallback():

    return "We will move to the next question for now."

def handle_edge_cases(answer):

    if detect_missing_answer(answer):
        return retry_logic()

    if detect_poor_audio(answer):
        return retry_logic()

    if detect_background_noise(answer):
        return retry_logic()

    if detect_language_mix(answer):
        return clarification_logic()

    return None