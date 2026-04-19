def classify_device(device):
    ports = set(device["ports"])
    vendor = device["vendor"].lower()

    score = {"Router": 0, "Computer": 0, "Mobile": 0}
    reasons = []

    if device["ip"].endswith(".1") and "53/tcp" in ports:
        return "Mobile Hotspot / Gateway", ["Gateway IP + DNS"], 85

    if len(ports) >= 2:
        score["Computer"] += 2

    if any(p in ports for p in ["21/tcp", "22/tcp", "3389/tcp"]):
        score["Computer"] += 2
        reasons.append("Common computer services")

    if "intel" in vendor:
        score["Computer"] += 2

    if not ports and device["mac"] == "Unknown":
        return "Mobile / Restricted Device", ["NAT + no ports"], 90

    best = max(score, key=score.get)
    confidence = min(90, score[best] * 20)

    return best, reasons, confidence
