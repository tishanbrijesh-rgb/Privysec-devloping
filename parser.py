# parser.py

import re

def parse_nmap(output):

    device = {
        "ip": "",
        "mac": "Unknown",
        "vendor": "Unknown",
        "ports": [],
        "services": [],
        "os": "Unknown"
    }

    for line in output.split("\n"):

        line = line.strip()

        # 📡 IP detection
        if "Nmap scan report for" in line:
            device["ip"] = line.split()[-1]

        # 🧬 MAC + Vendor detection
        elif "MAC Address" in line:
            match = re.search(r"MAC Address: ([\w:]+) \((.*?)\)", line)
            if match:
                device["mac"] = match.group(1)
                device["vendor"] = match.group(2)

            else:
                match = re.search(r"MAC Address: ([\w:]+)", line)
                if match:
                    device["mac"] = match.group(1)

        # 🔓 Port + Service + Version detection (🔥 IMPORTANT)
        elif "/tcp" in line and "open" in line:
            parts = line.split()

            port = parts[0]

            # Safe parsing
            service = parts[2] if len(parts) > 2 else "unknown"
            version = " ".join(parts[3:]) if len(parts) > 3 else ""

            full_service = f"{service} {version}".strip()

            device["ports"].append(port)
            device["services"].append(full_service)

        # 💻 OS detection (from -O or -sV)
        elif "OS details" in line:
            device["os"] = line.split(":", 1)[-1].strip()

        elif "Running:" in line:
            device["os"] = line.split(":", 1)[-1].strip()

    return device
