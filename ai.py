import requests


def ask_ai(port, service):
    prompt = f"""
You are a cybersecurity expert.

Port: {port}
Service: {service}

Give SHORT and CLEAN output.

Rules:
- No markdown (no ** or *)
- Max 1 line per field
- Keep it simple and realistic
- Do NOT mention exploits, CVEs, or RCE

FORMAT EXACTLY:

Service: <short description>\n

Possible Risks: <general security risks only (no deep technical claims)>\n

Severity: <LOW/MEDIUM/HIGH>\n

Recommendation: <short>
"""

    try:
        res = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )

        text = res.json().get("response", "").strip()

        return clean_parse(text)

    except:
        return fallback()


# 🔧 Clean + parse output
def clean_parse(text):
    data = {
        "service": "Unknown",
        "risks": "Unknown",
        "severity": "LOW",
        "fix": "Restrict access"
    }

    for line in text.split("\n"):
        line = line.replace("*", "").strip()  # 🔥 remove markdown

        if ":" not in line:
            continue

        key, value = line.split(":", 1)
        key = key.lower().strip()
        value = value.strip()

        if "service" in key:
            data["service"] = value[:80]

        elif "risk" in key:
            data["risks"] = value[:80]

        elif "severity" in key:
            data["severity"] = value.upper()

        elif "recommend" in key:
            data["fix"] = value[:100]

    return data


def fallback():
    return {
        "service": "Unknown service",
        "risks": "Possible misconfiguration",
        "severity": "LOW",
        "fix": "Restrict access if unnecessary"
    }
