# 🛡️ NichoSec V1 – AI-Powered Local Threat Scanner

NichoSec V1 is a local AI-powered threat scanner that detects suspicious content in emails, logs, and files.  
Built in **Python** with **Streamlit**, it runs completely **offline** (no cloud storage), flags threats by severity, and exports detailed reports in **PDF** or **CSV** formats.

---

## 🚀 Features

- 📄 Scan `.eml`, `.txt`, `.log`, `.pdf`, `.docx`, `.csv`, and more
- 🤖 Uses **GPT-4o** or **GPT-3.5** for smart threat analysis
- 🟢🟡🔴 Severity indicators with reasoning and risk summary
- 🌐 Extracts and enriches IP addresses using `ipinfo.io`
- 🔐 Local-first design: no files or data leave your machine
- 📥 Email loader (Gmail IMAP beta)
- 🧹 Optional “purge” plugin to sanitize sensitive content
- 🧾 Generates reports in PDF and CSV formats
- 💬 Built-in AI assistant for threat-related Q&A

---

## 📸 Screenshots

> _Add screenshots of the UI, scan results, and PDF report here_

---

## 📂 Tech Stack

- Python 3.10+
- [Streamlit](https://streamlit.io)
- OpenAI API (GPT-4o / GPT-3.5)
- `fpdf`, `PyMuPDF`, `imaplib`, `BeautifulSoup`, `pandas`

---

## 🔧 Getting Started

1. **Clone the repo**  
   ```bash
   git clone https://github.com/AddyNicholson/NichoSec.git
   cd NichoSec
