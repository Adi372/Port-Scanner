import socket

print("===== TCP CONNECTION TESTER =====")
host = input("Host: ")
port = int(input("Port: "))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect_ex() is essentially connect() designed to give you the result as a value, which makes it very convenient for port scanning.
# client.connect(("127.0.0.1", 5000))\
# It tries to establish the connection.
# If successful: connection established
# If it fails, connect() normally raises an exception.
# Example:
# client.connect(("127.0.0.1", 9999))
# If nothing is listening on port 9999, you may get: ConnectionRefusedError

# result = sock.connect_ex((host, port))
# It also tries to establish a TCP connection, but instead of raising an exception for normal connection errors, it returns an error code.
# For example:
# result = sock.connect_ex(("127.0.0.1", 5000))
# If successful:
# result == 0
# If it fails:
# result != 0

result = sock.connect_ex((host, port))

if result == 0:
    print("Connection successfull")
else:
    print("Connection failed")

# If you create a socket, close it when you're done with it.
# Why close it?
# If you don't close sockets, your program can leave network resources open.
# For a single test, you might not notice. But your port scanner could test hundreds or thousands of ports, so leaving every socket open would be a problem.
sock.close()