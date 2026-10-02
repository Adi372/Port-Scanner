from scapy.all import ARP, sr1
# Scapy is a Python library used to create, send, receive, and analyze network packets.
# On a local network, ARP (Address Resolution Protocol) is used to discover the MAC address associated with an IPv4 address.

target_ip = "192.168.31.217"

# This creates an ARP packet asking for the MAC address of the target IP.
# ARP(...) creates an ARP packet using Scapy.
# pdst means protocol destination.
# It tells Scapy: "This ARP request is about this IP address."
arp_request = ARP(pdst=target_ip)

# It gives a short description of the packet.
print(arp_request.summary())

# sr1() means: Send the packet and wait for one reply.
# timeout=2 means wait up to 2 seconds for a response.
# verbose=False simply prevents Scapy from printing extra information.
reply = sr1(arp_request, timeout=5, verbose=False)

# if reply:
#     print(reply.summary())
# else:
#     print("No reply")

if reply:
    # hwsrc means hardware source.
    print("MAC Address:", reply.hwsrc)
else:
    print("No reply")