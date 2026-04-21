from port_db import PORT_DB

def detect_vulns(device):

    ports = device.get("ports", [])
    vulns = []

    for p in ports:
        if p in PORT_DB:
            vulns.append(PORT_DB[p]["cve"])

    return vulns
