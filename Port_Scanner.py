import socket
import ipaddress
import psutil
from scapy.all import ARP, Ether, srp
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

def get_local_network():

    interfaces = psutil.net_if_addrs()

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        sock.connect(("8.8.8.8", 80))
        local_ip = sock.getsockname()[0]
    finally:
        sock.close()

    for interface, addresses in interfaces.items():

        for address in addresses:

            if address.family == socket.AF_INET:
                
                if address.address == local_ip:

                    network = ipaddress.ip_network(
                        f"{local_ip}/{address.netmask}",
                        strict=False
                    )

                    return interface, local_ip, network

    raise RuntimeError("Could not determine active network")


interface, local_ip, network = get_local_network()

print()
print(f"Interface : {interface}")
print(f"Local IP  : {local_ip}")
print(f"Network   : {network}")

print()
print("===== ARP DEVICE DISCOVERY =====")


arp_request = ARP(
    pdst=str(network)
)

ethernet_frame = Ether(
    dst="ff:ff:ff:ff:ff:ff"
)

packet = ethernet_frame / arp_request


answered, unanswered = srp(
    packet,
    timeout=2,
    verbose=0
)


print()
print("IP Address       MAC Address           Hostname")
print("-----------------------------------------------------")


hosts = {
    local_ip: socket.gethostname()
}

local_mac = "Unknown"

for address in psutil.net_if_addrs()[interface]:

    if address.family == psutil.AF_LINK:
        local_mac = address.address
        break


# Print your own device
print(
    f"{local_ip:<16} "
    f"{local_mac:<20} "
    f"{socket.gethostname()}"
)

for sent, received in answered:

    if received.psrc == local_ip:
        continue

    try:
        hostname = socket.gethostbyaddr(
            received.psrc
        )[0]

    except socket.herror:
        hostname = "Unknown"

    hosts[received.psrc] = hostname

    print(
        f"{received.psrc:<16} "
        f"{received.hwsrc:<20} "
        f"{hostname}"
    )


def portScan(host, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(1.5)
    try:
        result = client.connect_ex((host, port))
        if result == 0:
            tqdm.write(f"{host}:{port} OPEN")
    finally:
        client.close()


def main():

    for ip, hostname in hosts.items():

        print()
        print(f"Hostname: {hostname}")
        print(f"IP      : {ip}")

        ports = range(1, 1001)

        with ThreadPoolExecutor(max_workers=40) as executor:

            results = executor.map(
                lambda port: portScan(ip, port),
                ports
            )

            for _ in tqdm(
                results,
                total=1000,
                desc=f"Scanning {ip}",
                unit="port"
            ):
                pass

main()