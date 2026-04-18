import re


def parse_nmap(output):
    results = []

    pattern = r"(\d+/tcp)\s+open\s+([\w\-]+)\s*(.*)"

    matches = re.findall(pattern, output)

    for port, service, extra in matches:
        full_service = f"{service} {extra}".strip()
        results.append({
            "port": port,
            "service": full_service if full_service else "unknown"
        })

    return results
