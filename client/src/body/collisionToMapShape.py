from turtle import shape
from typing import List

from numpy import append, true_divide
from src.body.body.bodyClass import body
from src.body.collision_dot import collisionDot


class collisionToMapShape(body):
    def __init__(self, id: int, positionX: int, positionY: int, parentReference: object,  shape: List, group: str, name: str, positionFromParentX=0, positionFromParentY=0,):
        super().__init__(id, positionX, positionY, parentReference, name, positionFromParentX, positionFromParentY)

        self.shape = shape
        self.group = group

        self.filled = False
        
        self.pastIndex = []
        self.pastX = parentReference.positionX
        self.pastY = parentReference.positionY

        self.name = name

        
        self.myDot = collisionDot(0, self.positionX, self.positionY, self, self.group, self.parentReference.name)

    def doYourStuff(self, world, collision_world):
        
        self.fillWorld(collision_world,)
    
    def fillWorld(self, collision_world):
        if self.filled:
            for y in range(len(self.shape)):
                for x in range(len(self.shape[y])):
                    collision_world[self.pastY + y][self.pastX + x].pop(self.find_your_self(collision_world, x, y))

        if self.positionY < len(collision_world) and self.positionX < len(collision_world[self.positionY]) and self.positionY >= 0 and self.positionX >= 0:
            self.pastX = self.positionX
            self.pastY = self.positionY
            self.pastIndex.clear()
            for y in range(len(self.shape)):
                self.pastIndex.append([])
                for x in range(len(self.shape[y])): 
                    self.myDot = collisionDot(0, self.positionX + x, self.positionY + y, self, self.group, self.parentReference.name)
                    collision_world[self.positionY + y][self.positionX + x].append(self.myDot)
                    self.pastIndex[y].append(len(collision_world[self.positionY + y][self.positionX + x]))
            self.filled = True
        else: 
            self.filled = False
    
    def find_your_self(self, collision_world, X, Y):
        for s in range(len(collision_world[self.pastY + Y][self.pastX + X])):
            lol = collision_world[self.pastY + Y][self.pastX + X][s]
            if (lol.parentReference != None):
                if (lol.name == self.myDot.name):
                    return s


    def delMySelf(self, collision_world):
        for y in range(len(self.shape)):
            for x in range(len(self.shape[y])):
                collision_world[self.positionY + y][self.positionX + x].pop(self.find_your_self(collision_world, x, y))

