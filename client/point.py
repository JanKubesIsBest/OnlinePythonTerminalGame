from src.body.body.bodyClass import body

from src.body.collisionToMapShape import collisionToMapShape

class point(body):
    def __init__(self, id: int, positionX: int, positionY: int, parentReference: object, name: str, positionFromParentX=0, positionFromParentY=0):
        super().__init__(id, positionX, positionY, parentReference, name, positionFromParentX, positionFromParentY)
        self.shape = [[True]]
        self.add_new_child("collisionAdder", collisionToMapShape(len(self.childs), self.positionX, self.positionY, self, self.shape, "point", "CollisionAdderForPoint"))

        self.defaultSkin = "#"
        self.collideWith = ["player"]

        self.name = name

    def doYourStuff(self, world, collision_world):
        if self.positionY < len(collision_world) and self.positionX < len(collision_world[self.positionY]) and self.positionY >= 0 and self.positionX >= 0:

            for dot in collision_world[self.positionY][self.positionX]:
                if dot.group in self.collideWith:
                        self.childs[0][2].delMySelf(collision_world)
                        self.parentReference.all_objects.pop(self.id)
                        self.childs.pop(0)
                        self.parentReference.pointIsInGame = 0

                        del self
                        return 

        super().doYourStuff(world, collision_world)
    
    def player_hited_me(self, collision_world):
        self.childs[0][2].delMySelf(collision_world)
        self.parentReference.all_objects.pop(self.id)
        self.childs.pop(0)
        self.parentReference.pointIsInGame = 0
        self.parentReference.all_points += 1