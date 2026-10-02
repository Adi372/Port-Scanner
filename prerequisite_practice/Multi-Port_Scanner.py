import socket

host = input("Host: ")
start_port = 1
end_port = 100

print()
print("===== PORT SCAN =====")

for port in range(start_port, end_port + 1):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Wait a maximum of 1 second for the connection attempt.
    # Without a timeout:
    # Port 1 → waiting...
    # Port 2 → waiting...
    # Port 3 → waiting...

    # A filtered/unresponsive port could make your scanner wait unnecessarily.
    # With:
    # sock.settimeout(1)
    # it moves on after approximately 1 second if there's no response.
    sock.settimeout(1)

    result = sock.connect_ex((host, port))

    if result == 0:
        print(port, "OPEN")
    else:
        print(port, "CLOSED")

    sock.close()