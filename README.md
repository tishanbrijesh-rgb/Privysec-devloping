# 🛰️ PRIVYSEC — Intelligent IoT Discovery Agent

> **"From unknown devices to actionable security insights — instantly."**

---

## 🚨 Problem Statement

Modern networks are filled with IoT devices like cameras, routers, printers, and smart TVs.
Most users **do not know**:

* What devices are connected
* What services they expose
* How vulnerable they are

This lack of visibility creates a **major security risk**.

---

## 💡 Proposed Solution

**PRIVYSEC** is an intelligent IoT Discovery Agent that:

* Automatically scans your local network
* Identifies active devices
* Classifies them using fingerprinting logic
* Detects vulnerabilities based on open ports
* Assigns a **security score**
* Provides **actionable fixes**

👉 It transforms raw network data into **clear, human-readable security intelligence**

---

## ⚙️ Tech Stack

* **Backend:** Python (Flask)
* **Scanning Engine:** Nmap
* **Frontend:** HTML, CSS (Cyberpunk UI)
* **Logic Modules:**

  * Device Fingerprinting Engine
  * Risk Scoring System
  * CVE Detection Engine

---

## 🚀 Features

### 🔍 Network Discovery

* Automatically scans LAN for active hosts

### 🧠 Smart Device Fingerprinting

* Classifies devices:

  * Router / Gateway
  * IoT Devices
  * Computers
  * Mobile Devices

### 🔐 Security Scorecard

* Assigns score (0–100)
* Risk Levels:

  * LOW
  * MEDIUM
  * HIGH

### ☠️ Vulnerability Detection

* Maps open ports to known CVEs
* Highlights risky services like:

  * Telnet
  * FTP
  * SMB

### 📊 Attack Surface Analysis

* Shows:

  * High-risk ports
  * Medium-risk ports
  * Low-risk ports

### 📈 Risk Visualization (NEW 🔥)

* Color-based risk bars
* Risk distribution chart

### 🚨 Most Dangerous Device (NEW 🔥)

* Automatically highlights:

  * Highest risk device
  * Risk score
  * Open ports
  * Reason for risk

### 🧾 Scan History

* Stores last 10 scans

---

## 🏗️ Architecture / Flow

User Input (Target IP / Scan)
        ↓
Network Discovery (Nmap)
        ↓
Parser → Extract Ports, Services, OS
        ↓
Fingerprint Engine → Device Type
        ↓
Score Engine → Risk + Issues + Fixes
        ↓
Vulnerability Engine → CVE Detection
        ↓
Dashboard Visualization
```

---


## 🚀 Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/privysec.git
cd privysec
```

---

### 2. Create Virtual Environment (Recommended)

```bash
python3 -m venv venv
```

---

### 3. Activate Virtual Environment

#### On Linux / macOS:

```bash
source venv/bin/activate
```

#### On Windows:

```bash
venv\Scripts\activate
```

---

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Setup Environment Variables

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_api_key_here
```

---

### 6. Run the Application

```bash
python app.py
```

---

### 7. Open in Browser

```
http://127.0.0.1:5000
```

---

## ⚠️ Notes

* Make sure Nmap is installed on your system:

```bash
sudo apt install nmap
```

* Do NOT upload your `.env` file to GitHub.

* Always activate the virtual environment before running the app.

---

## 🧠 Features

* 🔍 Network Scanning (Nmap)
* 🧠 Device Fingerprinting
* 📊 Risk Scoring System
* 🚨 Attack Surface Analysis
* 🛠 AI-Generated Issues & Fixes
* 🤖 AI Security Insights
* 📜 Scan History

---
snapshorts 
<img width="1920" height="1200" alt="image" src="https://github.com/user-attachments/assets/4e5a4f07-6aba-4787-986e-e18c66f1b296" />

