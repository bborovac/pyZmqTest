import zmq

# print(zmq.zmq_version())

context = zmq.Context()

socket = context.socket(zmq.REP)


