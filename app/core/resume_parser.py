import re


# ============================================================
# EXPERIENCE SCORE
# ============================================================

def extract_experience_score(resume_text: str) -> float:
    """
    Estimate experience quality score
    """

    experience_keywords = [
        "intern",
        "experience",
        "worked",
        "developer",
        "engineer",
        "analyst",
        "project",
        "freelance"
    ]

    score = 0

    text = resume_text.lower()

    for keyword in experience_keywords:
        if keyword in text:
            score += 12

    return min(score, 100)


# ============================================================
# PROJECT SCORE
# ============================================================

def extract_project_score(resume_text: str) -> float:
    """
    Estimate project quality score
    """

    project_keywords = [
        "ai",
        "machine learning",
        "llm",
        "rag",
        "nlp",
        "api",
        "automation",
        "dashboard",
        "analytics",
        "assistant"
    ]

    score = 0

    text = resume_text.lower()

    for keyword in project_keywords:
        if keyword in text:
            score += 10

    return min(score, 100)


# ============================================================
# EDUCATION SCORE
# ============================================================

def extract_education_score(resume_text: str) -> float:
    """
    Estimate education quality score
    """

    education_keywords = [
        "bachelor",
        "b.tech",
        "engineering",
        "computer science",
        "electronics",
        "cgpa",
        "university"
    ]

    score = 40

    text = resume_text.lower()

    for keyword in education_keywords:
        if keyword in text:
            score += 8

    return min(score, 100)