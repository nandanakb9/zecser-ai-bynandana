# HR Interview AI – API Specification

## 1. ATS Scoring API
POST /api/ats-score

Input:
{
  "resume": "text",
  "job_description": "text"
}

Output:
{
  "ats_score": 82
}

---

## 2. Eligibility API
POST /api/eligibility

Input:
{
  "candidate": "name",
  "ats_score": 78
}

Output:
{
  "decision": "Eligible"
}

---

## 3. HR Scoring API
POST /api/hr-score

Input:
{
  "answers": ["text"]
}

Output:
{
  "hr_score": 85
}

---

## 4. Unified Score API
POST /api/unified-score

Input:
{
  "ats": 80,
  "screening": 75,
  "hr": 85
}

Output:
{
  "hiring_fit": 82.3
}

---

## 5. Ethics Check API
POST /api/ethics-check

Output:
{
  "status": "compliant"
}