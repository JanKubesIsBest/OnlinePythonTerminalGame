from src.design.animation import animation 

class walkingLeft(animation):
    def __init__(self, animationName):
        super().__init__(animationName)

        self.animation = [
            [
            ["<"]
            ],
        ]
