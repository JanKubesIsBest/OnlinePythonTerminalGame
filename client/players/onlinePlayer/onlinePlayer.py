from typing import List
from src.body.player import player
from src.body.collisionToMapShape import collisionToMapShape
from src.body.collision_shape_detector import collision_shape_detector



class onlinePlayer(player):
    def __init__(self, positionX: int, positionY: int, defaultSkin: str, id: int, parentReference: object, collideWith: List, name: str):
        super().__init__(positionX, positionY, defaultSkin, id, parentReference, collideWith, name)
        self.shape = [[True]]
        self.add_new_child("collisionShape", collisionToMapShape(len(self.childs), self.positionX, self.positionY, self, self.shape, "player", self.name))
        self.add_new_child("collision_shape_detector", collision_shape_detector(len(self.childs), self.positionX, self.positionY, self, self.shape, ["point"], get_point, "collision_detector_for_player"))

        self.frames_from_celebrating = 0

    def doYourStuff(self, world, collision_world):
        super().doYourStuff(world, collision_world)
        
        
    
def get_point(player, point, collision_world):
        player.points += 1
        player.parentReference.need_new_point = True
        point.player_hited_me(collision_world)
        if len(player.childs) == 3:
            player.childs[2][2].changeAnimation("celebrating")

        player.frames_from_celebrating = 1