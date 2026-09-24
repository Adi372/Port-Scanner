import ipaddress

from scapy.all import ARP, Ether, srp


network_input = input("Enter local network: ")

network = ipaddress.ip_network(
    network_input,
    strict=False
)

print()
print(f"Network: {network}")
print()
print("===== ARP DEVICE DISCOVERY =====")


# Generate ARP request
arp_request = ARP(
    pdst=str(network)
)

# Ethernet broadcast
ethernet_frame = Ether(
    dst="ff:ff:ff:ff:ff:ff"
)

# Combine Ethernet + ARP
packet = ethernet_frame / arp_request


# Send ARP requests and collect replies
answered, unanswered = srp(
    packet,
    timeout=2,
    verbose=0
)


print()
print("IP Address       MAC Address")
print("---------------------------------")

for sent, received in answered:

    print(
        f"{received.psrc:<16} "
        f"{received.hwsrc}"
    )