import tkinter as tk
import threading
import time

from scanner import run_nmap, run_network_scan
from parser import parse_nmap_output, parse_network_output
from ai import ask_ai


def log(message):
    output_box.insert(tk.END, message + "\n")
    output_box.see(tk.END)


def run_scan(command):
    status_label.config(text="⏳ Scanning...")
    output_box.delete("1.0", tk.END)

    start_time = time.time()
    log(f"[{time.strftime('%H:%M:%S')}] Starting scan...")

    # ================= NETWORK SCAN =================
    if command == "run nmap network":

        log("[⏳ Estimated time: ~10 sec]")
        log("-" * 50)

        try:
            log("[🔄] Scanning local network...\n")

            net_output = run_network_scan()
            devices = parse_network_output(net_output)

            if not devices:
                log("No devices found.")
            else:
                log("Devices found:\n")
                for d in devices:
                    log(f"→ {d}")

                log(f"\nTotal devices: {len(devices)}")

            end_time = time.time()
            total_time = round(end_time - start_time, 2)

            log("-" * 50)
            log(f"[⏱ Completed in {total_time} sec]")
            log("[✔] Network scan complete.")

            status_label.config(text="✅ Done")

        except Exception as e:
            log(f"Error: {e}")
            status_label.config(text="❌ Error")

        return

    # ================= NORMAL SCAN =================
    if command.startswith("run nmap"):

        parts = command.split()
        mode = "fast"
        target = "localhost"

        if "full" in parts:
            mode = "full"
        elif "aggressive" in parts:
            mode = "aggressive"

        # Estimated time
        if mode == "fast":
            est = 5
        elif mode == "full":
            est = 15
        else:
            est = 25

        log(f"[⏳ Estimated time: ~{est} sec]")
        log("-" * 50)
        log(f"[+] Running {mode} scan...\n")

        try:
            log("[🔄] Scan in progress...\n")

            scan_output = run_nmap(target, mode)
            findings = parse_nmap_output(scan_output)

            # ---- No ports ----
            if not findings:
                log("No open ports found.")
                log("System appears secure (basic scan).")
                log("-" * 50)

                log("\n[AI Summary]")
                log("No critical vulnerabilities detected. System is relatively secure.")
                log("-" * 50)

                end_time = time.time()
                total_time = round(end_time - start_time, 2)

                log(f"\n[⏱ Completed in {total_time} sec]")
                log("[✔] Scan complete. System analyzed.")

                status_label.config(text="✅ Done")
                return

            # ---- Process ports ----
            risk_count = {"High": 0, "Medium": 0, "Low": 0}

            for item in findings:
                port = item["port"]
                service = item["service"]

                # 🔥 NEW AI PROMPT (expert level)
                prompt = f"""
You are a cybersecurity expert.

Analyze:
Port {port} running {service}

Respond STRICTLY in this format:

Risk: Low/Medium/High
Impact: What could happen (short)
Reason: Why this is risky (short)
Fix: How to fix (short)
"""

                ai_output = ask_ai(prompt)
                lines = ai_output.strip().split("\n")

                risk = lines[0].replace("Risk:", "").strip() if len(lines) > 0 else "Unknown"
                impact = lines[1].replace("Impact:", "").strip() if len(lines) > 1 else "Unknown"
                reason = lines[2].replace("Reason:", "").strip() if len(lines) > 2 else "N/A"
                fix = lines[3].replace("Fix:", "").strip() if len(lines) > 3 else "Review config"

                if risk in risk_count:
                    risk_count[risk] += 1

                log(f"Port {port} ({service})")
                log(f"Risk: {risk}")
                log(f"Impact: {impact}")
                log(f"Reason: {reason}")
                log(f"Fix: {fix}")
                log("-" * 50)

            # ---- AI Summary ----
            log("\n[AI Summary]")
            log(f"High: {risk_count['High']} | Medium: {risk_count['Medium']} | Low: {risk_count['Low']}")

            if risk_count["High"] > 0:
                log("⚠️ Critical vulnerabilities detected. Immediate action required.")
            elif risk_count["Medium"] > 0:
                log("Moderate risks detected. Review recommended.")
            else:
                log("System exposure appears low.")

            log("-" * 50)

            end_time = time.time()
            total_time = round(end_time - start_time, 2)

            log(f"\n[⏱ Completed in {total_time} sec]")
            log("[✔] Scan complete. System analyzed.")

            status_label.config(text="✅ Done")

        except Exception as e:
            log(f"Error: {e}")
            status_label.config(text="❌ Error")

    else:
        log("Unknown command")
        log("Try: run nmap fast / full / aggressive / network")
        status_label.config(text="❌ Invalid command")


def run_command():
    command = entry.get().strip().lower()

    if not command:
        status_label.config(text="⚠️ Enter a command")
        return

    thread = threading.Thread(target=run_scan, args=(command,))
    thread.start()


# ================= UI =================
root = tk.Tk()
root.title("🛡️ PrivySec Desktop")
root.geometry("760x540")
root.configure(bg="#0f172a")

frame = tk.Frame(root, bg="#0f172a")
frame.pack(pady=10)

entry = tk.Entry(frame, width=55, font=("Arial", 12))
entry.pack(side=tk.LEFT, padx=5)

button = tk.Button(frame, text="Run", command=run_command,
                   bg="#22c55e", fg="white", font=("Arial", 10, "bold"))
button.pack(side=tk.LEFT)

output_box = tk.Text(root, height=27, width=92,
                     bg="#1e293b", fg="white", font=("Consolas", 10))
output_box.pack(pady=10)

status_label = tk.Label(root, text="Ready",
                        bg="#0f172a", fg="white", font=("Arial", 10))
status_label.pack(pady=5)

root.mainloop()
