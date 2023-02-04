

import socket
import threading
from ChessBoard import ChessBoard
import pickle
import time

HEADER = 64
PORT = 5050


SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print("New Connection {addr} connected.")

    connected = True
    while connected:

        msg = conn.recv()



def start():
    server.listen()

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))

        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("Server is starting...")
if __name__ == "__main__":

    pass