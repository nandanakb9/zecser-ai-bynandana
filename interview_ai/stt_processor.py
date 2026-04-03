import re

FILLER_WORDS = [
    "um", "umm", "uh", "uhh",
    "like", "you know", "okay",
    "hmm", "ah", "er"
]

def remove_fillers(text):
    for word in FILLER_WORDS:
        text = re.sub(rf"\b{word}\b", "", text, flags=re.IGNORECASE)
    return text


def normalize_case(text):
    return text.lower().strip()


def fix_spacing(text):
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def clean_transcript(text):
    text = remove_fillers(text)
    text = normalize_case(text)
    text = fix_spacing(text)
    return text

def handle_partial(text):
    if len(text.split()) < 2:
        return "partial_answer"
    return text


def detect_silence(text):
    if text.strip() == "":
        return "silence_detected"
    return text

def speech_to_text(audio_input):
    # mock STT (future: Whisper / Google STT)
    return audio_input