import socket

host = "localhost"
port = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    result = s.connect_ex((host, port))
    if result == 0:
        print(f"Port {port} is open")
    else:
        print(f"Port {port} is closed")
