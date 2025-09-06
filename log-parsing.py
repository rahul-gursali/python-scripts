def parse_logs(file_path, keyword):
    with open(file_path) as f:
        return [line for line in f if keyword in line]

# Usage
errors = parse_logs("/var/log/syslog", "ERROR")
print(errors)
