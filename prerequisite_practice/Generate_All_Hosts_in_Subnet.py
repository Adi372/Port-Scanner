import ipaddress

ip = input("IP: ")
netmask = input("Netmask: ")

network = ipaddress.ip_network(
    f"{ip}/{netmask}",
    strict=False
)

for host in network.hosts():
    print(host)