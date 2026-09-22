import socket
import threading

HOST = "0.0.0.0"
PORT = 5000

clients = []
usernames = []


def broadcast(message, sender):
    for client in clients:
        if client != sender:
            try:
                client.send(message)
            except:
                pass


def handle_client(client, address):
    print(f"[CONNECTED] {address}")

    try:
        username = client.recv(1024).decode()

        if not username:
            return

        usernames.append(username)
        clients.append(client)

        print(f"[USER] {username} joined the chat")

        welcome = f"{username} joined the chat!\n"
        broadcast(welcome.encode(), client)

        while True:
            message = client.recv(1024)

            if not message:
                break

            text = f"{username}: {message.decode()}"
            print(text)

            broadcast(text.encode(), client)

    except:
        pass

    finally:
        if client in clients:
            clients.remove(client)

        if username in usernames:
            usernames.remove(username)

        client.close()

        print(f"[DISCONNECTED] {address}")

        message = f"{username} left the chat.\n"
        broadcast(message.encode(), client)


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind((HOST, PORT))
    server.listen()

    print(f"Server listening on {HOST}:{PORT}")

    while True:
        client, address = server.accept()

        thread = threading.Thread(
            target=handle_client,
            args=(client, address)
        )

        thread.start()

        print(f"[ACTIVE CLIENTS] {threading.active_count() - 1}")


start_server()