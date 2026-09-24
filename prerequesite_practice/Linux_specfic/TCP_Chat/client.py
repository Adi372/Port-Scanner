import socket
import threading

HOST = "127.0.0.1"
PORT = 5000


def receive_messages(client):
    while True:
        try:
            message = client.recv(1024)

            if not message:
                break

            print(message.decode(), end="")

        except:
            break


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

username = input("Enter username: ")

client.send(username.encode())

thread = threading.Thread(
    target=receive_messages,
    args=(client,)
)

thread.daemon = True
thread.start()

while True:
    message = input()

    if message.lower() == "/quit":
        break

    client.send(message.encode())

client.close()