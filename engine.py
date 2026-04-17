import subprocess
import time


def run_nmap(cmd):
    try:
        return subprocess.check_output(cmd, stderr=subprocess.STDOUT).decode()
    except Exception as e:
        return str(e)


def parse_nmap(output):
    results = []

    for line in output.split("\n"):
        if "/tcp" in line and "open" in line:
            parts = line.split()
            port = parts[0].split("/")[0]
            service = parts[2] if len(parts) > 2 else "unknown"

            results.append({
                "port": port,
                "service": service
            })

    return results


def scan_system(target, mode):
    start = time.time()

    if mode == "fast":
        cmd = ["nmap", "-F", target]
    elif mode == "full":
        cmd = ["nmap", "-p-", target]
    else:
        cmd = ["nmap", "-A", target]

    output = run_nmap(cmd)
    results = parse_nmap(output)

    end = time.time()

    return {
        "results": results,
        "time": round(end - start, 2)
    }


def scan_network():
    start = time.time()

    cmd = ["nmap", "-sn", "192.168.1.0/24"]
    output = run_nmap(cmd)

    devices = []
    for line in output.split("\n"):
        if "Nmap scan report for" in line:
            devices.append(line.split()[-1])

    end = time.time()

    return {
        "devices": devices,
        "time": round(end - start, 2)
    }
