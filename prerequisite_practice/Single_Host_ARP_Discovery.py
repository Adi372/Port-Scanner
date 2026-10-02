from scapy.all import ARP, Ether, srp

target_ip = "192.168.31.34"
arp_request = ARP(pdst=str(target_ip))

# Creates an Ethernet frame.
# dst means destination MAC address.
# FF:FF:FF:FF:FF:FF
# is the broadcast MAC address.
# It means:
# "Send this Ethernet frame to every device on my local network."
ether = Ether(dst="ff:ff:ff:ff:ff:ff")

# The / in Scapy means stack/combine layers.
# You're putting the ARP packet inside the Ethernet frame:
# Ethernet
# └── ARP

# So you have:
# Ethernet frame
#     ↓
# Destination MAC: FF:FF:FF:FF:FF:FF
#     ↓
# ARP request
#     ↓
# "Who has 192.168.31.1?"
packet = ether / arp_request

# print(packet.summary())

# srp() means: Send and Receive Packets at Layer 2.
# Ethernet is the name of a Layer-2 networking technology, but Layer 2 also exists over Wi-Fi.

# Your interface is probably: wlan0
# and it has a MAC address just like an Ethernet interface would.
# So:
# Wi-Fi → still has Layer 2
# Ethernet cable → also has Layer 2
# Why Ether() then?

# Scapy's Ether() represents the Ethernet-style Layer-2 frame structure used for this kind of packet crafting. On your Wi-Fi LAN, Scapy can still use a Layer-2 socket to send the ARP frame through your wireless interface.
# So don't think:

# Layer 2 = Ethernet cable ❌

# Think:
# Layer 2 = local-link communication + MAC addresses ✅
# Ethernet → one Layer-2 technology
# Wi-Fi    → another Layer-2 technology

answered, unanswered = srp(
    packet,
    timeout=2,
    verbose=False
)

if answered:
    reply = answered[0][1]

    print("IP Address :", reply[ARP].psrc)
    print("MAC Address:", reply[ARP].hwsrc)
else:
    print("No reply")