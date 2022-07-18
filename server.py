import socket
import os
import threading
from util.logger import log, fg, Style, RgbFg

os.system("")
fg.green = Style(RgbFg(0, 255, 0))

HOST = "127.0.0.1"
PORT = 8080
BITRATE = 8192

clients = {}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
log("SYSTEM", "Starting server")
server.bind((HOST, PORT))
server.listen(10)
log("SYSTEM", "Server has started")


def handle_client(client):
    while True:
        try:
            emsg = client.recv(BITRATE)
        except:
            nickname = clients[client]
            clients.pop(client)
            send_to_clients(fg.red + "[SYSTEM] " + fg.rs + f"{nickname} Left Chat")
            break
        msg = emsg.decode("UTF-8")
        full_msg = fg.green + "[{}]: " + fg.rs + "{}"
        full_msg = full_msg.format(clients[client], msg)
        send_to_clients(full_msg, client)


def send_to_clients(msg, sender=None):
    for client in clients.keys():
        if client == sender:
            continue
        client.send(msg.encode("utf-8"))


while True:
    client, addr = server.accept()
    log("INFO", "New Client Connection From \"{}\"".format(addr[0]))
    nickname = client.recv(BITRATE).decode("utf-8")
    clients[client] = nickname
    threading.Thread(target=handle_client, args=(client,), daemon=True).start()
    send_to_clients(fg.red + "[SYSTEM] " + fg.rs + f"{nickname} Joined Chat")
