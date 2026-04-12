# Metadata Standards

## Candidate Metadata
- candidate_id
- resume_file
- parsed_resume_file
- upload_timestamp

## Job Metadata
- job_id
- job_role
- jd_file
- parsed_jd_file

## AI Model Metadata
- model_version
- training_dataset
- evaluation_score

## Processing Metadata
- processed_timestamp
- pipeline_stage
- status
# Model Versioning

Model Version Format:
v1.0 - Initial ATS scoring
v1.1 - Improved skill matching
v2.0 - AI semantic matching

Each processed record should include:
- model_version
- processing_timestamp