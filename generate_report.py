import os
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

def generate_report():
    report = {"traffic_data": [], "device_inventory": [], "alerts_logs": []}

    traffic_data_dir = os.path.expanduser("~/network_security/data/traffic_data/")
    for filename in os.listdir(traffic_data_dir):
        with open(os.path.join(traffic_data_dir, filename), 'r') as file:
            report["traffic_data"].append(json.load(file))

    device_inventory_dir = os.path.expanduser("~/network_security/data/device_inventory/")
    for filename in os.listdir(device_inventory_dir):
        with open(os.path.join(device_inventory_dir, filename), 'r') as file:
            report["device_inventory"].append(json.load(file))

    alerts_logs_dir = os.path.expanduser("~/network_security/data/alerts_logs/")
    for filename in os.listdir(alerts_logs_dir):
        with open(os.path.join(alerts_logs_dir, filename), 'r') as file:
            for line in file:
                report["alerts_logs"].append(json.loads(line))

    report_filename = os.path.expanduser(f"~/network_security/reports/report_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json")
    with open(report_filename, 'w') as file:
        json.dump(report, file)
    
    print(f"Report saved to {report_filename}")
    return report_filename

def send_email(report_file):
    from_addr = "your_email@gmail.com"  # Replace with your email address
    to_addr = "recipient@example.com"  # Replace with the recipient's email address
    app_password = "your_password"  # Replace with your password

    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = "Weekly Network Security Report"

    body = "Please find the attached weekly network security report."
    msg.attach(MIMEText(body, 'plain'))

    with open(report_file, 'r') as file:
        attachment = MIMEText(file.read())
        attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(report_file))
        msg.attach(attachment)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_addr, app_password)
        text = msg.as_string()
        server.sendmail(from_addr, to_addr, text)
        server.quit()
        print("Email sent successfully.")
    except smtplib.SMTPAuthenticationError as e:
        print(f"SMTP Authentication Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    report_file = generate_report()
    if os.path.exists(report_file):
        send_email(report_file)
    else:
        print(f"Report file not found: {report_file}")
