# 📦 Syntecxhub Folder Backup Tool Ultra

An advanced Python-based backup and synchronization utility designed for secure, automated, and compressed folder backups with logging, hashing, and multi-threaded performance.

---

## 🚀 Features

- 📂 Folder Backup Automation
- ⚡ Multi-threaded File Copy
- 🕒 Timestamped Backups
- 📦 ZIP Compression
- 🔐 SHA256 File Integrity Verification
- 🧠 Incremental Backup Detection
- 📝 Logging System
- 🛡️ Error Handling
- 💻 CLI Arguments
- 🔄 Recursive Folder Sync
- 🚀 Fast Performance
- 📊 Backup Statistics
- 🧪 Dry Run Mode
- 🔥 Professional Sysadmin Utility

---

## 🧠 How It Works

The tool:

- Scans the source folder
- Detects changed/new files
- Copies files into timestamped backups
- Verifies file integrity using SHA256 hashes
- Compresses backups into ZIP archives
- Logs all backup activities
- Generates backup statistics

---

## ▶️ Installation

pip3 install colorama

---

## ▶️ Run

python3 backup_ultra.py -s test_source -d test_backup --compress

---

## 🧪 Dry Run Mode

python3 backup_ultra.py -s test_source -d test_backup --dry-run

---

## 📊 Example Output

🚀 BACKUP ENGINE STARTED

✔ Copied: test_source/file1.txt
✔ Copied: test_source/file2.txt

===== BACKUP SUMMARY =====

Total Files Scanned : 2
Files Backed Up     : 2

📦 Compressed: backup_20260526.zip

---

## 📁 Project Structure

backup_ultra.py
README.md
requirements.txt
.gitignore
test_source/
test_backup/

---

## ⚠️ Disclaimer

This project is for educational purposes only.

--- 

## 👨‍💻 Author

Sonu Kumar
https://github.com/whoami-sonu

--- 

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!













pip3 install colorama
