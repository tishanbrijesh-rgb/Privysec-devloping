import re

COMMON_PORTS = {
    "21/tcp": "FTP",
    "22/tcp": "SSH",
    "23/tcp": "Telnet",
    "53/tcp": "DNS",
    "80/tcp": "HTTP",
    "443/tcp": "HTTPS",
    "554/tcp": "RTSP",
    "8080/tcp": "HTTP-Proxy",
}

def parse_nmap(output):

    device = {
        "ip": "",
        "mac": "Unknown",
        "vendor": "Unknown",
        "ports": [],
        "services": []
    }

    for line in output.split("\n"):

        if "Nmap scan report for" in line:
            device["ip"] = line.split()[-1]

        elif "MAC Address" in line:
            match = re.search(r"MAC Address: ([\w:]+)", line)
            if match:
                device["mac"] = match.group(1)

        elif "/tcp" in line and "open" in line:
            port = line.split()[0]

            if port.startswith("49"):
                service = "Dynamic Port"
            else:
                service = COMMON_PORTS.get(port, "Unknown Service")

            device["ports"].append(port)
            device["services"].append(service)

    return device
