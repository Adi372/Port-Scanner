import socket
from concurrent.futures import ThreadPoolExecutor, as_completed


def scan_host(host, port):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((host, port))

    sock.close()

    if result == 0:
        return host

    return None


hosts = [
    "192.168.31.1",
    "192.168.31.146",
    "192.168.31.172",
    "192.168.31.215",
    "192.168.31.217"
]

port = 80

futures = []

with ThreadPoolExecutor(max_workers=10) as executor:

    for host in hosts:
        future = executor.submit(scan_host, host, port)
        futures.append(future)

    for future in as_completed(futures):
        result = future.result()

        if result is not None:
            print(f"{result}:{port} OPEN")