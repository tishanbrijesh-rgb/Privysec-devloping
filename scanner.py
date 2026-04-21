# scanner.py

import subprocess

def run_nmap(target, mode):

    if mode == "quick":
        cmd = ["nmap", "-T4", "-F", target]

    elif mode == "balanced":
        cmd = ["nmap", "-sS", "-sV", "-T4", target]

    elif mode == "deep":
        cmd = ["nmap", "-sS", "-sV", "-O", "-T4", "-p-", target]

    else:
        cmd = ["nmap", "-T4", "-F", target]

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        return ""

    return result.stdout
