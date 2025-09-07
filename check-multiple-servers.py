services = ["nginx", "docker", "postgres"]

for service in services:
    print(f"Checking status of {service}...")
    os.system(f"systemctl status {service}")
