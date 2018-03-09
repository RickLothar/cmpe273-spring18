import zmq
import sys

# ZeroMQ Context
context = zmq.Context()

# TODO: change this to PUB pattern.
# Define the socket using the "Context"
sock_rq = context.socket(zmq.REQ)
sock_rq.connect("tcp://127.0.0.1:5678")
sock_sb = context.socket(zmq.SUB)
sock_sb.connect("tcp://127.0.0.1:5556")

# Send a "message" using the socket
user_name = " ".join(sys.argv[1:])
print("[client]:" + user_name)
sock_rq.send_string(user_name)
msg = sock_rq.recv().decode()
print("User[%s] Connected to the chat server" %msg)

def check_usr(msg_sb):
    reply_title='['+user_name+']'
    char_count = len(reply_title)
    if msg_sb[:char_count]==reply_title:
        return False
    else:
        return True

sock_sb.setsockopt_string(zmq.SUBSCRIBE, '')

while True:
    sock_rq.connect("tcp://127.0.0.1:5678")

    user_input=input("[%s]> " %user_name)
    sock_rq.send_string("[%s]: %s" %(user_name, user_input))
    msg = sock_rq.recv()

    msg_sb=sock_sb.recv().decode()
    if check_usr(msg_sb):
        print(msg_sb)

    