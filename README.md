# Elimuhub Event Messaging — Automated Event Messaging System

This repo provides a complete solution to send scheduled Emails and WhatsApp messages to contacts for Islamic education events (e.g., Education Fair 2025).

## Features
- Upload contacts CSV (email, WhatsApp, preferred time, message)
- Schedule & send Emails and WhatsApp messages using your SMTP & Twilio/UltraMsg credentials
- Simple, beginner-friendly UI for uploading and previewing messages
- Message logs and compliance notes

## Quickstart

1. **Clone repo:**  
   `git clone https://github.com/kibiti/elimuhub-event-messaging.git && cd elimuhub-event-messaging`
2. **Copy `.env.example` to `.env` and fill all UPPERCASE placeholders**
3. **Create virtualenv and install dependencies:**  
   `./run.sh`
4. **Start app:**  
   `flask run` or `./run.sh`
5. **Open browser:**  
   [http://localhost:5000](http://localhost:5000)
6. **Upload contacts CSV** (see `contacts_examples/sample_contacts.csv`)

## CSV Format

See `contacts_examples/sample_contacts.csv`.  
Required headers: `name,email,phone,whatsapp_number,send_email,send_whatsapp,preferred_time,message`

## Providers

- **Email:** SMTP (Gmail, SendGrid, etc.)
- **WhatsApp:** Twilio or UltraMsg

## Fill-in checklist (ALL MUST BE FILLED)

- `.env`: SMTP, Twilio/UltraMsg, FLASK_SECRET, DEFAULT_SCHEDULE_DATETIME
- `contacts_examples/sample_contacts.csv`: Use real contacts (+2547XXXXXXXX), customize messages & opt-out wording

## Compliance

- Only message contacts who have consented.
- Include opt-out/STOP instructions in your message.

---

## Repo Structure

```
elimuhub-event-messaging/
├── README.md
├── requirements.txt
├── .env.example
├── config.example.py
├── run.sh
├── Dockerfile
├── procfile
├── contacts_examples/
│   └── sample_contacts.csv
├── app/
│   ├── __init__.py
│   ├── app.py
│   ├── scheduler.py
│   ├── utils.py
│   ├── messaging/
│   │   ├── __init__.py
│   │   ├── emailer.py
│   │   └── whatsapp.py
│   └── templates/
│       ├── index.html
│       └── preview.html
└── logs/
    └── messages.log    # created at runtime
```

---

## How to push to GitHub

```sh
mkdir elimuhub-event-messaging
cd elimuhub-event-messaging
# Add files (copy-paste from below)
git init
git add .
git commit -m "Initial commit – automated messaging system"
git remote add origin https://github.com/kibiti/elimuhub-event-messaging.git
git branch -M main
git push -u origin main
```
