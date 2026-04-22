from flask import Flask, render_template, request, session, redirect
from scanner import run_nmap
from parser import parse_nmap
from discovery import discover_hosts
from fingerprint import classify_device
from scorecard import calculate_score
from vuln import detect_vulns
from network import detect_network_type
from ai import ask_ai_device_summary, ask_ai_issues_fixes, ask_ai_exploitability
from port_db import PORT_DB

import json
from datetime import datetime

app = Flask(__name__)
app.secret_key = "privysec"


def auth():
    return "user" in session


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["username"] == "admin" and request.form["password"] == "admin":
            session["user"] = True
            return redirect("/")
    return render_template("login.html")


@app.route("/")
def home():
    if not auth():
        return redirect("/login")
    return render_template("index.html")


@app.route("/discover")
def discover():
    hosts = discover_hosts()
    return render_template("devices.html", hosts=hosts)


# ---------------- SCAN ----------------
@app.route("/scan", methods=["POST"])
def scan():

    target = request.form.get("target")
    if not target:
        return "Invalid target"

    mode = request.form.get("mode", "quick")

    raw_output = run_nmap(target, mode)
    if not raw_output:
        return "Scan failed"

    scan_data = parse_nmap(raw_output)

    dtype, confidence, reasons = classify_device(scan_data)
    scan_data["type"] = dtype.lower()

    vulns = detect_vulns(scan_data)

    # 🔥 AI EXPLOITABILITY
    try:
        exploit_level, exploit_reasons = ask_ai_exploitability(scan_data, vulns)
    except:
        exploit_level, exploit_reasons = "UNKNOWN", ["AI unavailable"]

    score, risk, issues, fixes = calculate_score(scan_data)

    try:
        ai_issues, ai_fixes = ask_ai_issues_fixes(scan_data, vulns)
        if ai_issues:
            issues = ai_issues
        if ai_fixes:
            fixes = ai_fixes
    except:
        pass

    network_type = detect_network_type(scan_data)

    try:
        ai_summary = ask_ai_device_summary(dtype, scan_data.get("ports"), vulns)
    except:
        ai_summary = "AI insight unavailable."

    # ================= FIXED ATTACK SURFACE =================
    attack_surface = {"total_ports": 0, "high": 0, "medium": 0, "low": 0}

    for p in scan_data.get("ports", []):
        attack_surface["total_ports"] += 1

        if p in PORT_DB:
            risk_level = PORT_DB[p]["risk"]

            if risk_level == "HIGH":
                attack_surface["high"] += 1
            elif risk_level == "MEDIUM":
                attack_surface["medium"] += 1
            else:
                attack_surface["low"] += 1
        else:
            attack_surface["low"] += 1

    # ✅ NORMALIZED PERCENTAGES (MAIN FIX)
    total = attack_surface["total_ports"] or 1

    attack_surface["high_pct"] = (attack_surface["high"] / total) * 100
    attack_surface["medium_pct"] = (attack_surface["medium"] / total) * 100
    attack_surface["low_pct"] = (attack_surface["low"] / total) * 100

    # ✅ OVERALL LEVEL (IMPORTANT)
    if attack_surface["high"] > 0:
        attack_surface["level"] = "HIGH"
    elif attack_surface["medium"] > 0:
        attack_surface["level"] = "MEDIUM"
    else:
        attack_surface["level"] = "LOW"
    # ======================================================

    danger_reason = None

    if score < 50:
        danger_reason = "High risk due to multiple vulnerabilities"
    elif attack_surface["high"] > 0:
        danger_reason = "Critical services exposed"
    elif "23/tcp" in scan_data.get("ports", []):
        danger_reason = "Telnet detected (insecure protocol)"
    elif "445/tcp" in scan_data.get("ports", []):
        danger_reason = "SMB exposed (exploit risk)"

    is_dangerous = danger_reason is not None
    unknown_alert = (dtype == "Unknown Device")

    paired_ports = list(zip(scan_data["ports"], scan_data["services"]))

    return render_template(
        "dashboard.html",
        data=scan_data,
        device={"type": dtype, "confidence": confidence, "reasons": reasons},
        score=score,
        risk=risk,
        issues=issues,
        fixes=fixes,
        vulns=vulns,
        network_type=network_type,
        attack_surface=attack_surface,
        unknown_alert=unknown_alert,
        paired_ports=paired_ports,
        ai_summary=ai_summary,
        is_dangerous=is_dangerous,
        danger_reason=danger_reason,
        exploit_level=exploit_level,
        exploit_reasons=exploit_reasons
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
