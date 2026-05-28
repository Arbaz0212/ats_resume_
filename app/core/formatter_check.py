def check_formatting(text):
    issues = []

    if len(text) < 300:
        issues.append("Resume too short")

    if "table" in text:
        issues.append("Tables detected (ATS-unfriendly)")

    if "@" not in text:
        issues.append("Email not detected")

    return issues
