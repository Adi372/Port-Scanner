import psutil
import socket
import ipaddress

interfaces = psutil.net_if_addrs()

print()
print("===== NETWORK INFORMATION =====")
print()

for interface in interfaces:
    ipv4 = None
    netmask = None

    addresses = interfaces[interface]

    for address in addresses:
        if address.family == socket.AF_INET:
            ipv4 = address.address
            netmask = address.netmask

            network = ipaddress.ip_network(
                f"{ipv4}/{netmask}",
                strict=False
            )

            break

    if ipv4:
        print("Interface :", interface)
        print("IP        :", ipv4)
        print("Netmask   :", netmask)
        print("Network   :", network)
        print()