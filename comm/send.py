import socket
from consts import *

def send(ip="192.168.1.6", port=5005):
    UDP_IP = ip_send
    UDP_PORT = port_send
    MESSAGE = message

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # TODO: Remove this later:
    counter = 5
    while counter >= 0:
        print(counter)
        sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
        counter -= 1

