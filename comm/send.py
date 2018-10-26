import socket

def send(ip="192.168.1.6", port=5005):
    UDP_IP = ip
    UDP_PORT = port
    MESSAGE = "HELLO WORLD"

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # TODO: Remove this later:
    counter = 5
    while counter >= 5:
        print(counter)
        sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
        counter -= 1

