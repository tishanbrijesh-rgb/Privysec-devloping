import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "mistral"


def generate(prompt):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            }
        )

        if response.status_code == 200:
            return response.json().get("response", "").strip()

        print("❌ Ollama error:", response.text)
        return None

    except Exception as e:
        print("❌ Connection error:", e)
        return None


# 🔍 AI SUMMARY
def ask_ai_device_summary(device_type, ports, vulns):
    prompt = f"""
You are a cybersecurity expert.

Device Type: {device_type}
Open Ports: {ports}
Vulnerabilities: {vulns}

Give a short 1-2 line security insight.
"""

    result = generate(prompt)
    return result if result else "⚠️ Local AI unavailable."


# 🛠️ AI FIXES
def ask_ai_issues_fixes(scan_data, vulns):
    prompt = f"""
You are a penetration tester.

Device: {scan_data.get("type")}
Open Ports: {scan_data.get("ports")}
Vulnerabilities: {vulns}

Return STRICT format:

Issues:
- (clear issue)

Fixes:
- (exact actionable fix)
"""

    result = generate(prompt)

    if not result:
        return [], []

    issues = []
    fixes = []

    section = None
    for line in result.split("\n"):
        line = line.strip()

        if "Issues" in line:
            section = "issues"
        elif "Fixes" in line:
            section = "fixes"
        elif line.startswith("-"):
            if section == "issues":
                issues.append(line[1:].strip())
            elif section == "fixes":
                fixes.append(line[1:].strip())

    return issues, fixes


# ⚡ NEW — AI EXPLOITABILITY
def ask_ai_exploitability(scan_data, vulns):
    prompt = f"""
You are a cybersecurity expert.

Analyze exploitability.

Device: {scan_data.get("type")}
Ports: {scan_data.get("ports")}
Services: {scan_data.get("services")}
Vulnerabilities: {vulns}

Return STRICT format:

LEVEL: HIGH/MEDIUM/LOW
REASONS:
- reason 1
- reason 2
"""

    result = generate(prompt)

    if not result:
        return "UNKNOWN", ["AI unavailable"]

    level = "UNKNOWN"
    reasons = []

    for line in result.split("\n"):
        line = line.strip()

        if "LEVEL:" in line:
            level = line.split(":")[1].strip()
        elif line.startswith("-"):
            reasons.append(line[1:].strip())

    return level, reasons
