import socket
import threading

host = "127.0.0.1"

ports = [
    21, 22, 23, 25, 53,
    80, 110, 143, 443,
    3306, 5432, 6379,
    8080, 8443
]


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

        elif port == 21:
            service = "FTP"

        elif port == 25:
            service = "SMTP"

        elif port == 3306:
            service = "MySQL"

        elif port == 5432:
            service = "PostgreSQL"

        else:
            service = "Unknown"

        print()
        print(f"Port: {port}")
        print(f"Service: {service}")
        print(f"Banner: {banner}")

    except socket.timeout:
        print(f"Port {port}: Connection timed out")

    except ConnectionRefusedError:
        print(f"Port {port}: Connection refused")

    except Exception as e:
        print(f"Port {port}: Error: {e}")

    finally:
        client.close()


def main():

    threads = []

    for port in ports:
        thread = threading.Thread(
            target=portScan,
            args=(host, port)
        )

        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


main()