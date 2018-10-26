import socket
import threading
from comm.receive import receive
from comm.send import send

# This class will be used to have send and receive run in parallel
# on both RPi's. 
# We will create 2 commThreads for each RPi. One for receiving and one for sending coordinates
# These do not need to be synchronized as the pi's do not share state
class commThread(threading.Thread):
    def __init__(self, threadID, name, func):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.func = func
    def run(self):
        print "Starting " + self.name
        self.func()

thread1 = commThread(1, "RPi-1-Send", send)
thread2 = commThread(2, "RPi-1-Receive", receive)
thread1.start()
thread2.start()

