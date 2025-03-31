import socket

def is_server_up(host, port):
    try:
        socket.create_connection((host, port), timeout=5)
        return True
    except socket.error:
        return False

print(is_server_up("google.com", 80))
