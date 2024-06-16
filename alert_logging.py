# alert_logging.py
import os
import json
from datetime import datetime

def log_alert(alert):
    filename = f"~/network_security/data/alerts_logs/{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"
    with open(os.path.expanduser(filename), 'a') as file:
        json.dump(alert, file)
        file.write('\n')

alert = {
    "timestamp": datetime.now().isoformat(),
    "message": "Unusual activity detected",
    "severity": "High"
}
log_alert(alert)
