import socket

target_host="www.google.com"
target_port=80

client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # create a socket object

client.sendto("AKASH AWASTHI",(target_host,target_port))

data,add=client.recvfrom(4096) # return both the data and the details of the remote host and port

print(data)
