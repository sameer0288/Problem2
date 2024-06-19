import psutil
import logging
from datetime import datetime

# Configuration for thresholds
CPU_THRESHOLD = 80  # in percentage
MEMORY_THRESHOLD = 80  # in percentage
DISK_THRESHOLD = 80  # in percentage

# Setup logging
logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s %(message)s')

def log_alert(message):
    print(message)
    logging.info(message)

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        log_alert(f"High CPU usage detected: {cpu_usage}%")

def check_memory_usage():
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        log_alert(f"High memory usage detected: {memory_usage}%")

def check_disk_usage():
    disk_usage = psutil.disk_usage('/')
    if disk_usage.percent > DISK_THRESHOLD:
        log_alert(f"High disk usage detected: {disk_usage.percent}%")

def check_running_processes():
    processes = [proc.info for proc in psutil.process_iter(['pid', 'name', 'username'])]
    log_alert(f"Currently running processes: {processes}")

def monitor_system():
    log_alert("Starting system health monitoring.")
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_running_processes()
    log_alert("Completed system health check.")

if __name__ == "__main__":
    monitor_system()
