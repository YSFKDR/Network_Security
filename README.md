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

Network_Security/
├── data/
│ ├── traffic_data/
│ ├── device_inventory/
│ ├── alerts_logs/
├── reports/
├── nsenv/
├── traffic_data_capture.py
├── device_discovery.py
├── alert_logging.py
├── generate_report.py
├── manage_data_size.py
├── main.py
└── README.md

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
