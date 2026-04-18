import subprocess
import shutil


def check_nmap():
    if not shutil.which("nmap"):
        print("❌ Nmap not installed. Run: sudo apt install nmap")
        exit()


def smart_scan(target):
    print("\n⚡ Phase 1: Fast scan...")

    fast_cmd = [
        "nmap",
        "-T4",
        "-F",                 # fast scan
        "--open",
        "--min-rate", "100",
        target
    ]

    fast_output = subprocess.getoutput(" ".join(fast_cmd))

    open_ports = []
    for line in fast_output.split("\n"):
        if "/tcp" in line and "open" in line:
            port = line.split("/")[0]
            open_ports.append(port)

    # ✅ If ports found → deep scan
    if open_ports:
        print(f"🔍 Found open ports: {', '.join(open_ports)}")

        print("\n🔍 Phase 2: Deep scan on found ports...")

        ports_str = ",".join(open_ports)

        deep_cmd = [
            "nmap",
            "-sS",
            "-sV",
            "-T4",
            "-p", ports_str,
            "--max-retries", "1",
            target
        ]

        return subprocess.getoutput(" ".join(deep_cmd))

    # ❗ If nothing found → fallback full scan
    print("⚠️ No ports found, switching to full scan...")

    fallback_cmd = [
        "nmap",
        "-sS",
        "-sV",
        "-T4",
        "-p-",                # full scan
        "--min-rate", "100",
        "--max-retries", "1",
        "--open",
        target
    ]

    return subprocess.getoutput(" ".join(fallback_cmd))


def run_nmap(target, mode):
    check_nmap()

    if mode == "quick":
        cmd = ["nmap", "-T4", "-F", target]

    elif mode == "balanced":
        cmd = [
            "nmap", "-sS", "-sV", "-T4", "-p-",
            "--min-rate", "1000",
            "--max-retries", "1",
            target
        ]

    elif mode == "deep":
        cmd = [
            "sudo",
            "nmap", "-sS", "-sV", "-O",
            "-T4", "-p-",
            "--min-rate", "1000",
            "--max-retries", "2",
            target
        ]

    elif mode == "smart":
        return smart_scan(target)

    else:
        print("❌ Invalid mode")
        return ""

    print("\n[DEBUG] Running:", " ".join(cmd))

    try:
        return subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError as e:
        return e.output
