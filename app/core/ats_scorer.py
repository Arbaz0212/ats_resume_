from app.core.section_parser import compare_skills
from app.core.section_parser import (
    compare_skills,
    extract_skills
)
from app.core.similarity import calculate_similarity
from app.core.resume_parser import (
    extract_experience_score,
    extract_project_score,
    extract_education_score
)
from pathlib import Path
import json


# ============================================================
# LOAD ROLE SKILLS (ONCE)
# ============================================================

BASE_DIR = Path(__file__).resolve().parents[2]
ROLE_SKILLS_PATH = BASE_DIR / "models" / "role_skills.json"

with open(ROLE_SKILLS_PATH, "r", encoding="utf-8") as f:
    ROLE_SKILLS = json.load(f)


# ============================================================
# SKILL SCORE (REAL ATS LOGIC)
# ============================================================

def calculate_skill_score(matched: int, total: int) -> float:
    if total == 0:
        return 0.0
    return round((matched / total) * 100, 2)


# ============================================================
# FINAL ATS SCORER
# ============================================================

def calculate_final_ats_score(
    resume_text: str,
    job_description_text: str,
    job_role: str
) -> dict:
    """
    Central ATS scoring brain (industry-correct)
    """

    # ==============================
    # SKILLS (ROLE DRIVEN — FIXED)
    # ==============================

    role_key = job_role.lower().strip()

    # ============================================================
    # DYNAMIC ROLE HANDLING
    # ============================================================

    if role_key in ROLE_SKILLS:

        required_skills = ROLE_SKILLS[role_key]

    else:

        # Fallback → extract skills from JD dynamically
        required_skills = extract_skills(job_description_text)

    # ============================================================
    # SKILL COMPARISON
    # ============================================================

    skill_data = compare_skills(
        resume_text=resume_text,
        role_required_skills=required_skills
    )

    skills_score = calculate_skill_score(
        matched=skill_data["matched_count"],
        total=skill_data["total_required"]
    )

    # ==============================
    # OTHER SECTIONS (JD DRIVEN)
    # ==============================

    similarity_score = calculate_similarity(
        resume_text,
        job_description_text
    )

    experience_score = extract_experience_score(resume_text)
    project_score = extract_project_score(resume_text)
    education_score = extract_education_score(resume_text)

    # ==============================
    # FINAL WEIGHTED ATS SCORE
    # ==============================

    final_score = round(
        (skills_score * 0.35) +
        (similarity_score * 0.25) +
        (experience_score * 0.20) +
        (project_score * 0.10) +
        (education_score * 0.10),
        2
    )

    return {
        "final_score": final_score,
        "matched_skills": skill_data["matched_skills"],
        "missing_skills": skill_data["missing_skills"],
        "section_scores": {
            "skills": skills_score,
            "similarity": similarity_score,
            "experience": experience_score,
            "projects": project_score,
            "education": education_score
        }
    }

