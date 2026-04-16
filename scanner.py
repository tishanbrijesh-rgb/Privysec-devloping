import subprocess

def run_nmap(target, mode="fast"):
    try:
        if mode == "fast":
            cmd = ["nmap", "-F", target]

        elif mode == "full":
            cmd = ["nmap", "-p-", target]

        elif mode == "elite_lite":
            # ⚡ Fast + all ports + OS guess
            cmd = ["sudo", "nmap", "-O", "--osscan-guess", "-T4", "-p-", target]

        elif mode == "elite_full":
            # 🔥 Deep scan (best)
            cmd = ["sudo", "nmap", "-A", "--osscan-guess", "-p-", "-T4", target]

        else:
            cmd = ["nmap", target]

        print(f"[DEBUG] Running: {' '.join(cmd)}")

        result = subprocess.run(cmd, capture_output=True, text=True)

        return result.stdout

    except Exception as e:
        return f"Error: {e}"
