import zmq
import sys
import time

context = zmq.Context()

# settings for SUB
subscriber = context.socket(zmq.SUB)
subscriber.connect("tcp://127.0.0.1:5556")
subscriber.setsockopt_string(zmq.SUBSCRIBE, '')

# settings for REQ
sender = context.socket(zmq.REQ)
sender.connect("tcp://127.0.0.1:5678")
user_name = sys.argv[1]
sender.send_string('[%s] joined the chat' % user_name)
msg = sender.recv().decode()

# settings for poll set
poller = zmq.Poller()
poller.register(subscriber, zmq.POLLIN)
poller.register(sender, zmq.POLLIN)

while True:
    while True:
        try:
            sender.connect("tcp://127.0.0.1:5678")
            usr_input = input('[%s]> ' % user_name)
            sender.send_string("[%s]: %s" % (user_name, usr_input))
            msg = sender.recv()
        except zmq.Again:
            break
    
    while True:
        try:
            msg = subscriber.recv().decode()
            print(msg)
        except zmq.Again:
            break

    time.sleep(0.01)

