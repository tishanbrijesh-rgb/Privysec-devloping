from flask import Flask, render_template, request
from scanner import run_nmap
from parser import parse_nmap_output
from ai import ask_ai

app = Flask(__name__)


def fallback(port, service):
    return "Low", "Basic exposure detected", "Review configuration"


def clean_ai_output(text):
    lines = [l.strip() for l in text.split("\n") if l.strip()]

    risk = "Unknown"
    reason = "N/A"
    fix = "Review manually"

    for l in lines:
        if "Risk:" in l:
            risk = l.split("Risk:")[-1].strip()
        elif "Reason:" in l:
            reason = l.split("Reason:")[-1].strip()
        elif "Fix:" in l:
            fix = l.split("Fix:")[-1].strip()

    return risk, reason, fix


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/scan", methods=["POST"])
def scan():
    target = request.form.get("target")
    mode = request.form.get("mode")
    use_ai = request.form.get("use_ai")

    results = []
    error = None

    if not target:
        return render_template("index.html", error="Enter target")

    output = run_nmap(target, mode)

    if "Error" in output:
        return render_template("index.html", error=output)

    findings = parse_nmap_output(output)

    for item in findings:
        port = item["port"]
        service = item["service"]

        if use_ai:
            prompt = f"""
You are a cybersecurity expert.

Analyze:
Port {port} running {service}

Format:
Risk: Low/Medium/High
Reason: short explanation
Fix: short action
"""

            ai_output = ask_ai(prompt)

            if not ai_output or len(ai_output.strip()) < 10:
                risk, reason, fix = fallback(port, service)
            else:
                risk, reason, fix = clean_ai_output(ai_output)
        else:
            risk, reason, fix = fallback(port, service)

        results.append({
            "port": port,
            "service": service,
            "risk": risk,
            "reason": reason,
            "fix": fix
        })

    return render_template("index.html", results=results)


if __name__ == "__main__":
    app.run(debug=True)
