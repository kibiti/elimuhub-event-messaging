from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.date import DateTrigger
from datetime import datetime
from .messaging.emailer import send_email
from .messaging.whatsapp import send_whatsapp
from .utils import log_message
from config import Config
import pandas as pd

scheduler = BackgroundScheduler()

def _schedule_job(send_time, func, *args, **kwargs):
    if isinstance(send_time, str):
        send_time = pd.to_datetime(send_time)
    if pd.isna(send_time):
        send_time = pd.to_datetime(Config.DEFAULT_SCHEDULE)
    if isinstance(send_time, pd.Timestamp):
        send_time = send_time.to_pydatetime()
    trigger = DateTrigger(run_date=send_time)
    job = scheduler.add_job(func, trigger=trigger, args=args, kwargs=kwargs)
    return job

def schedule_messages_from_df(df: pd.DataFrame, default_schedule=None):
    for idx, row in df.iterrows():
        name = row.get('name') or row.get('NAME') or "RECIPIENT"
        email = row.get('email') or ""
        whatsapp_num = row.get('whatsapp_number') or row.get('phone') or ""
        send_email_flag = str(row.get('send_email', 'yes')).strip().lower() in ('yes','y','true','1')
        send_whatsapp_flag = str(row.get('send_whatsapp', 'yes')).strip().lower() in ('yes','y','true','1')
        preferred_time = row.get('preferred_time') or default_schedule or Config.DEFAULT_SCHEDULE
        message = row.get('message') or "Assalamu Alaikum. You are invited."

        if send_email_flag and email:
            _schedule_job(preferred_time, _send_email_job, name, email, message)
        if send_whatsapp_flag and whatsapp_num:
            _schedule_job(preferred_time, _send_whatsapp_job, name, whatsapp_num, message)

def _send_email_job(name, email, message):
    subject = "Invitation: Kenya Islamic Universities & Colleges Education Fair"
    try:
        send_email(to=email, subject=subject, body=message, recipient_name=name)
        log_message(f"EMAIL sent to {email} | name={name}")
    except Exception as e:
        log_message(f"EMAIL FAILED to {email} | error={e}")

def _send_whatsapp_job(name, whatsapp_number, message):
    try:
        send_whatsapp(to=whatsapp_number, message=message)
        log_message(f"WHATSAPP sent to {whatsapp_number} | name={name}")
    except Exception as e:
        log_message(f"WHATSAPP FAILED to {whatsapp_number} | error={e}")
