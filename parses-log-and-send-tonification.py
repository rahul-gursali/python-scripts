import re

def monitor_logs(logfile):
    with open(logfile, 'r') as file:
        for line in file:
            if re.search("ERROR|FATAL", line):
                print(f"Alert! Issue found: {line.strip()}")

monitor_logs("/var/log/syslog")
