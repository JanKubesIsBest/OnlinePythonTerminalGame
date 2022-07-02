from flask import Flask
from thread import thread

app = Flask(__name__)


ports = []
last_port = 3000

threads = []

@app.route('/new_game')
def hello():
    global last_port
    last_port += 1
    ports.append(last_port + 1)
    game_thread = thread(ports[len(ports) - 1])
    threads.append(game_thread)

    threads[len(threads) - 1].start()
    return str(ports[len(ports) - 1])

#@app.route("/connect_to_game")
#def connect_to_game():
#    return str(ports)

@app.route("/list")
def connect_to_game():
    return str(ports)


