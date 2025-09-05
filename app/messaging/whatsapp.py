from config import Config
from ..utils import log_message

def send_whatsapp_twilio(to: str, message: str):
    from twilio.rest import Client
    client = Client(Config.TWILIO_ACCOUNT_SID, Config.TWILIO_AUTH_TOKEN)
    whatsapp_to = f"whatsapp:{to}"
    whatsapp_from = Config.TWILIO_WHATSAPP_FROM
    msg = client.messages.create(body=message, from_=whatsapp_from, to=whatsapp_to)
    log_message(f"Twilio message sid: {msg.sid}", Config.LOG_PATH)
    return msg.sid

def send_whatsapp_ultramsg(to: str, message: str):
    import requests
    token = Config.ULTRAMSG_TOKEN
    instance = Config.ULTRAMSG_INSTANCE
    if not token or not instance:
        raise Exception("UltraMsg credentials not set")
    url = f"https://api.ultramsg.com/{instance}/messages/chat"
    data = {"token": token, "to": to, "body": message}
    r = requests.post(url, data=data, timeout=20)
    log_message(f"UltraMsg response: {r.text}", Config.LOG_PATH)
    r.raise_for_status()
    return r.json()

def send_whatsapp(to: str, message: str):
    if Config.TWILIO_ACCOUNT_SID and Config.TWILIO_AUTH_TOKEN and Config.TWILIO_WHATSAPP_FROM:
        return send_whatsapp_twilio(to, message)
    if Config.ULTRAMSG_TOKEN and Config.ULTRAMSG_INSTANCE:
        return send_whatsapp_ultramsg(to, message)
    raise Exception("No WhatsApp provider credentials found (TWILIO or ULTRAMSG)")
