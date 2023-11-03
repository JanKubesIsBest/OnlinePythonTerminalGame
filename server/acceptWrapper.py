
import socket
import selectors
import types

def accept_wrapper(sock, sel):
    sockOBJ, addr = sock.accept()  # Should be ready to read
    print(f"Accepted connection from {addr}")
    sockOBJ.setblocking(False)
    data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(sockOBJ, events, data=data)