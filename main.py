from scanner import run_nmap
from parser import parse_nmap_output
from ai import ask_ai
import json

def analyze_fallback(port, service):
    data = {
        "22": ("Medium", "SSH exposed. Use keys."),
        "80": ("Low", "HTTP open. Avoid sensitive data."),
        "443": ("Low", "HTTPS active. Check SSL."),
        "21": ("High", "FTP insecure. Disable if unused."),
        "8000": ("Low", "Local server. Use carefully."),
        "tcpwrapped": ("Medium", "Filtered service. Check firewall.")
    }

    if port in data:
        return data[port]

    if service in data:
        return data[service]

    return ("Unknown", f"{service} on port {port}. Review config.")


def main():
    print("=== PrivySec FINAL ===")

    target = input("Enter target (localhost or IP): ")
    mode = input("Select mode (fast/full/aggressive): ").lower()
    use_ai = input("Use AI? (y/n): ").lower()

    output = run_nmap(target, mode)

    if "Error" in output:
        print(output)
        return

    findings = parse_nmap_output(output)

    if not findings:
        print("No open ports found.")
        return

    print("\n[+] Scan Results:\n")

    results = []

    for item in findings:
        port = item["port"]
        service = item["service"]

        if use_ai == "y":
            prompt = f"""
Port {port} running {service}.

Give output STRICTLY in this format:
Risk: Low/Medium/High
Reason: One short sentence
Fix: One short action

Keep under 30 words.
"""
            ai_output = ask_ai(prompt)

            if "Error" in ai_output or len(ai_output.strip()) < 10:
                risk, message = analyze_fallback(port, service)
                reason = message
                fix = "Review configuration"
            else:
                lines = ai_output.strip().split("\n")

                # safe parsing
                risk = lines[0].replace("Risk:", "").strip() if len(lines) > 0 else "AI"
                reason = lines[1].replace("Reason:", "").strip() if len(lines) > 1 else "N/A"
                fix = lines[2].replace("Fix:", "").strip() if len(lines) > 2 else "N/A"

        else:
            risk, reason = analyze_fallback(port, service)
            fix = "Review configuration"

        print(f"Port: {port} | Service: {service}")
        print(f"Risk: {risk}")
        print(f"Reason: {reason}")
        print(f"Fix: {fix}")
        print("-" * 50)

        results.append({
            "port": port,
            "service": service,
            "risk": risk,
            "reason": reason,
            "fix": fix
        })

    # Save report
    with open("report.json", "w") as f:
        json.dump(results, f, indent=4)

    print("\n[+] Report saved as report.json")


if __name__ == "__main__":
    main()
