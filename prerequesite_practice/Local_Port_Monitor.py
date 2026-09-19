import subprocess

result = subprocess.run(
    ["ss", "-tuln"],
    capture_output=True,
    text=True
)

lines = result.stdout.splitlines()

print("Listening TCP ports:")

for line in lines:

    if line.startswith("tcp") and "LISTEN" in line:

        address = line.split()[-2]
        port = address.split(":")[-1]

        print(port)