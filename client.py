
import socket
HOST = "192.168.0.150"
#HOST = socket.gethostname()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, 1234))
s.sendall(b'bsdfgfdshy')
msg = s.recv(1024)
print(msg.decode("utf-8"))
while True:
    data = bytes(input(),"utf-8")
    s.sendall(data)