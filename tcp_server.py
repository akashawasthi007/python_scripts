import socket
import threading

bind_ip="192.168.5.20"
bind_port= 9999

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((bind_ip,bind_port))
server.listen(5)

print("[*] serer listening on %s : %d"%(bind_ip,bind_port))

# this is our client-handling thread
def handle_Client(client_socket):
    # print out whar the client send
    request=client_socket.recv(1024) #1024 represent size of data
    print("[*] received: %s"%request)

    # sends a packet
    client_socket.send(b"Ack")
    #print(client_socket.getpeername())
    client_socket.close()

while True:
    client,add=server.accept()
    print("[*] accepted connection from %s : %d"%(add[0],add[1]))

    #spin our client thread to handle incoming data
    client_handler=threading.Thread(target=handle_Client,args=(client,))
    client_handler.start()
