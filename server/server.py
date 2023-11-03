
import socket
import selectors
from server.acceptWrapper import accept_wrapper
from server.service_connection import service_connection

from src.body.collision_dot import collisionDot
from src.game.game import game

    

def main(port):
    width = 10
    heigth = 10

    game_world = [[" "]*width for _ in range(heigth)]
    collision_world = [[[collisionDot(None, None, None, None, None)] for _ in range(width)] for _ in range(heigth)]

    pointPosition = [5, 5]


    serverGame = game(game_world, collision_world, 5)

    all_points = 0


    players = []
    playersInfo = []
    worldSkins = []

    HOST = "0.0.0.0"
    PORT = port

    sel = selectors.DefaultSelector()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen()

    print(f"Listening on http://localhost:{PORT}")

    sock.setblocking(False)
    sel.register(sock, selectors.EVENT_READ, data=None)

    try: 
        while True:
            events = sel.select(timeout=1)
    
            for key, mask in events:
                if key.data is None:
                    accept_wrapper(sock, sel)
                else:
                   service_connection(key, mask, all_points, sel, players, playersInfo, worldSkins, serverGame, pointPosition, heigth, width)
            
            serverGame.world = [[" "]*width for _ in range(heigth)]
            serverGame.do_game_logic()
    
    except KeyboardInterrupt:
        print("Socket closed because of keyboard interrupt")
    finally:
        sel.close()
    