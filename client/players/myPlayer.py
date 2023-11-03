from typing import List
from players.onlinePlayer.onlinePlayer import onlinePlayer
from src.body.kinematic_body import kinematic_body

from players.animations.celebratingAnimation import celebratingAnimation
from players.animations.walking.walkingLeft import walkingLeft
from players.animations.walking.walkingRight import walkingRight
from players.animations.standing import standingAnimation
class myPlayer(onlinePlayer):
    def __init__(self, positionX: int, positionY: int, defaultSkin: str, id: int, parentReference: object, collideWith: List, name: str):
        super().__init__(positionX, positionY, defaultSkin, id, parentReference, collideWith, name)

        self.add_new_child("sprite", kinematic_body(self.positionX, self.positionY, "", len(self.childs), self,animate=True, animations=[celebratingAnimation("celebrating"), walkingRight("walkingRight"), walkingLeft("walkingLeft"), standingAnimation("standing")], firstAnimation="standing", name="kinematicBodyForPlayer"))

        self.kinematicBody = self.childs[len(self.childs) - 1][2]

    def doYourStuff(self, world, collision_world):        
        self.moveX = int(self.keyboard.is_pressed("d")) - int(self.keyboard.is_pressed("a"))
        self.moveY = int(self.keyboard.is_pressed("s")) - int(self.keyboard.is_pressed("w"))


        if (self.frames_from_celebrating > 0 and self.frames_from_celebrating < 4):
            self.frames_from_celebrating += 1
            self.moveX = 0
            self.moveY = 0
        else: 
            self.frames_from_celebrating = 0
        if self.moveX < 0:
            self.kinematicBody.changeAnimation("walkingLeft")
        elif self.moveX > 0:
            self.kinematicBody.changeAnimation("walkingRight")
        elif self.frames_from_celebrating == 0:
            self.kinematicBody.changeAnimation("standing")

        super().doYourStuff(world, collision_world)
        self.moveAndCollide(collision_world)