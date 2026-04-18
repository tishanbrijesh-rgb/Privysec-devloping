from scanner import run_nmap
from parser import parse_nmap
from ai import ask_ai


def print_header():
    print("\n" + "="*55)
    print("      ⚡ PRIVYSEC — SMART NETWORK SCANNER")
    print("="*55)


def print_section(title):
    print("\n" + "-"*50)
    print(f" {title}")
    print("-"*50)


print_header()

target = input("🎯 Target: ")

print("\n1. ⚡ Quick\n2. 🔍 Balanced\n3. 💀 Deep")
choice = input("Choice: ")

mode = {"1": "quick", "2": "balanced", "3": "deep"}.get(choice, "quick")

use_ai = input("🤖 Use AI (y/n): ").lower()

print_section("🚀 Starting Scan")

output = run_nmap(target, mode)
results = parse_nmap(output)

print_section("📊 Results")

for i, r in enumerate(results, 1):
    port = r["port"]
    service = r["service"]

    print(f"\n[{i}] {port} → {service.upper()}")

    if use_ai == "y":
        ai = ask_ai(port, service)

        print("  🔍 Service:", ai["service"])
        print("  ⚠️ Possible Risks:", ai["risks"])
        print("  🚨 Severity:", ai["severity"])
        print("  🛠 Recommendation:", ai["fix"])

print_section("✅ Done")
