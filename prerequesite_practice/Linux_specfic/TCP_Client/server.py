import socket

server = socket.socket()
server.bind(("192.168.31.217", 5000))
server.listen()

print("Waiting for connection...")

client, address = server.accept()

data = client.recv(1024)
message = data.decode()

print("Received:", message)

client.close()
server.close()

