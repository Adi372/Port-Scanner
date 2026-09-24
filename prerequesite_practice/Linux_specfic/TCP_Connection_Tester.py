import socket
import errno

host = input("Host: ")
port = int(input("Port: "))

try:
    ip = socket.gethostbyname(host)

    s=socket.socket()
    s.settimeout(3)

    result = s.connect_ex((ip, port))

    if result == 0:
        print("OPEN")

    elif result == errno.ECONNREFUSED:
        print("CLOSED")

    else:
        print("CLOSED")

    s.close()

except socket.timeout:
    print("TIMEOUT")

except socket.gaierror:
    print("INVALID HOST")