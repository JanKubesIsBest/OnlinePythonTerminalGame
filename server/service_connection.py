import random
import selectors
import json
from src.body.player import player

def service_connection(key, mask, all_points, sel, players, playersInfo, worldSkins, serverGame, pointPosition, heigth, width):
    sock = key.fileobj
    data = key.data
    
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(4024)
        if recv_data:
            data.outb += recv_data
            recv_data = recv_data.decode()
            recv_data = json.loads(recv_data)
            if recv_data["playerName"] not in players:
                players.append(recv_data["playerName"])
                playersInfo.append(recv_data)
                worldSkins.append(recv_data["skin"])
                serverGame.add_new_child(recv_data["playerName"], player(recv_data["x"], recv_data["y"], recv_data["skin"], len(players), serverGame, []))
            else:
                serverGame.all_objects[players.index(recv_data["playerName"])][2].positionX = recv_data["x"]
                serverGame.all_objects[players.index(recv_data["playerName"])][2].positionY = recv_data["y"]

                if (recv_data["points"] != playersInfo[players.index(recv_data["playerName"])]["points"]):
                    pointPosition[0] = random.randint(0, heigth - 1)
                    pointPosition[1] = random.randint(0, width - 1)

                    all_points += 1

                playersInfo[players.index(recv_data["playerName"])] = recv_data
        else:
            print(f"Closing connection to {data.addr}")
            sel.unregister(sock)
            sock.close()
        if recv_data:
            data = json.dumps({"playersInfo": playersInfo, "pointPositionY": pointPosition[0], "pointPositionX": pointPosition[1], "all_points": all_points})
            data = data.encode()
            sock.sendall(data)
    #except:
     #   print("no data")
        #print("Connection closed with: " + str(data.addr))
        #print("Or error caused a connection closing")
        #sock.close()
        #sel.unregister(sock)   