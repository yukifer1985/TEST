import socket,sys
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.1.115",23))
print(s.getsockname())
print(s.getpeername())
buf=s.recv(2048)
print(buf)
