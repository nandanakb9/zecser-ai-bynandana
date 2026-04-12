# ATS Architecture

## Pipeline Architecture

1. Resume Input
2. Section Classification
3. Skill Extraction
4. Education Parsing
5. Experience Parsing
6. ATS Scoring
7. Ranking Engine
8. Shortlisting
9. API Output

## Modules

* screening_ai
* utils
* api
* tests
* docs

## Data Flow

uploads → parsed → scores → ranking → shortlist
