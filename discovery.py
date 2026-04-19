import subprocess
import socket
import time


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


def get_subnet(ip):
    return ".".join(ip.split(".")[:3]) + ".0/28"


def discover_hosts():
    ip = get_local_ip()
    subnet = get_subnet(ip)

    print(f"\n⚡ Fast discovery (max 30 sec)...")

    cmd = [
        "nmap", "-sn", "-n", "-T5",
        "--max-retries", "0",
        "--host-timeout", "2s",
        subnet
    ]

    start = time.time()

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=30
    )

    output = result.stdout
    elapsed = round(time.time() - start, 2)

    hosts = []
    ip = None

    for line in output.split("\n"):
        if "Nmap scan report for" in line:
            ip = line.split()[-1]
        elif "Host is up" in line and ip:
            hosts.append({"ip": ip, "hostname": "unknown"})

    print(f"⚡ Found {len(hosts)} hosts in {elapsed}s")

    return hosts
