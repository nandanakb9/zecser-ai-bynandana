import re

# Role similarity mapping
ROLE_SIMILARITY = {
    "data analyst": ["data analyst", "business analyst", "data scientist"],
    "python developer": ["python developer", "software engineer", "backend developer"],
    "financial analyst": ["financial analyst", "accountant", "finance executive"]
}


def extract_experience_blocks(text):
    """
    Extract experience blocks based on year patterns
    Example: Data Analyst ABC Company 2021 - 2023
    """
    pattern = r'(.*?)(\d{4})\s*-\s*(\d{4}|present)'
    matches = re.findall(pattern, text, re.IGNORECASE)
    return matches


def parse_experience(text):
    """
    Parse experience into structured objects
    """
    matches = extract_experience_blocks(text)

    experience_list = []

    for match in matches:
        role_company = match[0].strip()
        start = match[1]
        end = match[2]

        experience_list.append({
            "role_company": role_company,
            "start_year": start,
            "end_year": end
        })

    return experience_list


def calculate_total_experience(experience_list):
    """
    Calculate total years of experience
    """
    total_years = 0

    for exp in experience_list:
        start = int(exp["start_year"])

        if exp["end_year"].lower() == "present":
            end = 2026
        else:
            end = int(exp["end_year"])

        total_years += (end - start)

    return total_years


def detect_gaps(experience_list):
    """
    Detect gaps between employment periods
    """
    years = []

    for exp in experience_list:
        years.append((int(exp["start_year"]), exp["end_year"]))

    years_sorted = sorted(years)

    gaps = []

    for i in range(len(years_sorted) - 1):

        end_year = years_sorted[i][1]

        if isinstance(end_year, str) and end_year.lower() == "present":
            continue

        gap = years_sorted[i + 1][0] - int(end_year)

        if gap > 1:
            gaps.append(gap)

    return gaps


def experience_relevance(experience_list, target_role):
    """
    Calculate relevance score for target role
    """
    score = 0

    for exp in experience_list:

        role_text = exp["role_company"].lower()

        for role, similar_roles in ROLE_SIMILARITY.items():

            if target_role == role:

                for sim in similar_roles:
                    if sim in role_text:
                        score += 1

    return score


def extract_experience_data(text, target_role):
    """
    Main experience extraction engine
    """
    experience_list = parse_experience(text)

    total_exp = calculate_total_experience(experience_list)

    gaps = detect_gaps(experience_list)

    relevance = experience_relevance(experience_list, target_role)

    return {
        "experience": experience_list,
        "total_experience": total_exp,
        "gaps": gaps,
        "relevance_score": relevance
    }