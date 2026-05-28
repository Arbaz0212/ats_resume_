import json
import re

def extract_keywords(text, skill_db_path="models/skill_db.json"):
    with open(skill_db_path, "r") as f:
        skills = json.load(f)

    found = []
    for category in skills.values():
        for skill in category:
            if re.search(rf"\b{re.escape(skill.lower())}\b", text):
                found.append(skill)

    return list(set(found))
