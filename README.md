# Deception Based Security Mechanism (Honeypot Login System)

## 📌 Project Overview
This project implements a deception-based security mechanism using a fake login interface (honeypot).  
The system is designed to detect unauthorized access attempts by capturing user inputs and marking them as suspicious activity.

---

## 🎯 Objective
- Create a fake login system to trap attackers
- Detect unauthorized login attempts
- Monitor and log suspicious activity

---

## ⚙️ Technologies Used
- Python
- Flask
- HTML
- JSON

---

## 🧠 How It Works
1. A fake admin login page is displayed.
2. User enters username and password.
3. System does not allow login and shows "Invalid Credentials".
4. The entered data is captured and stored in a log file.
5. The activity is marked as suspicious.

---

## 📂 Project Structure
task3_deception/

honeypot_logs.json

login.html

##

app.py

templates/

- README.md
- ---

## 🚀 Features
- Fake login interface
- Captures user credentials
- Logs suspicious activity
- Simple monitoring system

---

## 🧪 Example Output
When a user attempts to log in:

- Output: `Invalid Credentials`
- Log File Stores:
  - Username
  - Password
  - IP Address
  - Timestamp
  - Status (Suspicious)

---

## ⚠️ Note
This is a simulated system for educational purposes only.

---

## 📌 Conclusion
This project demonstrates how deception techniques can be used in cybersecurity to detect and analyze malicious behavior.
