import psutil
import time
from prometheus_client import start_http_server, Gauge

CPU_USAGE = Gauge('netpulse_cpu_usage_percent', 'CPU usage percent over time')
RAM_USAGE = Gauge('netpulse_ram_usage_percent', 'RAM usage percent over time')


def monitor_system():
    start_http_server(8000)
    print("NetPulse Exporter started on http://localhost:8000")
    print("Sending metrics to Prometheus... Press Ctrl+C to stop.")
    print("-" * 50)

    try:
        while True:

            cpu = psutil.cpu_percent(interval=1)
            ram = psutil.virtual_memory().percent

            CPU_USAGE.set(cpu)
            RAM_USAGE.set(ram)

            print(f"Metrict updated -> CPU: {cpu}% | RAM: {ram}%")

            time.sleep(4)

    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")


if __name__ == "__main__":
    monitor_system()