from src.design.animation import animation 

class celebratingAnimation(animation):
    def __init__(self, animationName):
        super().__init__(animationName)

        self.animation = [
            [
            ["*"],
            ],
            [
            ["#"],
            ],
            [
            ["±"],
            ]
        ]
