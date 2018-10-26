import socket

def receive(ip="0.0.0.0", port=5005):
    UDP_IP = ip
    UDP_PORT = port

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))

    # TODO: Remove this later
    counter = 5
    while counter >= 0:
        data, addr = sock.recvfrom(1024)
        print "received message:", data
        counter -= 1

