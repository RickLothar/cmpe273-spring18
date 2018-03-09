import zmq

# ZeroMQ Context
context = zmq.Context()

sock = context.socket(zmq.SUB)

sock.connect("tcp://127.0.0.1:5556")
sock.setsockopt_string(zmq.SUBSCRIBE, '')

while True:
    msg = sock.recv()
    print(msg.decode())
