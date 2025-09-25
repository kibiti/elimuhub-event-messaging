import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import Config
from ..utils import log_message

def send_email(to: str, subject: str, body: str, recipient_name: str = ""):
    msg = MIMEMultipart('alternative')
    msg['From'] = Config.FROM_EMAIL
    msg['To'] = to
    msg['Subject'] = subject

    text_part = f"Assalamu Alaikum {recipient_name},\n\n{body}\n\nRegards,\nELIMUHUB"
    html_part = f"""
    <html>
      <body>
        <p>Assalamu Alaikum {recipient_name},</p>
        <p>{body}</p>
        <p>Regards,<br/>Elimuhub Education Consultants</p>
      </body>
    </html>
    """

    msg.attach(MIMEText(text_part, 'plain'))
    msg.attach(MIMEText(html_part, 'html'))

    server = smtplib.SMTP(Config.SMTP_HOST, Config.SMTP_PORT)
    server.starttls()
    server.login(Config.SMTP_USER, Config.SMTP_PASS)
    server.sendmail(Config.FROM_EMAIL, to, msg.as_string())
    server.quit()

    log_message(f"Email queued to {to}")
