import socket
from tqdm import tqdm

host = input("Enter Host: ")

start_port=1
end_port=100

for port in tqdm(
    (range(start_port, end_port+1)),
    desc=f"Scanning: {host}",
    unit="port"
):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((host, port))

    if result == 0:
        try:
            service = socket.getservbyport(port, "tcp")
            tqdm.write(f"{port} OPEN {service.upper()}")
        except OSError:
            tqdm.write(f"{port} OPEN UNKNOWN")

    sock.close()