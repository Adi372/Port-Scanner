from scapy.all import ARP, Ether, srp

target_ip = input("Enter target IP: ")

arp_request = ARP(pdst=target_ip)

ethernet_frame = Ether(
    dst="ff:ff:ff:ff:ff:ff"
)

packet = ethernet_frame / arp_request

answered, unanswered = srp(
    packet,
    timeout=2,
    verbose=0
)

if answered:
    response = answered[0][1]
    print()
    print(f"IP  : {response.psrc}")
    print(f"MAC : {response.hwsrc}")
else:
    print("No ARP response received.")