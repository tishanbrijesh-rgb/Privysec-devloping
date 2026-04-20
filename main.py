from discovery import discover_hosts
from scanner import run_nmap
from parser import parse_nmap
from fingerprint import classify_device
from scorecard import calculate_score

def print_header():
    print("="*50)
    print("⚡ PRIVYSEC — SMART NETWORK SCANNER")
    print("="*50)

def main():
    print_header()

    hosts = discover_hosts()

    if not hosts:
        print("No devices found.")
        return

    print("\n📡 Active Devices:")
    for i, host in enumerate(hosts):
        print(f"[{i+1}] {host}")

    choice = int(input("\nSelect device: ")) - 1
    target = hosts[choice]

    print("\nSelect mode:")
    print("1. Quick\n2. Balanced\n3. Deep")

    mode_map = {1: "quick", 2: "balanced", 3: "deep"}
    mode = mode_map[int(input("Choice: "))]

    print("\n🚀 Scanning...\n")

    output = run_nmap(target, mode)
    device = parse_nmap(output)

    print("📊 Device Info")
    print(f"IP      : {device['ip']}")
    print(f"MAC     : {device['mac']}")

    print("\n🔓 Open Ports:")
    if device["ports"]:
        for p, s in zip(device["ports"], device["services"]):
            print(f"- {p} ({s})")
    else:
        print("- No open ports")

    # Fingerprinting
    dtype, confidence, reasons = classify_device(device)

    print("\n🧠 Device Classification")
    print(f"Type       : {dtype}")
    print(f"Confidence : {confidence}%")

    print("Based on:")
    for r in reasons:
        print(f"- {r}")

    # Behavior analysis
    print("\n🧠 Behavior Analysis:")
    if "53/tcp" in device["ports"]:
        print("- Acts as DNS provider → likely gateway")
    if not device["ports"]:
        print("- No inbound services → NAT/firewall protected")

    # Scorecard
    score, risk, issues, fixes = calculate_score(device)

    print("\n🔐 Security Scorecard")
    print(f"Risk Level : {risk}")
    print(f"Score      : {score}/100")

    if issues:
        print("\n⚠️ Issues:")
        for i in issues:
            print(f"- {i}")

        print("\n🛠 Fixes:")
        for f in fixes:
            print(f"- {f}")

    print("\n✅ Scan Complete")

if __name__ == "__main__":
    main()
