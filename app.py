from flask import Flask, render_template, request
from scanner import run_nmap
from parser import parse_nmap
from discovery import discover_hosts
from fingerprint import classify_device
from scorecard import calculate_score

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/discover')
def discover():
    hosts = discover_hosts()
    return render_template("devices.html", hosts=hosts)

@app.route('/scan', methods=['POST'])
def scan():

    target = request.form.get("target")
    mode = request.form.get("mode")

    raw_output = run_nmap(target, mode)
    scan_data = parse_nmap(raw_output)

    dtype, confidence, reasons = classify_device(scan_data)

    # attach type for scorecard
    scan_data["type"] = dtype.lower()

    score, risk, issues, fixes = calculate_score(scan_data)

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
        fixes=fixes
    )

if __name__ == "__main__":
    app.run(debug=True)
