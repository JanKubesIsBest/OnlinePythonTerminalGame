from src.body.body.bodyClass import body

class collisionDot(body):
    def __init__(self, id: int, positionX: int, positionY: int, parentReference: object, group: str, name: str):
        super().__init__(id, positionX, positionY, parentReference, name)

        self.group = group 

        self.name = name


