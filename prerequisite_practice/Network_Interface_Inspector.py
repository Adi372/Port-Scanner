# psutil is a Python library that lets you inspect information about the operating system.
import psutil
# A Python socket is an interface that lets a program communicate with another program/device over a network.
import socket

# This function gets the addresses assigned to network interfaces.
interfaces = psutil.net_if_addrs()

print("===== NETWORK INTERFACES =====")
print()

# print(interfaces)

for interface in interfaces:
    # print(interface)

    ipv4 = None
    netmask = None
    mac = None

    addresses = interfaces[interface]

    for address in addresses:
        # print(address)
        # print("Family :", address.family)
        # print("Address:", address.address)
        # print("Netmask:", address.netmask)
        # print()

        if address.family == socket.AF_INET:
            ipv4 = address.address
            netmask = address.netmask

        elif address.family == psutil.AF_LINK:
            mac = address.address

    print(f"Interface: {interface}")
    print(f"IPv4     : {ipv4}")
    print(f"Netmask  : {netmask}")
    print(f"MAC      : {mac}")
    print()

# print(socket.AF_INET)
# 2 is simply the numeric value assigned to AF_INET by your operating system
# print(psutil.AF_LINK)
# 17 is the numeric value that psutil uses for AF_LINK on your system
# AF_LINK is an address-family identifier for link-layer addresses, such as MAC addresses.