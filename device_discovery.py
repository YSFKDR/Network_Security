# device_discovery.py
import os
import json
import subprocess
from datetime import datetime

def discover_devices():
    command = "sudo nmap -sn 111.111.1.0/00"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    devices = parse_nmap_output(result.stdout)
    return devices

def parse_nmap_output(output):
    devices = []
    lines = output.split('\n')
    for line in lines:
        if "Nmap scan report for" in line:
            ip = line.split()[-1]
            devices.append({"ip": ip})
        elif "MAC Address:" in line:
            mac = line.split()[2]
            devices[-1]["mac"] = mac
            devices[-1]["vendor"] = ' '.join(line.split()[3:])
    return devices

def save_device_inventory(devices):
    filename = f"~/network_security/data/device_inventory/{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"
    with open(os.path.expanduser(filename), 'w') as file:
        json.dump(devices, file)

devices = discover_devices()
save_device_inventory(devices)
