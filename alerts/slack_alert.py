import os
import requests

def format_report(report):
    return '\n'.join([f"{r['type']} - {r['id']}" for r in report])

def send(report):
    webhook = os.environ.get('SLACK_WEBHOOK')
    if not webhook:
        print("⚠️ SLACK_WEBHOOK is not set. Skipping Slack alert.")
        return
    msg = f"🚨 Idle Resources Detected:\n{format_report(report)}"
    response = requests.post(webhook, json={"text": msg})
    if response.status_code == 200:
        print("✅ Slack alert sent.")
    else:
        print(f"❌ Slack alert failed. Status code: {response.status_code}")
