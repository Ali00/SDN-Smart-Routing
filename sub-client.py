#This based on the Code of Example-22 by Greg M. Bernstein
#from https://www.grotto-networking.com/SDNfun.html
"""
    A subscriber for events from my OutLineAppZMQ POX application.
    IMPORTANT note for Windows users: Ctrl-C doesn't seem to shut this down on
    windows but Ctrl-Break does.
"""
import zmq

PUB_URL = "tcp://localhost:5555"  # You may need to adjust the address
context = zmq.Context()
socket = context.socket(zmq.SUB)  # The "request" side of the 0MQ "socket"
socket.connect(PUB_URL)
socket.setsockopt(zmq.SUBSCRIBE, "")
print "Starting Subscriber for Messages:"
while True:
    try:
        message = socket.recv_string()
        print "Received message: {}".format(message)
    except KeyboardInterrupt:
        print("W: interrupt received, proceeding")
        break
