import socket

# Creates a TCP IPv4 socket:
# AF_INET → IPv4
# SOCK_STREAM → TCP
# TCP provides a connection-oriented communication process:
# Client                    Server
#   |                         |
#   | ---- connect() ------>  |
#   | <--- connection ------- |
#   |                         |
#   | ---- send() ----------> |
#   | <---- recv() ---------- |
#   |                         |
# Main difference
# TCP: Client → connect() → Server
# There is a clear connection attempt. If the server accepts it, we know something is listening.
# UDP: Client → send UDP packet → Server
# There is no connection handshake. UDP is connectionless.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Assigns the server to:
# IP   → 127.0.0.1
# Port → 5000 (5000 is just the port number we chose for our server)
# 127.0.0.1 means this same computer
server.bind(("127.0.0.1", 5000))

# Puts the socket into listening mode, waiting for clients.
# The 1 in: server.listen(1) means the backlog size.
# It tells the OS:
# “Allow up to 1 connection to wait in the queue while the server is busy handling another connection.”
server.listen(1)

print("Listening on 127.0.0.1:5000")

# This line waits for a client to connect and, when one connects, gives you two things:
# (client_socket, ('127.0.0.1', 54321))
# client is a new socket specifically for communicating with that client.
# And address contains the client's:
# IP address
# Port

client, address = server.accept()
print("Client connected: ", address)