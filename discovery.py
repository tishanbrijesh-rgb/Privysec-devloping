import subprocess
import socket

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

def get_subnet(ip):
    return ".".join(ip.split(".")[:3]) + ".0/24"

def discover_hosts():

    ip = get_local_ip()
    subnet = get_subnet(ip)

    cmd = [
        "nmap", "-sn",
        "--min-rate", "500",
        "--max-retries", "1",
        subnet
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    hosts = []

    for line in result.stdout.split("\n"):
        if "Nmap scan report for" in line:
            hosts.append(line.split()[-1])

    return hosts
