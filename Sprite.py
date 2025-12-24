
# characters like Impostors and Crewmates inherit from Sprite class, useful for collision detection
class Sprite: 
    def __init__(self, x, y, width, height, walk_right, walk_left, window):
        self.x = x 
        self.y = y
        self.width = width 
        self.height = height 
        self.walk_right = walk_right 
        self.walk_left = walk_left 
        self.window = window 

    def collision_check(self): 
        return 
    
    def draw(self): 
        return