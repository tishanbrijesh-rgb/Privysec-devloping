import subprocess
import shutil


def check_nmap():
    if not shutil.which("nmap"):
        print("❌ Nmap not installed. Run: sudo apt install nmap")
        exit()


def run_nmap(target, mode):
    check_nmap()

    if mode == "quick":
        cmd = ["nmap", "-T4", "-F", target]

    elif mode == "balanced":
        cmd = [
            "nmap", "-sS", "-sV", "-T4","-p-",
            "--min-rate", "1000",
            "--max-retries", "1",
            target
        ]

    elif mode == "deep":
        cmd = ["sudo",
            "nmap", "-sS", "-sV", "-O",
            "-T4", "-p-",
            "--min-rate", "1000",
            "--max-retries", "2",
            target
        ]

    else:
        print("❌ Invalid mode")
        return ""

    print("\n[DEBUG] Running:", " ".join(cmd))

    try:
        return subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError as e:
        return e.output
