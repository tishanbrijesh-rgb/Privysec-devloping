def classify_device(device):

    ports = set(device.get("ports", []))
    vendor = (device.get("vendor") or "").lower()
    ip = device.get("ip", "")

    score = {
        "gateway": 0,
        "mobile": 0,
        "computer": 0,
        "iot": 0
    }

    reasons = []

    if "53/tcp" in ports:
        score["gateway"] += 40
        reasons.append("DNS service detected")

    if ip.endswith(".1"):
        score["gateway"] += 30
        reasons.append("Gateway IP pattern (.1)")

    if len(ports) >= 3:
        score["gateway"] += 20

    if not ports:
        score["mobile"] += 60
        reasons.append("No open ports (NAT device)")

    if "intel" in vendor:
        score["computer"] += 40

    device_type = max(score, key=score.get)
    confidence = min(100, score[device_type])

    labels = {
        "gateway": "Mobile Hotspot / Gateway",
        "mobile": "Mobile / Restricted Device",
        "computer": "Computer",
        "iot": "Smart IoT Device"
    }

    return labels[device_type], confidence, reasons
