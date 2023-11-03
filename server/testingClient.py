import socket
from time import sleep
from typing import final

HOST = "127.0.0.1" 
PORT = 3000


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, world")
    data = s.recv(1024)
    try:
        while data:
            sleep(1)
            s.sendall(b"LOL")
            print(f"Received {data!r}")
    except KeyboardInterrupt:
        print("conection closed")
    finally: 
        s.close()

