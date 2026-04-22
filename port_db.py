PORT_DB = {

    # 🔴 HIGH RISK PORTS
    "23/tcp": {
        "service": "Telnet",
        "risk": "HIGH",
        "issue": "Telnet exposed (plaintext credentials)",
        "fix": "Disable Telnet and use SSH",
        "cve": "CVE-2001-0554 → Telnet vulnerability"
    },

    "445/tcp": {
        "service": "SMB",
        "risk": "HIGH",
        "issue": "SMB exposed (wormable attack risk)",
        "fix": "Disable SMBv1 and restrict access",
        "cve": "CVE-2017-0144 → EternalBlue"
    },

    "3389/tcp": {
        "service": "RDP",
        "risk": "HIGH",
        "issue": "RDP exposed (brute-force risk)",
        "fix": "Use VPN and restrict access",
        "cve": "CVE-2019-0708 → BlueKeep"
    },


    # 🟠 MEDIUM RISK PORTS
    "21/tcp": {
        "service": "FTP",
        "risk": "MEDIUM",
        "issue": "FTP exposed (insecure authentication)",
        "fix": "Use SFTP instead of FTP",
        "cve": "CVE-1999-0497 → Anonymous FTP login"
    },

    "22/tcp": {
        "service": "SSH",
        "risk": "MEDIUM",
        "issue": "SSH exposed (brute-force risk)",
        "fix": "Use key-based authentication",
        "cve": "CVE-2018-15473 → OpenSSH enumeration"
    },

    "53/tcp": {
        "service": "DNS",
        "risk": "MEDIUM",
        "issue": "DNS exposed (cache poisoning risk)",
        "fix": "Restrict DNS and enable DNSSEC",
        "cve": "CVE-2020-8616 → DNS cache poisoning"
    },

    "80/tcp": {
        "service": "HTTP",
        "risk": "MEDIUM",
        "issue": "HTTP exposed (unencrypted traffic)",
        "fix": "Use HTTPS",
        "cve": "CVE-2019-11043 → PHP-FPM RCE"
    },

    "3306/tcp": {
        "service": "MySQL",
        "risk": "MEDIUM",
        "issue": "Database exposed",
        "fix": "Bind to localhost and secure credentials",
        "cve": "CVE-2012-2122 → MySQL auth bypass"
    },

    "5432/tcp": {
        "service": "PostgreSQL",
        "risk": "MEDIUM",
        "issue": "Database exposed",
        "fix": "Restrict external access",
        "cve": "CVE-2018-1058 → privilege escalation"
    },

    "6379/tcp": {
        "service": "Redis",
        "risk": "MEDIUM",
        "issue": "Redis exposed (no authentication)",
        "fix": "Enable authentication and firewall",
        "cve": "CVE-2022-0543 → Redis RCE"
    },

    "27017/tcp": {
        "service": "MongoDB",
        "risk": "MEDIUM",
        "issue": "MongoDB exposed (data leak risk)",
        "fix": "Enable authentication",
        "cve": "CVE-2019-10758 → NoSQL injection"
    },


    # 🟢 LOW RISK PORTS
    "443/tcp": {
        "service": "HTTPS",
        "risk": "LOW",
        "issue": "HTTPS exposed",
        "fix": "Ensure TLS is updated",
        "cve": "CVE-2021-3449 → OpenSSL DoS"
    },


    # 🟡 DEV / OTHER PORTS
    "5000/tcp": {
        "service": "Flask Dev Server",
        "risk": "MEDIUM",
        "issue": "Flask debug server exposed",
        "fix": "Disable debug mode",
        "cve": "Debug mode → RCE risk"
    },

    "3000/tcp": {
        "service": "Node Dev Server",
        "risk": "LOW",
        "issue": "Dev server exposed",
        "fix": "Restrict access",
        "cve": "Dev exposure risk"
    }

}
