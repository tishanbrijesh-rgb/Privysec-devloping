def calculate_score(device):

    ports = set(device.get("ports", []))
    device_type = device.get("type", "").lower()

    score = 100
    issues = []
    fixes = []

    if "21/tcp" in ports:
        score -= 10
        issues.append("FTP exposed")
        fixes.append("Use SFTP")

    if "23/tcp" in ports:
        score -= 25
        issues.append("Telnet insecure")
        fixes.append("Use SSH")

    if "53/tcp" in ports:
        if "gateway" in device_type:
            score -= 5
        else:
            score -= 15
            issues.append("Unexpected DNS service")
            fixes.append("Disable DNS")

    if not ports:
        score += 5

    score = max(0, min(100, score))

    if score >= 80:
        risk = "LOW"
    elif score >= 50:
        risk = "MEDIUM"
    else:
        risk = "HIGH"

    return score, risk, issues, fixes
