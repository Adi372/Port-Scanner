import socket
import ipaddress
from concurrent.futures import ThreadPoolExecutor


network_input = input("Enter network: ")

network = ipaddress.ip_network(
    network_input,
    strict=False
)


def check_host(ip):

    sock = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    sock.settimeout(1)

    try:
        result = sock.connect_ex(
            (str(ip), 80)
        )

        if result == 0:
            return ip, "Reachable"

        return ip, "No response"

    except socket.timeout:
        return ip, "Timeout"

    finally:
        sock.close()


print()
print("===== HOST DISCOVERY =====")


hosts = list(network.hosts())

with ThreadPoolExecutor(max_workers=20) as executor:

    results = executor.map(
        check_host,
        hosts
    )

    for ip, status in results:

        if status == "Reachable":
            print(f"{str(ip):<16} {status}")