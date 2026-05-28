import json

with open("models/role_skills.json") as f:
    ROLE_PROFILES = json.load(f)

def get_role_profile(role):
    role_key = role.lower().replace(" ", "_")
    if role_key not in ROLE_PROFILES:
        raise ValueError("Unsupported role")
    return ROLE_PROFILES[role_key]
