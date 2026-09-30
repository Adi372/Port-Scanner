import socket

# socket as an interface Python can use to communicate over a network
# Create an IPv4 UDP socket
# UDP lets us discover the local IP without actually connecting to the internet
# With TCP, connect() normally involves establishing a TCP connection with the remote host.
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# print(sock)

# 8.8.8.8 → destination IP
# 80      → destination port
# 8.8.8.8 is a public DNS server operated by Google.
# Port 80 is the standard port associated with HTTP
sock.connect(("8.8.8.8", 80))

# getsockname() returns the socket's local address.
# local_address = sock.getsockname()

# ('local IP', local port)
# print(local_address)

local_ip = sock.getsockname()[0]
print("Local IP:", local_ip)