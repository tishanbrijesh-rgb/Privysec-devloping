from scanner import run_nmap
from parser import parse_nmap
from ai import ask_ai


def print_header():
    print("\n" + "=" * 55)
    print("      ⚡ PRIVYSEC — SMART NETWORK SCANNER")
    print("=" * 55)


def print_section(title):
    print("\n" + "-" * 50)
    print(f" {title}")
    print("-" * 50)


# 🚀 START
print_header()

target = input("🎯 Target: ")

print("\nSelect Scan Mode:")
print("1. ⚡ Quick")
print("2. 🔍 Balanced")
print("3. 💀 Deep")
print("4. 🚀 Smart (Fast + Adaptive)")

choice = input("Choice: ")

mode_map = {
    "1": "quick",
    "2": "balanced",
    "3": "deep",
    "4": "smart",
}

mode = mode_map.get(choice, "quick")

mode_label = {
    "quick": "⚡ Quick",
    "balanced": "🔍 Balanced",
    "deep": "💀 Deep",
    "smart": "🚀 Smart"
}

use_ai = input("🤖 Use AI (y/n): ").lower()

print(f"\n⚙️ Mode Selected: {mode_label[mode]}")

print_section("🚀 Starting Scan")

output = run_nmap(target, mode)
results = parse_nmap(output)

print_section("📊 Results")

# ✅ Handle no results
if not results:
    print("❌ No open ports found")
    print_section("✅ Done")
    exit()

# 🔍 Show results
for i, r in enumerate(results, 1):
    port = r["port"]
    service = r["service"]

    print(f"\n[{i}] 🔌 {port} → {service.upper()}")

    if use_ai == "y":
        ai = ask_ai(port, service)

        print("  🔍 Service        :", ai["service"])
        print("  ⚠️ Possible Risks :", ai["risks"])
        print("  🚨 Severity       :", ai["severity"])
        print("  🛠 Recommendation :", ai["fix"])

print_section("✅ Scan Complete")
