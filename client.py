import socket
import threading
import os
from sty import fg, Style, RgbFg

fg.cyann = Style(RgbFg(0, 255, 255))
os.system("")

HOST = "54.205.221.147"
PORT = 8080
BITRATE = 8192

NICKNAME = input("Enter your chat name: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
client.send(NICKNAME.encode("utf-8"))


def handle_click():
    while True:
        inp = input(f"{fg.cyann}")
        client.send(inp.encode("utf-8"))


threading.Thread(target=handle_click, daemon=True).start()

while True:
    msg = client.recv(BITRATE).decode("utf-8")
    print(msg + fg.cyann)
