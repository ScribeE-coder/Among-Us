
# characters like Impostors and Crewmates inherit from Sprite class
class Sprite: 
    def __init__(self, img, x, y, width, height, walk_right, walk_left, obstacles, window):
        self.img = img
        self.x = x 
        self.y = y
        self.width = width 
        self.height = height 
        self.walk_right = walk_right 
        self.walk_left = walk_left 
        self.obstacles = obstacles 
        self.window = window 

    def collision_check(self): 
        raise NotImplementedError("Only subclasses contain this method")
    
    def draw(self): 
        raise NotImplementedError("Only subclasses contain this method") 