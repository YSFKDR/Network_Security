# traffic_data_capture.py
import os
import json
from datetime import datetime
import subprocess

def capture_traffic_data():
    command = "sudo tcpdump -i eth0 -c 100 -w -"
    result = subprocess.run(command, shell=True, capture_output=True)
    traffic_data = {
        "timestamp": datetime.now().isoformat(),
        "total_bytes": 1024,
        "device_data": [
            {"ip": "111.111.1.1", "bytes": 512},
            {"ip": "111.111.1.1", "bytes": 512}
        ]
    }
    return traffic_data

def save_traffic_data(data):
    filename = f"~/network_security/data/traffic_data/{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"
    with open(os.path.expanduser(filename), 'w') as file:
        json.dump(data, file)

data = capture_traffic_data()
save_traffic_data(data)
