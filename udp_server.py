import socket
import threading

bind_ip="192.168.152.20"
bind_port=9999

server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind((bind_ip,bind_port))
print("[*] server listening on %s : %d" %(bind_ip,bind_port))

while True:
    data,addr=server.recvfrom(4096)
    print(data)
    server.sendto("aaaaaa",addr)
