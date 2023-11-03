from src.design.animation import animation 

class walkingRight(animation):
    def __init__(self, animationName):
        super().__init__(animationName)

        self.animation = [
            [
            [">"]
            ],
        ]
