# fingerprint.py

from collections import defaultdict


def classify_device(device):

    ports = set(device.get("ports", []))
    services = device.get("services", [])
    vendor = (device.get("vendor") or "").lower()
    os = (device.get("os") or "").lower()
    ip = device.get("ip", "")

    score = defaultdict(int)
    reasons = []

    # =========================
    # 🌐 GATEWAY DETECTION
    # =========================
    if "53/tcp" in ports:
        score["gateway"] += 40
        reasons.append("DNS service detected")

    if ip.endswith(".1"):
        score["gateway"] += 30
        reasons.append("Gateway IP pattern (.1)")

    if len(ports) >= 3:
        score["gateway"] += 10

    # =========================
    # 📡 IoT DEVICE DETECTION
    # =========================
    if "554/tcp" in ports and "80/tcp" in ports:
        score["iot"] += 60
        reasons.append("Camera pattern (RTSP + HTTP)")

    if "9100/tcp" in ports:
        score["iot"] += 50
        reasons.append("Printer port detected")

    if "8008/tcp" in ports or "8009/tcp" in ports:
        score["iot"] += 50
        reasons.append("Smart TV / Chromecast ports")

    if "23/tcp" in ports:
        score["iot"] += 25
        reasons.append("Telnet → common in IoT")

    if "8080/tcp" in ports and "554/tcp" in ports:
        score["iot"] += 40
        reasons.append("Camera alt pattern (RTSP + HTTP-alt)")

    # =========================
    # 💻 COMPUTER DETECTION
    # =========================
    if "3389/tcp" in ports:
        score["computer"] += 50
        reasons.append("RDP service → Windows system")

    if "22/tcp" in ports and "linux" in os:
        score["computer"] += 40
        reasons.append("SSH + Linux OS")

    if "445/tcp" in ports:
        score["computer"] += 40
        reasons.append("SMB → Windows system")

    if any("apache" in s or "nginx" in s for s in services):
        score["computer"] += 20
        reasons.append("Web server detected")

    # =========================
    # 📱 MOBILE DEVICE DETECTION
    # =========================
    if not ports:
        score["mobile"] += 60
        reasons.append("No open ports (NAT/mobile)")

    if "apple" in vendor or "samsung" in vendor:
        score["mobile"] += 30
        reasons.append(f"Mobile vendor ({vendor})")

    if "android" in os:
        score["mobile"] += 40
        reasons.append("Android OS detected")

    # =========================
    # 🧠 UNKNOWN DEVICE DETECTION
    # =========================
    if not ports and vendor == "unknown":
        score["unknown"] += 50
        reasons.append("No identifiable fingerprint")

    # =========================
    # 🎯 FINAL DECISION
    # =========================
    if not score:
        device_type = "unknown"
        confidence = 0
    else:
        device_type = max(score, key=score.get)
        confidence = min(100, score[device_type])

    labels = {
        "gateway": "Gateway / Router",
        "mobile": "Mobile Device",
        "computer": "Computer",
        "iot": "Smart IoT Device",
        "unknown": "Unknown Device"
    }

    return labels[device_type], confidence, reasons
