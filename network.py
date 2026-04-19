import ipaddress


def detect_network_type(device):
    ip = device.get("ip", "")
    mac = device.get("mac", "Unknown")

    try:
        ip_obj = ipaddress.ip_address(ip)
    except:
        return "Unknown"

    if ip_obj.is_private:
        return "Private NAT / Hotspot Network" if mac == "Unknown" else "Private LAN Network"

    return "Public Network"
