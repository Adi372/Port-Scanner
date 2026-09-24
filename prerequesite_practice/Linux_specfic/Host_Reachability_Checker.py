import subprocess
import ipaddress

route = subprocess.run(
    ["ip", "route"],
    capture_output=True,
    text=True
)

interface = ""

for line in route.stdout.splitlines():
    if line.startswith("default"):
        parts = line.split()

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


network = ipaddress.ip_network(
    f"{ipv4}/{prefix}",
    strict=False
)

print(f"Interface : {interface}")
print(f"IPv4      : {ipv4}")
print(f"Network   : {network}")
print()
print("===== HOST DISCOVERY =====")


active_hosts = []

for ip in network.hosts():

    result = subprocess.run(
        ["ping", "-c", "1", "-W", "0.1", str(ip)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    print(f"Checking {ip}...")

    if result.returncode == 0:
        active_hosts.append(ip)
        print(f"{ip} appears to be reachable.")

print("\n===== ACTIVE HOSTS =====")
for ip in active_hosts:
    print(ip)