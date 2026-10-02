import socket

host = input("Enter Host: ")

start_port = 1
end_port = 100

for port in range(start_port, end_port + 1):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((host, port))

    if result == 0:
        try:
            # This is a Python socket function that looks up a service name based on a port number.
            # What standard TCP service is associated with this port number?
            service = socket.getservbyport(port, "tcp")
            print(port, "OPEN", service.upper())
        except OSError:
            print(port, "OPEN", "UNKNOWN")

    sock.close()