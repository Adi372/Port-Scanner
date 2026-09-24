import socket
import threading

host = "127.0.0.1"

def portScan(host, port):

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(3)

    try:
        client.connect((host, port))
        banner = client.recv(1024).decode(errors="ignore").strip()

        if banner.startswith("SSH"):
            service = "SSH"

        elif banner.startswith("HTTP"):
            service = "HTTP"

        elif banner.startswith("FTP"):
            service = "FTP"

        elif banner.startswith("SMTP"):
            service = "SMTP"

        elif port == 21:
            service = "FTP"

        elif port == 22:
            service = "SSH"

        elif port == 25:
            service = "SMTP"

        elif port == 53:
            service = "DNS"

        elif port == 80:
            service = "HTTP"

        elif port == 110:
            service = "POP3"

        elif port == 143:
            service = "IMAP"

        elif port == 443:
            service = "HTTPS"

        elif port == 3306:
            service = "MySQL"

        elif port == 5432:
            service = "PostgreSQL"

        elif port == 6379:
            service = "Redis"

        elif port == 8080:
            service = "HTTP Proxy/Alternate HTTP"

        elif port == 8443:
            service = "HTTPS Alternate"

        else:
            service = "Unknown"

        print() 
        print(f"Port: {port}")
        print(f"Status: OPEN")
        print(f"Service: {service}")

        if banner:
            print(f"Banner: {banner}")
        else:
            print("Banner: no banner received")

    except socket.timeout:

        print(f"Port {port}: TIMEOUT")

    except ConnectionRefusedError:

        print(f"Port {port}: CLOSED")

    except OSError as e:

        print(f"Port {port}: Error: {e}")

    finally:

        client.close()


def main():

    threads = []

    print("===== TCP PORT SCANNER =====")
    port_range = input("Enter port range (example: 1-1024): ")

    try:
        start, end = map(int, port_range.split("-"))

    except ValueError:
        print("Invalid port range.")
        print("Use format: 1-1024")
        return

    if start < 1 or end > 65535 or start > end:
        print("Invalid port range.")
        return

    print()
    print(f"Target: {host}")
    print(f"Scanning ports: {start}-{end}")
    print()

    for port in range(start, end+1):

        thread = threading.Thread(
            target = portScan,
            args = (host, port)
        )

        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print()
    print("===== SCAN COMPLETE =====")


main()