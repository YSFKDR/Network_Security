# Network Security Tool

**Network Security Tool** is a home network security monitoring and reporting tool. It captures network traffic data, device inventory, and alerts, and generates user-friendly HTML reports that are sent via email weekly.

## Features

- **Traffic Data Monitoring:** Captures and summarizes network traffic data.
- **Device Discovery:** Periodically scans the network to discover connected devices.
- **Alert Logging:** Logs anomalies and potential security threats.
- **Weekly Reports:** Generates and emails HTML reports with traffic data, device inventory, and alerts.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/YSFKDR/Network_Security.git
    cd Network_Security
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv nsenv
    source nsenv/bin/activate
    ```

3. **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your email configuration in `generate_report.py`:**
    ```python
    from_addr = "your_email@outlook.com"  # Replace with your Outlook email address
    to_addr = "recipient@example.com"  # Replace with the recipient's email address
    app_password = "your_app_password"  # Replace with your generated app password
    ```

## Usage

1. **Run the main script to start the application:**
    ```bash
    python main.py
    ```

2. **Click "Generate Report" in the GUI to capture data and generate the report.**

## Directory Structure

```markdown
Network_Security/
├── data/
│   ├── traffic_data/          # Captured traffic data files
│   ├── device_inventory/      # Discovered device inventory files
│   ├── alerts_logs/           # Logged alert files
├── reports/                   # Generated reports
├── nsenv/                     # Virtual environment directory
├── traffic_data_capture.py    # Script to capture network traffic data
├── device_discovery.py        # Script to discover devices on the network
├── alert_logging.py           # Script to log alerts and anomalies
├── generate_report.py         # Script to generate and email reports
├── manage_data_size.py        # Script to manage data size and delete old files
├── main.py                    # Main script to run the application
├── icon.png                   # Application icon
└── README.md                  # Project documentation
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
