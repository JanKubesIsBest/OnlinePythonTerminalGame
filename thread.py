import threading

from server.server import main 

class thread(threading.Thread):
    def __init__(self, port):
        threading.Thread.__init__(self)
        self.port = port
 
        # helper function to execute the threads
    def run(self):
        main(self.port)
 