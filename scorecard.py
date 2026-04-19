def calculate_score(device):
    ports = set(device["ports"])
    services = set(device["services"])

    score = 100
    issues = []
    fixes = []

    if "23/tcp" in ports:
        score -= 30
        issues.append("Telnet exposed")
        fixes.append("Disable Telnet")

    if "21/tcp" in ports:
        score -= 20
        issues.append("FTP exposed")
        fixes.append("Use SFTP")

    if "80/tcp" in ports:
        score -= 10
        issues.append("HTTP used")
        fixes.append("Use HTTPS")

    if len(ports) > 5:
        score -= 15
        issues.append("Too many open ports")
        fixes.append("Close unused ports")

    risk = "LOW" if score >= 80 else "MEDIUM" if score >= 50 else "HIGH"

    return score, risk, issues, fixes
