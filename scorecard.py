from port_db import PORT_DB

HIGH_RISK = ["23/tcp", "445/tcp", "3389/tcp"]
MEDIUM_RISK = ["21/tcp", "80/tcp"]
LOW_RISK = ["443/tcp"]

def calculate_score(device):

    ports = set(device.get("ports", []))
    device_type = device.get("type", "").lower()

    score = 100
    issues = []
    fixes = []

    for p in ports:

        if p in PORT_DB:
            data = PORT_DB[p]

            issues.append(data["issue"])
            fixes.append(data["fix"])

            if p in HIGH_RISK:
                score -= 25
            elif p in MEDIUM_RISK:
                score -= 15
            elif p in LOW_RISK:
                score -= 5
            else:
                score -= 10

        else:
            issues.append(f"Unknown service on {p}")
            fixes.append(f"Restrict port {p}")
            score -= 5

    if device_type == "gateway" and "53/tcp" in ports:
        score += 5

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
