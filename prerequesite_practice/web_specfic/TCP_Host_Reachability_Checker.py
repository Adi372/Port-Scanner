import socket

ip = input("Enter the IP address: ")
port = int(input("Enter the port: "))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(2)

try:
    result = sock.connect_ex((ip, port))

    if result == 0:
        print(f"{ip}:{port} is reachable and accepting TCP connections")
    else:
        print(f"{ip}:{port} is not accepting a TCP connection.")

except socket.timeout:
    print(f"{ip}:{port} timed out")

except ConnectionRefusedError:
    print(f"{ip}:{port} refused the connection.")

finally:
    sock.close()