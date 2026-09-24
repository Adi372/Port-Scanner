import subprocess
import socket


route = subprocess.run(
    ["ip", "route"],
    capture_output=True,
    text=True
)

gateway = ""
interface = ""

for line in route.stdout.splitlines():
    if line.startswith("default"):
        parts = line.split()

        gateway = parts[2]
        interface = parts[4]

        break


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


print("===== NETWORK INTERFACE INFORMATION =====")
print()
print(f"Interface : {interface}")
print(f"IPv4      : {ipv4}")
print(f"Gateway   : {gateway}")