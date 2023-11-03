from calendar import c
import os
from time import sleep
from typing import List

from myGame import myGame

from src.body.collision_dot import collisionDot
from src.rendering.canvas import canvas

from point import point




def main(port):
    #main function, everthing starts here
    print("game started...")
    running = True
    width = 10
    heigth = 10

    array = [[] for _ in range(width)]
    game_world = [[" "]*width for _ in range(heigth)]
    collision_world = [[[collisionDot(None, None, None, None, None, None)] for _ in range(width)] for _ in range(heigth)]

    playerName = input("Add your player name: ")
    print("")
    playerSkin = input("Add your player skin: ")

    myCanvas = canvas(width, heigth, game_world)
    MyGame = myGame(game_world, collision_world, 5, playerName, playerSkin, port)
    
    #adding rooted objects
    #
    while (running):
        os.system('clear')

        MyGame.world = [[" "]*width for _ in range(heigth)]

        MyGame.do_game_logic()

        myCanvas.pixels = MyGame.world
        myCanvas.draw()


        for x in MyGame.playersInfo:
            print(x["playerName"] + ": " + str(x["points"]))
        
        sleep(1 / MyGame.fps)


import requests

decision_is_making = True
print("Type c for connect, n for new server and l for list of servers currently running.")
decision = input()

list = requests.get("http://127.0.0.1:2000/list").content.decode()


while (decision_is_making):
    list = requests.get("http://127.0.0.1:2000/list").content.decode()
    if decision == "l":

        print("Excellent choice, here is your list.")
        print(list)
        print("What do you want to do now? (help for possible decisions)")
        decision = input()
    elif decision == "c":
        print("Enter server port.")
        port = int(input())
        if (str(port) in list):
            main(port)
        else:
            print("Wrong port... If you want to check list again, type l")
            print("(help for possible decisions)")
            decision = input()
    elif decision == "n":
        res = requests.get("http://127.0.0.1:2000/new_game").content.decode()

        print("Your new server was created at port: " + res)
        print("You will be redirected to that server in:")
        sleep(1)
        print("1")
        sleep(1)
        print("2")
        sleep(1)
        print("3")
        print("redirecting...")
        sleep(1)

        main(int(res))
        break

    elif decision == "help":
        print("Type c for connect, n for new server and l for list of servers currently running.")
        decision = input()
