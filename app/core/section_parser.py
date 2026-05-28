import json
import re
from pathlib import Path
from typing import List, Dict, Set


# ============================================================
# PATH RESOLUTION
# ============================================================

BASE_DIR = Path(__file__).resolve().parents[2]
SKILL_DB_PATH = BASE_DIR / "models" / "skill_db.json"

with open(SKILL_DB_PATH, "r", encoding="utf-8") as f:
    RAW_SKILL_DB = json.load(f)


# ============================================================
# BUILD SKILL WHITELIST
# ============================================================

def _flatten_skill_db(skill_db: Dict[str, List[str]]) -> Set[str]:
    skills = set()
    for values in skill_db.values():
        for skill in values:
            skill = skill.strip().lower()
            if 1 <= len(skill.split()) <= 3:
                skills.add(skill)
    return skills


VALID_SKILLS = _flatten_skill_db(RAW_SKILL_DB)


# ============================================================
# NORMALIZATION
# ============================================================

def _normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9+#.\s]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


# ============================================================
# EXTRACT SKILLS FROM TEXT
# ============================================================

def extract_skills(text: str) -> Set[str]:
    text = _normalize(text)
    found = set()

    for skill in VALID_SKILLS:
        if re.search(rf"\b{re.escape(skill)}\b", text):
            found.add(skill)

    return found


# ============================================================
# COMPARE SKILLS (THIS IS THE REAL FIX)
# ============================================================

def compare_skills(
    resume_text: str,
    role_required_skills: List[str]
) -> Dict[str, List[str]]:

    resume_skills = extract_skills(resume_text)

    # normalize role skills ONLY from role_skills.json
    required_skills = {
        skill.lower().strip()
        for skill in role_required_skills
        if skill.lower().strip() in VALID_SKILLS
    }

    matched = sorted(resume_skills & required_skills)
    missing = sorted(required_skills - resume_skills)

    return {
        "matched_skills": matched,
        "missing_skills": missing,
        "total_required": len(required_skills),
        "matched_count": len(matched)
    }
