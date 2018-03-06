import zmq

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock_rp = context.socket(zmq.REP)
sock_pb = context.socket(zmq.PUB)
sock_rp.bind("tcp://127.0.0.1:5678")
sock_pb.bind("tcp://127.0.0.1:5556")

# Run a simple "Echo" server
while True:
    message = sock_rp.recv()
    message = message.decode()
    
    sock_rp.send_string(message)
    sock_pb.send_string(message)

    print("[Server-End]" + message)
