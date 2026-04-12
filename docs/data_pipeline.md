# AI Data Pipeline

Step 1: Candidate uploads resume
↓
Step 2: Resume stored in data/resumes
↓
Step 3: Resume parsed
↓
Step 4: Cleaned resume stored in data/processed_resumes
↓
Step 5: Employer uploads job description
↓
Step 6: JD stored in data/job_descriptions
↓
Step 7: JD parsed to structured format
↓
Step 8: Parsed JD stored in data/processed_jd
↓
Step 9: ATS engine compares resume and JD
↓
Step 10: Score generated
↓
Step 11: Score stored in data/ats_scores
↓
Step 12: Screening decision generated
↓
Step 13: Screening report stored
↓
Step 14: Candidate moves to interview stage
↓
Step 15: Interview results stored
↓
Step 16: Hiring decision made
Resume Upload → Resume Parser → Cleaned Resume
                                       ↓
Job Description Upload → JD Parser → Structured JD
                                       ↓
                     ATS Matching Engine
                               ↓
                         Score Generation
                               ↓
                      Screening Decision
                               ↓
                         Interview Stage
                               ↓
                         Hiring Decision