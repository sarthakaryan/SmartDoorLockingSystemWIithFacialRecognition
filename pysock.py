import socket

HOST = '192.168.161.105'  # IP address of the ESP32
PORT = 5000              # Port number of the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    message = "Hello, ESP32!\n"
    s.sendall(message.encode())
