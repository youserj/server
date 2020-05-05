import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#HOST = socket.gethostname()
HOST = "192.168.0.1"
print(HOST)
s.bind((HOST, 1234))
s.listen(5)

while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")
    clientsocket.send(bytes("Hey there!!!", "utf-8"))
    while True:
        data = clientsocket.recv(1024)
        if data != 0:
            print(repr(data))
        time.sleep(1)
