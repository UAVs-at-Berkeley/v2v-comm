import socket

UDP_IP = "192.168.1.6"
UDP_PORT = 5005
MESSAGE = "HELLO WORLD"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

