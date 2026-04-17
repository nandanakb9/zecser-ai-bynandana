# HR Interview AI – Developer Handbook

## Installation
pip install -r requirements.txt

## Running Tests
python tests/test_unified_scoring.py
python tests/test_hr_simulation.py
python tests/test_ethics.py

## Project Structure
interview_ai/
tests/
docs/

## Scoring Logic
Final Score =
ATS * 0.30 +
Screening * 0.30 +
HR * 0.40

## Data Format

Candidate Object:
{
 "name": "Candidate",
 "role": "fresher",
 "ats_score": 80,
 "screening_score": 75,
 "hr_score": 85
}

## Troubleshooting

Issue: ImportError
Fix: Check sys.path in test file

Issue: Score mismatch
Fix: Verify weights in unified scoring

Issue: Empty transcript
Fix: Check STT cleaning module

## Integration Steps
1. Send resume to ATS API
2. Run eligibility decision
3. Start HR screening
4. Store transcript
5. Run scoring
6. Generate final hiring score
7. Run ethics compliance check