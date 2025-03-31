import paramiko

def run_command(host, user, key_path, command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, username=user, key_filename=key_path)
    stdin, stdout, stderr = ssh.exec_command(command)
    print(stdout.read().decode())

run_command("server-ip", "ubuntu", "/path/to/private-key.pem", "sudo apt update")
