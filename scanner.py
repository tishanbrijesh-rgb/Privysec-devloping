import subprocess


def run_nmap(target, mode):
    if mode == "quick":
        cmd = ["nmap", "-T4", "-F", target]

    elif mode == "balanced":
        cmd = ["nmap", "-sS","-p-", "-T4", target]

    elif mode == "deep":
        cmd = ["nmap", "-sS", "-sV", "-T4", "-p-", target]

    else:
        cmd = ["nmap", "-sS", "-sV", "-T4", "-p-", "--min-rate", "1000", target]

    print(f"[DEBUG] Running: {' '.join(cmd)}")

    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout
