def parse_nmap_output(output):
    findings = []

    for line in output.split("\n"):
        if "/tcp" in line and "open" in line:
            parts = line.split()
            port = parts[0].split("/")[0]
            service = parts[2] if len(parts) > 2 else "unknown"

            findings.append({
                "port": port,
                "service": service
            })

    return findings


# 🔥 NEW: Network parser
def parse_network_output(output):
    devices = []

    for line in output.split("\n"):
        if "Nmap scan report for" in line:
            device = line.split("for")[-1].strip()
            devices.append(device)

    return devices
