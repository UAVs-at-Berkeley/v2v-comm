import socket
from consts import *

def receive(ip="0.0.0.0", port=5005):
    UDP_IP = ip_receive
    UDP_PORT = port_receive

    # TODO: Remove this later
    counter = 5
    while counter >= 0:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((UDP_IP, UDP_PORT))
        sock.settimeout(1)
        try:
            data, addr = sock.recvfrom(1024)
            print "received message:", data
        except:
            print "no message received"
        finally:
            counter -= 1

