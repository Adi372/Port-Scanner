import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 5000))

server.listen(1)

print("Server listening on port 5000...")

conn, address = server.accept()

print(f"Connected by {address}")

data = conn.recv(1024)

print(f"Received: {data.decode()}")

conn.send(data)

conn.close()
server.close()