import zmq
import sys

# ZeroMQ Context
context = zmq.Context()

# TODO: change this to PUB pattern.
# Define the socket using the "Context"
sock = context.socket(zmq.REQ)
sock.connect("tcp://127.0.0.1:5678")

# Send a "message" using the socket
user_name = " ".join(sys.argv[1:])
print("[client]:" + user_name)
sock.send_string(user_name)
msg = sock.recv()
print("[received]:" + msg.decode())

while True:
    sock.connect("tcp://127.0.0.1:5678")
    user_input=input("[%s]> " %user_name)
    sock.send_string(user_input)
    msg = sock.recv()
    print("[received]:" + msg.decode())