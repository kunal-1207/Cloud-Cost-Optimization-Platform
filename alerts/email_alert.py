import smtplib
from email.mime.text import MIMEText
import os

def format_report(report):
    return '\n'.join([f"{r['type']} - {r['id']}" for r in report])

def send(report):
    email_from = os.environ.get('EMAIL_FROM')
    email_to = os.environ.get('EMAIL_TO')
    email_password = os.environ.get('EMAIL_PASSWORD')

    if not all([email_from, email_to, email_password]):
        print("⚠️ Missing email environment variables. Skipping email alert.")
        return

    msg = MIMEText(format_report(report))
    msg['Subject'] = '🚨 Cloud Idle Resources Report'
    msg['From'] = email_from
    msg['To'] = email_to

    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(email_from, email_password)
        s.sendmail(email_from, [email_to], msg.as_string())
        s.quit()
        print("✅ Email alert sent.")
    except Exception as e:
        print(f"❌ Failed to send email alert: {e}")
