import socket
import psutil
import ipaddress
from scapy.all import ARP, Ether, srp

# Get own IP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(("8.8.8.8", 80))

own_ip = sock.getsockname()[0]

sock.close()

# Get own MAC and network
own_mac = None
network = None

interfaces = psutil.net_if_addrs()

for interface, addresses in interfaces.items():

    for address in addresses:

        if address.family == socket.AF_INET:

            if address.address == own_ip:

                netmask = address.netmask

                network = ipaddress.ip_network(
                    f"{own_ip}/{netmask}",
                    strict=False
                )

                for addr in addresses:

                    if addr.family == psutil.AF_LINK:
                        own_mac = addr.address
                        break

                break


# ARP discovery
arp_request = ARP(pdst=str(network))

ether = Ether(dst="ff:ff:ff:ff:ff:ff")

packet = ether / arp_request

answered, unanswered = srp(
    packet,
    timeout=2,
    verbose=False
)


# Output
print()
print("===== DEVICES =====")
print()
print(f"{'IP':<17} MAC")
print("-" * 35)

# Own device
print(f"{own_ip:<17} {own_mac}")

# Other devices
for sent, received in answered:

    ip = received[ARP].psrc
    mac = received[ARP].hwsrc

    if ip != own_ip:
        print(f"{ip:<17} {mac}")