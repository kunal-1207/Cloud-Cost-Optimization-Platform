from scanners import aws
from alerts import email_alert, slack_alert
from remediation import terraform
from ml import autoscaler
from dashboard import grafana_exporter
from dotenv import load_dotenv

load_dotenv()

def format_report(report):
    return '\n'.join([f"{r['type']} - {r['id']}" for r in report])

def main():
    print("🔍 Scanning AWS for idle resources...")
    report = aws.scan_idle_resources()
    print(f"✅ Scan complete. Found {len(report)} idle resources.")

    if not report:
        print("🎉 No idle resources found!")
        return

    print("📤 Sending Slack alert...")
    slack_alert.send(report)

    print("📧 Sending Email alert...")
    email_alert.send(report)

    print("🧠 Generating ML-based recommendations...")
    recommendations = autoscaler.generate_recommendations(report)
    print(f"✅ Recommendations: {recommendations}")

    print("🛠️ Triggering Terraform remediation...")
    terraform.remediate(recommendations)

    print("📊 Exporting metrics for Grafana...")
    grafana_exporter.export(report)

    print("✅ All tasks completed successfully.")

if __name__ == '__main__':
    main()
