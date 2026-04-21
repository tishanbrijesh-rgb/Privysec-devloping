from flask import Flask, render_template, request, session, redirect
from scanner import run_nmap
from parser import parse_nmap
from discovery import discover_hosts
from fingerprint import classify_device
from scorecard import calculate_score
from vuln import detect_vulns
from network import detect_network_type

import json
from datetime import datetime

app = Flask(__name__)
app.secret_key = "privysec"


# ---------------- AUTH ----------------
def auth():
    return "user" in session


@app.route("/login", methods=["GET","POST"])
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


# ---------------- HISTORY ----------------
def save_history(scan_data, risk, score):
    entry = {
        "ip": scan_data.get("ip"),
        "time": datetime.now().strftime("%H:%M:%S"),
        "risk": risk,
        "score": score
    }

    try:
        with open("history.json", "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append(entry)

    with open("history.json", "w") as f:
        json.dump(data[-10:], f)


def load_history():
    try:
        with open("history.json", "r") as f:
            return json.load(f)
    except:
        return []


# ---------------- SCAN ----------------
@app.route("/scan", methods=['POST'])
def scan():

    target = request.form.get("target")
    if not target:
        return "Invalid target"

    mode = request.form.get("mode", "quick")

    raw_output = run_nmap(target, mode)
    if not raw_output:
        return "Scan failed"

    scan_data = parse_nmap(raw_output)

    # 🧠 Fingerprint
    dtype, confidence, reasons = classify_device(scan_data)
    scan_data["type"] = dtype.lower()

    # 🔐 Score
    score, risk, issues, fixes = calculate_score(scan_data)

    # ☠️ Vulns
    vulns = detect_vulns(scan_data)

    # 🌐 Network
    network_type = detect_network_type(scan_data)

    # 📊 Summary
    summary = {
        "open_ports": len(scan_data.get("ports", [])),
        "critical": sum(1 for i in issues if "telnet" in i.lower() or "ftp" in i.lower()),
        "risk": risk,
        "score": score
    }

    # 🎯 Attack Surface
    attack_surface = {
        "total_ports": len(scan_data.get("ports", [])),
        "high": sum(1 for p in scan_data["ports"] if p in ["23/tcp","445/tcp","3389/tcp"]),
        "medium": sum(1 for p in scan_data["ports"] if p in ["21/tcp","80/tcp"]),
        "low": sum(1 for p in scan_data["ports"] if p in ["443/tcp"])
    }

    # ⚠ Unknown Device Alert
    unknown_alert = (dtype == "Unknown Device")

    # 🕘 History
    save_history(scan_data, risk, score)
    history = load_history()

    # FIX zip issue
    paired_ports = list(zip(scan_data["ports"], scan_data["services"]))

    return render_template(
        "dashboard.html",
        data=scan_data,
        device={
            "type": dtype,
            "confidence": confidence,
            "reasons": reasons
        },
        score=score,
        risk=risk,
        issues=issues,
        fixes=fixes,
        vulns=vulns,
        network_type=network_type,
        summary=summary,
        attack_surface=attack_surface,
        unknown_alert=unknown_alert,
        history=history,
        paired_ports=paired_ports
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
