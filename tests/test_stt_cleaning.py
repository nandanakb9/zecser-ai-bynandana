import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from interview_ai.stt_processor import clean_transcript, handle_partial, detect_silence

raw_text = "Um I have uh experience in financial analysis and like excel"

cleaned = clean_transcript(raw_text)
cleaned = handle_partial(cleaned)
cleaned = detect_silence(cleaned)

print("Raw :", raw_text)
print("Cleaned :", cleaned)

print("\n--- Accent / Noise Testing ---\n")

samples = [
    "uh i am from kerala and have experience",
    "umm worked in finance",
    "",
    "yes"
]

for s in samples:
    print("Input :", s)
    print("Output :", clean_transcript(s))
    print()