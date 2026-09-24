import socket

client = socket.socket()

client.connect(("192.168.31.217", 5000))

message = "Hello Server"

client.send(message.encode())

client.close()