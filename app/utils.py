import os
from datetime import datetime
from config import Config

def ensure_logs_dir():
    d = os.path.dirname(Config.LOG_PATH)
    if d and not os.path.exists(d):
        os.makedirs(d, exist_ok=True)
    if not os.path.exists(Config.LOG_PATH):
        open(Config.LOG_PATH, 'a', encoding='utf-8').close()

def log_message(text):
    try:
        with open(Config.LOG_PATH, 'a', encoding='utf-8') as f:
            f.write(f"{datetime.utcnow().isoformat()}Z - {text}\n")
    except Exception:
        pass
