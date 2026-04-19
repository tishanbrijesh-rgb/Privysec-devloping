from scanner import run_nmap
from parser import parse_nmap
from discovery import discover_hosts
from fingerprint import classify_device
from network import detect_network_type
from scorecard import calculate_score
from ai import ask_ai


def print_header():
    print("\n" + "=" * 55)
    print("      ⚡ PRIVYSEC — SMART NETWORK SCANNER")
    print("=" * 55)


def print_section(title):
    print("\n" + "-" * 50)
    print(f" {title}")
    print("-" * 50)


def main():
    print_header()

    hosts = discover_hosts()

    if not hosts:
        print("❌ No devices found")
        return

    print("\n📡 Active Devices:")
    for i, h in enumerate(hosts, 1):
        print(f"[{i}] {h['ip']} ({h['hostname']})")

    try:
        choice = int(input("\nSelect device to scan: "))
        target = hosts[choice - 1]["ip"]
    except:
        print("❌ Invalid selection")
        return

    print("\nSelect Scan Mode:")
    print("1. ⚡ Quick")
    print("2. 🔍 Balanced")
    print("3. 💀 Deep")
    print("4. 🚀 Smart")

    mode_map = {"1": "quick", "2": "balanced", "3": "deep", "4": "smart"}
    mode = mode_map.get(input("Choice: "), "quick")

    use_ai = input("🤖 Use AI (y/n): ").lower()

    print_section("🚀 Starting Scan")

    output = run_nmap(target, mode)
    device = parse_nmap(output)

    print_section("📊 Device Info")

    print(f"IP       : {device['ip']}")
    print(f"MAC      : {device['mac']}")
    print(f"Vendor   : {device['vendor']}")

    network_type = detect_network_type(device)
    print("\n🌐 Network Info")
    print(f"Type     : {network_type}")

    print("\n🔌 Open Ports:")
    if not device["ports"]:
        print("  ❌ No open ports found")
    else:
        for p, s in zip(device["ports"], device["services"]):
            print(f"  {p} → {s}")

            if use_ai == "y":
                ai = ask_ai(p, s)
                print("    ⚠️", ai["risks"])

    # 🧠 Fingerprinting
    device_type, reasons, confidence = classify_device(device)

    print("\n🧠 Device Classification")
    print(f"Type       : {device_type}")
    print(f"Confidence : {confidence}%")
    for r in reasons:
        print(f"  - {r}")

    # 🔐 Scorecard
    score, risk, issues, fixes = calculate_score(device)

    print("\n🔐 Security Scorecard")
    print(f"Risk Level : {risk}")
    print(f"Score      : {score}/100")

    print("\n⚠️ Issues:")
    if not issues:
        print("  ✅ No major issues found")
    else:
        for i in issues:
            print(f"  - {i}")

    print("\n🛠 Recommendations:")
    if not fixes:
        print("  ✅ No action needed")
    else:
        for f in fixes:
            print(f"  - {f}")

    print_section("✅ Scan Complete")


if __name__ == "__main__":
    main()
