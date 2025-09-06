def restart_service(service_name):
    import subprocess
    subprocess.run(["systemctl", "restart", service_name])
    print(f"{service_name} restarted successfully")

# Usage
restart_service("nginx")
restart_service("docker")
