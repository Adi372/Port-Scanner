import socket

ip = input("Enter IP address: ")
port = int(input("Enter port: "))

s = socket.socket()

result = s.connect_ex((ip, port))

if result == 0:
    print(f"Port {port}: OPEN")
else:
    print(f"Port {port}: CLOSED")

s.close()