import ipaddress
address = input("Enter network: ")

network = ipaddress.ip_network(
    address,
    strict=False
)

print("\n===== IP RANGE =====")

for ip in network.hosts():
    print(ip)