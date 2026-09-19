import socket

ip = input("Target: ")
start = int(input("Start port: "))
end = int(input("End port: "))

for port in range(start, end + 1):

    s = socket.socket()

    result = s.connect_ex((ip, port))

    if result == 0:
        print(f"{port} → OPEN")
    else:
        print(f"{port} → CLOSED")

    s.close()