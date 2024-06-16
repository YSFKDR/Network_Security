# manage_data_size.py
import os

def get_directory_size(directory):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def delete_oldest_file(directory):
    files = [os.path.join(directory, f) for f in os.listdir(directory)]
    oldest_file = min(files, key=os.path.getctime)
    os.remove(oldest_file)

data_directories = [
    "~/network_security/data/traffic_data/",
    "~/network_security/data/device_inventory/",
    "~/network_security/data/alerts_logs/"
]

while get_directory_size("~/network_security/data/") > 10 * 1024 * 1024 * 1024:
    for data_dir in data_directories:
        delete_oldest_file(os.path.expanduser(data_dir))
