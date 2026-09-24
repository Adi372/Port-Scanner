import subprocess
import ipaddress

from scapy.all import ARP, Ether, srp


# Get default network interface
route = subprocess.run(
    ["ip", "route"],
    capture_output=True,
    text=True
)

interface = ""

for line in route.stdout.splitlines():
    if line.startswith("default"):
        parts = line.split()

        interface = parts[4]
        break


# Get IPv4 address
addr = subprocess.run(
    ["ip", "addr", "show", interface],
    capture_output=True,
    text=True
)

ipv4 = ""
prefix = ""

for line in addr.stdout.splitlines():
    line = line.strip()

    if line.startswith("inet "):
        parts = line.split()
        address = parts[1]

        ipv4, prefix = address.split("/")
        break


# Calculate network
network = ipaddress.ip_network(
    f"{ipv4}/{prefix}",
    strict=False
)

print(f"Interface : {interface}")
print(f"IPv4      : {ipv4}")
print(f"Network   : {network}")
print()
print("===== ARP HOST DISCOVERY =====")


# Create ARP request for the entire network
arp_request = ARP(
    pdst=str(network)
)

# Ethernet broadcast
ethernet = Ether(
    dst="ff:ff:ff:ff:ff:ff"
)

# Combine Ethernet + ARP
packet = ethernet / arp_request


# Send ARP requests and collect replies
answered, unanswered = srp(
    packet,
    iface=interface,
    timeout=2,
    verbose=0
)


print("\n===== ACTIVE HOSTS =====")

for sent, received in answered:

    print(f"IP Address  : {received.psrc}")
    print(f"MAC Address : {received.hwsrc}")
    print()