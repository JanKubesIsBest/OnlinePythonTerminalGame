from ast import List, Str
from re import I
from turtle import position
from src.body.body.bodyClass import body

class collision_shape_detector(body):
    def __init__(self, id: int, positionX: int, positionY: int, parentReference: object, shape: List, collideWith: List, func, name: str):
        super().__init__(id, positionX, positionY, parentReference, name)

        self.shape = shape

        self.collideWith = collideWith
        self.collided = False

        self.defaultSkin = " "

        self.name = name
        self.func = func

        self.hitedObject = 0

    def doYourStuff(self, world, collision_world):
        if self.look_for_collision(collision_world, self.parentReference.positionX, self.parentReference.positionY):
            # every function passed to an collision_shape_detector has to have a parent reference and reference to hited object and as usual a collision_world
            self.func(self.parentReference, self.hitedObject.parentReference.parentReference, collision_world)
        return super().doYourStuff(world, collision_world)

    def look_for_collision(self, collision_world, positionX, positionY):
        for y in range(len(self.shape)):
            for x in range(len(self.shape[y])):
                if (self.shape[y][x]):
                    
                    self.collided = self._look_for_collision(collision_world, positionY + y, positionX + x)
                    if self.collided:
                        self.newPosX = positionX + x
                        self.newPosY = positionY + y
                        return self.collided

        return False
                        
    
    def _look_for_collision(self, collision_world, newPositionY, newPositionX):
        if self.positionY < len(collision_world) and self.positionX < len(collision_world[self.positionY]) and self.positionY >= 0 and self.positionX >= 0:

            for y in collision_world[newPositionY][newPositionX]:         
                if y.group in self.collideWith:
                    self.hitedObject = y
                    return y.group
            return False