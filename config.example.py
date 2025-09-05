import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    SMTP_HOST = os.getenv("SMTP_HOST")
    SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
    SMTP_USER = os.getenv("SMTP_USER")
    SMTP_PASS = os.getenv("SMTP_PASS")
    FROM_EMAIL = os.getenv("FROM_EMAIL")

    TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
    TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
    TWILIO_WHATSAPP_FROM = os.getenv("TWILIO_WHATSAPP_FROM")

    ULTRAMSG_TOKEN = os.getenv("ULTRAMSG_TOKEN")
    ULTRAMSG_INSTANCE = os.getenv("ULTRAMSG_INSTANCE")

    LOG_PATH = os.getenv("LOG_PATH", "./logs/messages.log")

    DEFAULT_SCHEDULE = os.getenv("DEFAULT_SCHEDULE_DATETIME")
