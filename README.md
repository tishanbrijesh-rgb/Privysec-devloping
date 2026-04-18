# ⚡ PRIVYSEC — Smart Network Scanner

> A lightweight IoT Discovery Agent that scans local networks, identifies devices, and provides actionable security insights using non-intrusive techniques.

---

## 📌 Overview

Modern local networks (LANs) contain multiple unknown or unmanaged devices such as laptops, phones, and IoT systems. Traditional tools like Nmap provide raw data but lack interpretation.

**PRIVYSEC bridges that gap** by transforming scan results into:
- Device identification
- Network awareness
- Security risk analysis

---

## 🚀 Key Features

- ⚡ **Fast Autonomous Discovery**
  - Automatically detects subnet
  - Finds active hosts in under 30 seconds

- 🧠 **Smart Device Fingerprinting**
  - Uses MAC address, vendor, ports, and services
  - Classifies devices (Computer, Mobile, Gateway)

- 🌐 **Network Type Detection**
  - Identifies Private LAN vs NAT/Hotspot networks

- 🔍 **Multiple Scan Modes**
  - Quick → Fast common ports
  - Balanced → Standard scan
  - Deep → Full port scan
  - Smart → Optimized aggressive scan

- 🔐 **Security Scorecard (Core Feature)**
  - Risk Level (LOW / MEDIUM / HIGH)
  - Security Score (0–100)
  - Identifies vulnerabilities
  - Provides recommendations


---

## ⚙️ How It Works

1. Detect local IP and subnet automatically  
2. Perform fast host discovery  
3. Scan selected device using Nmap  
4. Parse scan results into structured data  
5. Apply fingerprinting logic  
6. Generate a security scorecard  

---

## 🧠 Device Fingerprinting Logic

PRIVYSEC uses **multi-signal detection**:

- MAC vendor (e.g., Intel → Computer)
- Open ports (e.g., DNS → Gateway)
- Network behavior (NAT vs LAN)

### Example:

| Signal | Inference |
|------|----------|
| `.1` IP + Port 53 | Gateway / Hotspot |
| Intel Vendor | Computer |
| No ports + no MAC | Mobile / Restricted device |

---

## 🔐 Security Scorecard

Each device is evaluated for security risks.

### Output includes:

- **Risk Level**: LOW / MEDIUM / HIGH  
- **Score**: 0–100  
- **Issues**: Detected weaknesses  
- **Recommendations**: Fix suggestions  

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
