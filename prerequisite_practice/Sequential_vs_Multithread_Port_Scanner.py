import socket
import time

# A worker is simply something that performs a task.
# In our scanner:
# Task → scan port 53
# Worker → performs the scan
# With sequential scanning:
# Worker
#   │
#   ├── scan port 1
#   ├── scan port 2
#   ├── scan port 3
#   └── scan port 4

# Only one worker is doing everything.
# With multithreading:
# Worker 1 → port 1
# Worker 2 → port 2
# Worker 3 → port 3
# Worker 4 → port 4
# Now multiple ports can be tested at roughly the same time.
# The executor manages the workers
from concurrent.futures import ThreadPoolExecutor, as_completed

def scan_port(host, port):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((host, port))

    sock.close()

    if (result == 0):
        return port

    return None

host = input("Enter host: ")
futures = []

# Allow up to 10 worker threads to run tasks at the same time
with ThreadPoolExecutor(max_workers=10) as executor:
    for port in range(1, 101):
        future = executor.submit(scan_port, host, port)
        futures.append(future)

        # Why as_completed()?
        # You submitted:
        # Port 1
        # Port 2
        # Port 3
        # ...
        # Port 100

        # But they won't necessarily finish in that order.
        # For example:
        # Port 1   → still running
        # Port 2   → still running
        # Port 3   → finished
        # Port 4   → still running
        # Port 5   → finished
        # as_completed(futures) gives you each Future as soon as its task finishes.

    for future in as_completed(futures):
        result = future.result()
        
        if result is not None:
            print(result, "OPEN")