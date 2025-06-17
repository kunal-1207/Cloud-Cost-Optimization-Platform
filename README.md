# 💸 Autonomous Cloud Cost Optimization Platform

[![Python](https://img.shields.io/badge/language-Python-blue.svg)](https://www.python.org/)
[![AWS](https://img.shields.io/badge/cloud-AWS-orange)](https://aws.amazon.com/)
[![Terraform](https://img.shields.io/badge/infrastructure-Terraform-purple)](https://www.terraform.io/)
[![Slack Alerts](https://img.shields.io/badge/notifications-Slack-4A154B?logo=slack&logoColor=white)](https://slack.com/)
[![Email](https://img.shields.io/badge/alerts-Email-green)](#)

---

## 📘 Overview

**Autonomous Cloud Cost Optimization Platform** helps organizations eliminate cloud waste by identifying **idle or underutilized resources** across AWS, and triggering:

- 🔔 Slack/Email alerts
- 📉 Auto-scaling suggestions using ML
- 🔁 Automated remediation via Terraform
- 📊 Exporting metrics to Grafana-compatible dashboards

This combines **FinOps discipline** with **DevOps automation** to enable cost-efficient cloud usage.

---

## 🔍 Key Features

- 🧠 **ML-Powered Autoscaling Recommendations**
- ☁️ **Idle Resource Scanner** (e.g., EC2, EBS, IPs)
- 🔔 **Slack + Email Alerting**
- 🛠️ **Remediation-as-Code with Terraform**
- 📊 **Dashboard Export (Grafana-compatible JSON)**
- 🔐 **Secure `.env`-based configuration**

---

## 📁 Directory Structure

```bash
.
├── main.py                     # Entry point
├── .env                        # Environment variables
├── requirements.txt            # Python dependencies
├── alerts/
│   ├── slack_alert.py          # Slack notification handler
│   └── email_alert.py          # Email notification handler
├── scanners/
│   └── aws.py                  # AWS idle resource scanner
├── remediation/
│   └── terraform.py            # Terraform remediation engine
├── ml/
│   └── autoscaler.py           # ML logic for cost optimization
├── dashboard/
│   └── grafana_exporter.py     # Exports metrics to JSON for Grafana
````

---

## ⚙️ Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/your-org/cloud-cost-optimizer.git
cd cloud-cost-optimizer
```

2. **Create & Activate a Virtual Environment**

```bash
python -m venv .venv
source .venv/bin/activate   # on Linux/macOS
# OR
.venv\Scripts\activate      # on Windows
```

3. **Install Requirements**

```bash
pip install -r requirements.txt
```

4. **Configure Environment Variables**

Create a `.env` file:

```env
SLACK_WEBHOOK=https://hooks.slack.com/services/...
EMAIL_FROM=your_email@gmail.com
EMAIL_PASSWORD=your_gmail_app_password
EMAIL_TO=recipient@example.com
GRAFANA_METRICS_PATH=metrics/metrics.json
```

---

## 🚀 How It Works (Execution Flow)

### 🔍 1. Scan Idle AWS Resources

```python
report = aws.scan_idle_resources()
```

Example output:

```json
[
  {"id": "i-123456", "type": "EC2", "state": "stopped"},
  {"id": "vol-7890", "type": "EBS", "state": "unattached"}
]
```

---

### 📤 2. Send Alerts

**Slack Alert**

```python
slack_alert.send(report)
```

**Email Alert**

```python
email_alert.send(report)
```

---

### 🧠 3. ML-Based Recommendations

```python
recommendations = autoscaler.generate_recommendations(report)
```

Example:

```json
[
  {"id": "i-123456", "action": "shutdown at 8PM daily"},
  {"id": "vol-7890", "action": "schedule deletion"}
]
```

---

### 🛠️ 4. Terraform Remediation

```python
terraform.remediate(recommendations)
```

Generates Terraform `.tf` or triggers auto-remediation scripts.

---

### 📊 5. Export Metrics for Grafana

```python
grafana_exporter.export(report)
```

Saves output to:

```
metrics/metrics.json
```

---

## 🧪 Testing & Validation

Run the project locally:

```bash
python main.py
```

Expected console output:

```bash
🔍 Scanning AWS for idle resources...
✅ Scan complete. Found 2 idle resources.
📤 Sending Slack alert...
✅ Slack alert sent.
📧 Sending Email alert...
✅ Email alert sent.
🧠 Generating ML-based recommendations...
✅ Recommendations: [...]
🛠️ Triggering Terraform remediation...
✅ Remediation complete.
📊 Exporting metrics for Grafana...
✅ All tasks completed successfully.
```

---

## 📁 Sample `.env` File

```env
SLACK_WEBHOOK=https://hooks.slack.com/services/T000/B000/XXX
EMAIL_FROM=your_email@gmail.com
EMAIL_PASSWORD=your_gmail_app_password
EMAIL_TO=recipient@example.com
GRAFANA_METRICS_PATH=metrics/metrics.json
```

---

## 🔐 Security Notes

* ✅ **Never commit `.env` or secrets** to version control.
* 🔒 Use **App Passwords** for email integrations.
* 🔐 Store secrets securely using tools like AWS Secrets Manager or HashiCorp Vault in production.

---

## 🤝 Contribution

We welcome contributions! Feel free to:

* Submit pull requests
* File issues for bugs or features
* Improve ML recommendations or multi-cloud support

---

## 📜 License

This project is licensed under the **MIT License**.

---
