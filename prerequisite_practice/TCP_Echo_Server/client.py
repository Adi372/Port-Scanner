import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5000))
print("Connected to server")

# Why .encode()?
# TCP sends bytes, not Python strings.
# "Hello"           → string
# "Hello".encode()  → b"Hello"
# So the flow is now:
# Client                         Server
#    |                              |
#    | ------ connect() ----------> |
#    |                              |
#    | ------ "Hello" ------------> |
#    |                              |
#    |                         recv(1024)
client.send("Hello".encode())
