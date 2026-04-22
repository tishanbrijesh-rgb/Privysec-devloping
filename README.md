# 🔐 PRIVYSEC

### AI-Powered Cross-Platform Network Security Analyzer

<p align="center">
  <b>Scan • Analyze • Detect • Secure</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Flask-Web%20App-black?style=for-the-badge&logo=flask">
  <img src="https://img.shields.io/badge/Nmap-Network%20Scanner-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Ollama-AI%20Local-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge">
</p>

---

## 🚀 Overview

**PRIVYSEC** is a modern cybersecurity tool that performs **network scanning, vulnerability detection, and AI-driven security analysis** through an interactive dashboard.

It integrates:

* 🔍 **Nmap scanning**
* 🧠 **Device fingerprinting**
* ⚠️ **Risk scoring**
* 💀 **CVE detection**
* 🤖 **AI-based insights (Ollama + Mistral)**
* ⚡ **Exploitability analysis**

---

## 🌍 Platform Support

| OS         | Supported | Notes                       |
| ---------- | --------- | --------------------------- |
| 🐧 Linux   | ✅ Full    | Recommended (Kali / Ubuntu) |
| 🪟 Windows | ✅ Yes     | Requires PATH setup         |
| 🍎 macOS   | ✅ Yes     | Requires Homebrew           |

---

## ✨ Features

### 🔍 1. Network Scanning

* Uses **Nmap via subprocess** 
* Modes:

  * Quick scan
  * Balanced scan
  * Deep scan (full ports + OS detection)

---

### 📡 2. Device Discovery

* Scans local subnet automatically
* Finds all active devices 

---

### 🧠 3. Device Fingerprinting

* Classifies:

  * Gateway / Router
  * IoT Devices
  * Computers
  * Mobile Devices
* Confidence-based scoring 

---

### ⚠️ 4. Risk Scoring Engine

* Score from **0–100**
* Categories:

  * LOW
  * MEDIUM
  * HIGH
* Based on exposed ports & services 

---

### 💀 5. Vulnerability Detection

* Maps ports → known CVEs
* Uses internal database 

---

### 📊 6. Attack Surface Analysis

* Calculates:

  * % High risk ports
  * % Medium risk ports
  * % Low risk ports
* Uses normalized distribution (accurate visualization)

---

### 🤖 7. AI Security Engine

Powered by **Ollama (local LLM)** 

Generates:

* Security insights
* Issues & fixes
* Human-readable explanations

---

### ⚡ 8. Exploitability Analysis

* AI determines:

  * HIGH / MEDIUM / LOW exploitability
* Explains:

  * attack vectors
  * possible exploitation paths

---

### 🛠 9. Fix Recommendation System

* Provides actionable fixes:

  * Disable services
  * Secure configurations
  * Patch vulnerabilities

---

## 🏗️ Project Structure

```bash
privysec/
│
├── app.py              # Main Flask backend
├── scanner.py          # Nmap execution
├── parser.py           # Scan parsing
├── discovery.py        # Network discovery
├── fingerprint.py      # Device classification
├── scorecard.py        # Risk scoring
├── vuln.py             # CVE detection
├── port_db.py          # Port risk database
├── network.py          # Network type detection
├── ai.py               # AI (Ollama integration)
│
├── templates/
│   ├── index.html
│   ├── devices.html
│   ├── dashboard.html
│   └── login.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

## ⚙️ Installation Guide

---

# 🐧 Linux (Kali / Ubuntu)

```bash
# Clone repository
git clone https://github.com/tishanbrijesh-rgb/H2H-Nullpointers-PrivySec.git
cd H2H-Nullpointers-PrivySec

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install Nmap
sudo apt install nmap

# Install Ollama (AI)
curl -fsSL https://ollama.com/install.sh | sh
ollama run mistral

# Run application
python app.py
```

---

# 🪟 Windows

```powershell
git clone https://github.com/tishanbrijesh-rgb/H2H-Nullpointers-PrivySec.git
cd H2H-Nullpointers-PrivySec

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
```

### Install Nmap:

* Download: https://nmap.org/download.html
* Install and add to PATH:

```
C:\Program Files (x86)\Nmap
```

### Install Ollama:

* Download: https://ollama.com/download
* Run:

```bash
ollama run mistral
```

### Run App:

```bash
python app.py
```

---

# 🍎 macOS

```bash
# Install Homebrew (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Clone repo
git clone https://github.com/tishanbrijesh-rgb/H2H-Nullpointers-PrivySec.git
cd H2H-Nullpointers-PrivySec

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install nmap
brew install nmap

# Install Ollama
brew install ollama
ollama run mistral

# Run app
python app.py
```

---

## ▶️ Access Application

Open browser:

```text
http://127.0.0.1:5000
```

---

## 🔐 Default Login

```text
Username: admin
Password: admin
```

---

## 🧠 Workflow

1. Discover devices on network
2. Select target
3. Run scan (Quick / Balanced / Deep)
4. System processes:

   * Parsing
   * Classification
   * Risk scoring
   * CVE detection
5. AI generates:

   * Security insight
   * Exploitability analysis
6. Dashboard displays results

---

## 📸 Screenshots

*(Add images here for GitHub impact)*

---

## ⚠️ Known Issues

* Nmap must be installed and accessible in PATH
* AI requires Ollama running locally
* Windows may need manual PATH configuration

---

## ⚠️ Disclaimer

This tool is for:

✔ Educational use
✔ Authorized penetration testing

❌ Do NOT use on unauthorized networks

---

## 👨‍💻 Author

**Tishan Kumar B**
Cybersecurity Student

---

## 🏷️ Watermark

<p align="center">
  <b>⚡ PRIVYSEC // Built by Tishan Kumar ⚡</b>
</p>

---

## ⭐ Support

If you found this useful:

⭐ Star the repository
🔁 Share it
🛠 Contribute

---
