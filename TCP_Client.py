import socket

target_host = "www.reddit.com"
target_port = 80

#Create a socket object

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect the client

client.connect((target_host, target_port))

#Send some data!

client.send(("GET / HTTP/1.1/r\nHost: http://reddit.com\r\n\r\n"))

#Receive some data!

data = client.recv(4096)

print data
