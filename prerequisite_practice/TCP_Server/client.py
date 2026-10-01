import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5000))
print("Connected to server")

# When your client runs:
# client.connect(("127.0.0.1", 5000))

# you specify only the server's port:
# Server → 5000

# The operating system automatically chooses an available temporary port for the client:
# Client → 38156

# So the connection looks like:
# Client                         Server
# 127.0.0.1:38156  ───────────→  127.0.0.1:5000
#                  TCP connection