import ipaddress

ip = input("IP: ")
netmask = input("Netmask: ")

# In an IP address, / means CIDR/prefix length.
# 192.168.31.217/24 means: IP 192.168.31.217 with 24 network bits.

# And:
# 255.255.255.0 is equivalent to: /24

# So:
# 192.168.31.217/24 is not division. It's IP address + subnet size.

# For example:
# 192.168.31.217 is actually stored as 32 binary bits:

# 11000000 10101000 00011111 11011001

# Each group has 8 bits:
# 11000000 → 8 bits
# 10101000 → 8 bits
# 00011111 → 8 bits
# 11011001 → 8 bits

# Total:
# 8 + 8 + 8 + 8 = 32 bits
# So when we say: 192.168.31.217/24
# the /24 means: The first 24 bits identify the network, and the remaining 8 bits identify hosts within that network.


# strict=False tells Python:
# "The IP I gave you doesn't have to be the network address. Calculate the network containing it.
# Without strict=False:
# ipaddress.ip_network("192.168.31.217/24")
# Python raises an error because .217 isn't the network address.

network = ipaddress.ip_network(
    f"{ip}/{netmask}",
    strict=False
)

first = network.network_address + 1
last = network.broadcast_address - 1
hosts = network.num_addresses - 2

print()
print("Network :", network)
print("First   :", first)
print("Last    :", last)
print("Hosts   :", hosts)