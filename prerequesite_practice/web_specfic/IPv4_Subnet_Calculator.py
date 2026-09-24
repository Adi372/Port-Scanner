import ipaddress

address = input("Enter IPv4 address with CIDR: ")
network = ipaddress.ip_network(
    address,
    strict=False
)

print()
print(f"Network:   {network.network_address}")
print(f"Broadcast: {network.broadcast_address}")
print(f"Netmask:   {network.netmask}")
print(f"Host count: {network.num_addresses - 2}")