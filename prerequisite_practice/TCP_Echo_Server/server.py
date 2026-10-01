import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 5000))
server.listen(1)

print("Listening on 127.0.0.1:5000")

client, address = server.accept()

print("Client connected: ", address)

# client.recv(1024) means:
# Receive up to 1024 bytes of data from the client

# the result is bytes, for example: b'Hello'

# That's why we use:
# data.decode() to convert the bytes into a normal Python string:
# Hello

data = client.recv(1024)

print("Received: ", data.decode())