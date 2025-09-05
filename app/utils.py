import os
from datetime import datetime

def ensure_logs_dir(log_path):
    d = os.path.dirname(log_path)
    if d and not os.path.exists(d):
        os.makedirs(d, exist_ok=True)
    if not os.path.exists(log_path):
        open(log_path, 'a', encoding='utf-8').close()

def log_message(text, log_path="./logs/messages.log"):
    try:
        with open(log_path, 'a', encoding='utf-8') as f:
            f.write(f"{datetime.utcnow().isoformat()}Z - {text}\n")
    except Exception:
        pass
