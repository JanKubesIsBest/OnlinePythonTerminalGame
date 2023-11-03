from typing import final
from numpy import byte
import socket
import json

from src.game.game import game
from players.onlinePlayer.onlinePlayer import onlinePlayer
from players.myPlayer import myPlayer

from point import point

class myGame(game):
    def __init__(self, world, collision_world, fps, playerName: str, playerSkin: str, port: int):
        super().__init__(world, collision_world, fps)

        self.HOST = "127.0.0.1" 
        self.PORT = port

        self.playerName = playerName
        self.playerSkin = playerSkin
  
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.sock.connect((self.HOST, self.PORT))

        self.playersInfo = []
        self.allreadyAddedPlayers = []

        self.myPlayerRef = False

        self.myPlayerAdded = False

        self.pointIsInGame = 0
        
        self.pastPointX = 0
        self.pastPointY = 0

        self.all_points = 0

        self.need_new_point = True


    def do_game_logic(self):
        # Worlds will be merged here\
        if self.myPlayerAdded != True:
            data = json.dumps({"playerName": self.playerName, "skin": self.playerSkin, "x": 0, "y": 0, "points": 0, "all_points": 0})
            data = data.encode()
            self.sock.sendall(data)
        else:
            data = json.dumps({"playerName": self.playerName, "skin": self.playerSkin, "x": self.myPlayerRef.positionX, "y": self.myPlayerRef.positionY, "points": self.myPlayerRef.points, "all_points": self.all_points})
            data = data.encode()
            self.sock.sendall(data)

        #except:
        #    print("Connection lost")
        #    self.sock.close()
        newPlayersInfo = self.sock.recv(1024)
        newPlayersInfo = newPlayersInfo.decode()
        newPlayersInfo = json.loads(newPlayersInfo)


        if (self.need_new_point):
            self.pointIsInGame = 1

            if (len(self.all_objects) > 0):
                if (self.all_objects[0][2].name == "point"):
                    self.all_objects.pop(0)

            self.pastPointX = newPlayersInfo["pointPositionX"]
            self.pastPointY = newPlayersInfo["pointPositionY"]
            self.add_new_child_to_the_start("point", point(0, self.pastPointX, self.pastPointY, self, "point"))

            self.need_new_point = False

            


        newPlayersInfo = newPlayersInfo["playersInfo"]

        if newPlayersInfo != self.playersInfo or self.myPlayerAdded != True:
            for player in newPlayersInfo:
                if player["playerName"] == self.playerName and self.playerName not in self.allreadyAddedPlayers:
                    self.add_new_child(player["playerName"], myPlayer(0, 0, self.playerSkin, len(self.all_objects), self, [], player["playerName"]))
                    self.allreadyAddedPlayers.append(player["playerName"])
                    self.myPlayerAdded = True
                    self.myPlayerRef = self.all_objects[self.allreadyAddedPlayers.index(player["playerName"]) + self.pointIsInGame][2]
                elif player["playerName"] not in self.allreadyAddedPlayers:
                    self.add_new_child(player["playerName"], onlinePlayer(player["x"], player["y"], player["skin"], len(self.all_objects), self, [], player["playerName"]))
                    self.allreadyAddedPlayers.append(player["playerName"])
                else:
                    index = self.allreadyAddedPlayers.index(player["playerName"]) + self.pointIsInGame
                    self.all_objects[index][2].positionX = player["x"]
                    self.all_objects[index][2].positionY = player["y"]
        self.playersInfo = newPlayersInfo




        super().do_game_logic()
    
    def getPlayers(self, name):
        pass


