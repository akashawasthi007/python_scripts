import socket

target_host="192.168.5.20" #ip address or target host
target_port=9999 # target port

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM) # create a socket object

# AF_INET parameter is saying we are going to use a standard IPv4 address.
# SOCK_STREAM indicates that this will be a TCP client.

client.connect((target_host,target_port)) #cconnect the client

client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n") # send the data

response=client.recv(4096) # receive some data

print(response)
