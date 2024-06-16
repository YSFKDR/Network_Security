import os
import tkinter as tk
from tkinter import messagebox

def run_script(script_name):
    script_path = os.path.expanduser(f"~/Network_Security/{script_name}.py")
    os.system(f"~/Network_Security/nsenv/bin/python {script_path}")

def generate_full_report():
    try:
        capture_traffic_data()
        discover_devices()
        log_alert()
        manage_data_size()
        generate_report()
        messagebox.showinfo("Info", "Full report generated and emailed successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def capture_traffic_data():
    run_script('traffic_data_capture')

def discover_devices():
    run_script('device_discovery')

def log_alert():
    run_script('alert_logging')

def generate_report():
    run_script('generate_report')

def manage_data_size():
    run_script('manage_data_size')

# Create directories if they don't exist
directories = [
    "~/Network_Security/data/traffic_data",
    "~/Network_Security/data/device_inventory",
    "~/Network_Security/data/alerts_logs",
    "~/Network_Security/reports"
]

for directory in directories:
    os.makedirs(os.path.expanduser(directory), exist_ok=True)

# Create the main window
root = tk.Tk()
root.title("Network Security Tool")

frame = tk.Frame(root)
frame.pack(pady=20, padx=20)

btn_generate_report = tk.Button(frame, text="Generate Report", command=generate_full_report)
btn_generate_report.grid(row=0, column=0, pady=20)

root.mainloop()
