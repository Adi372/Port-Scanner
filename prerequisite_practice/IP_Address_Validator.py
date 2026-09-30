# ipaddress is a built-in Python module for working with IP addresses and networks.
import ipaddress

ip = input("Enter IP address: ")
# print(ip)

# Is this string a valid IP address, and if so, represent it as an IP address object.
# address = ipaddress.ip_address(ip)

# print(address)

# try:
#     address = ipaddress.ip_address(ip)
#     print("Valid IPv4 address")

# except ValueError:
#     print("Invalid IPv4 address")

try:
    address = ipaddress.ip_address(ip)

    if address.version == 4:
        print("Valid IPv4 address")
    else:
        print("Not an IPv4 address")
except ValueError:
    print("Invalid IP address")