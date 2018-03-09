import zmq
import sys


# ZeroMQ Context
# context = zmq.Context()

# sock_pb = context.socket(zmq.PUB)

# port = sys.argv[1:]

# sock_pb.bind("tcp://127.0.0.1:%s" % port)

def main(port, who):

    ctx = zmq.Context()
    socket = ctx.socket(zmq.PUB)
    socket.bind("tcp://127.0.0.1:%s" %port)

    while True:
        msg = input("%s> " % who)
        socket.send_pyobj((who, msg))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Use: client.py <port> <username>")
        raise SystemExit
    main(sys.argv[1], sys.argv[2])
