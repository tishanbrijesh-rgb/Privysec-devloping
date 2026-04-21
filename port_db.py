PORT_DB = {

    "21/tcp": {
        "service": "FTP",
        "issue": "FTP exposed (insecure authentication)",
        "fix": "Disable FTP or use SFTP",
        "cve": "CVE-1999-0497 → Anonymous FTP login"
    },

    "22/tcp": {
        "service": "SSH",
        "issue": "SSH exposed (brute-force risk)",
        "fix": "Use key-based auth & disable root login",
        "cve": "CVE-2018-15473 → OpenSSH user enumeration"
    },

    "23/tcp": {
        "service": "Telnet",
        "issue": "Telnet exposed (plaintext credentials)",
        "fix": "Disable Telnet, use SSH",
        "cve": "CVE-2001-0554 → Telnet vulnerability"
    },

    "53/tcp": {
        "service": "DNS",
        "issue": "DNS service exposed",
        "fix": "Restrict DNS & enable DNSSEC",
        "cve": "CVE-2020-8616 → DNS cache poisoning"
    },

    "80/tcp": {
        "service": "HTTP",
        "issue": "HTTP exposed (unencrypted traffic)",
        "fix": "Use HTTPS",
        "cve": "CVE-2019-11043 → PHP-FPM RCE"
    },

    "443/tcp": {
        "service": "HTTPS",
        "issue": "HTTPS exposed",
        "fix": "Ensure TLS is updated",
        "cve": "CVE-2021-3449 → OpenSSL DoS"
    },

    "445/tcp": {
        "service": "SMB",
        "issue": "SMB exposed (wormable attack risk)",
        "fix": "Disable SMBv1 & restrict access",
        "cve": "CVE-2017-0144 → EternalBlue"
    },

    "3389/tcp": {
        "service": "RDP",
        "issue": "RDP exposed (brute-force risk)",
        "fix": "Use VPN & restrict access",
        "cve": "CVE-2019-0708 → BlueKeep"
    },

    "3306/tcp": {
        "service": "MySQL",
        "issue": "Database exposed",
        "fix": "Bind to localhost & secure credentials",
        "cve": "CVE-2012-2122 → MySQL auth bypass"
    },

    "5432/tcp": {
        "service": "PostgreSQL",
        "issue": "Database exposed",
        "fix": "Restrict external access",
        "cve": "CVE-2018-1058 → privilege escalation"
    },

    "6379/tcp": {
        "service": "Redis",
        "issue": "Redis exposed (no auth risk)",
        "fix": "Enable authentication & firewall",
        "cve": "CVE-2022-0543 → Redis RCE"
    },

    "27017/tcp": {
        "service": "MongoDB",
        "issue": "MongoDB exposed (data leak risk)",
        "fix": "Enable auth & restrict access",
        "cve": "CVE-2019-10758 → NoSQL injection"
    },

    "5000/tcp": {
        "service": "Flask Dev Server",
        "issue": "Flask debug server exposed",
        "fix": "Disable debug mode",
        "cve": "DEBUG MODE → remote code execution risk"
    },

    "3000/tcp": {
        "service": "Node Dev Server",
        "issue": "Node dev server exposed",
        "fix": "Restrict access",
        "cve": "DEV SERVER → attack surface"
    }

}
