import re


def parse_nmap(output):
    device = {
        "ip": None,
        "mac": "Unknown",
        "vendor": "Unknown",
        "ports": [],
        "services": []
    }

    for line in output.split("\n"):
        line = line.strip()

        if "Nmap scan report for" in line:
            device["ip"] = line.split()[-1]

        elif "MAC Address:" in line:
            match = re.search(r"MAC Address: ([\w:]+) \((.*?)\)", line)
            if match:
                device["mac"] = match.group(1)
                device["vendor"] = match.group(2)

        elif "/tcp" in line and "open" in line:
            parts = line.split()
            device["ports"].append(parts[0])
            device["services"].append(parts[2] if len(parts) > 2 else "unknown")

    return device
