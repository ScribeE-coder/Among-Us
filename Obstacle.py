class Obstacle(): 
    def __init__(self, x, y, radius): 
        self.x = x 
        self.y = y
        self.radius = radius 
        self.center_x = self.x 
        self.center_y = self.y
        self.width = None 
        self.height = None 

class Rectangle_Obstacle(Obstacle): 
    def __init__(self, x , y, width, height): 
        super.__init__() 
        self.x = x 
        self.y = y 
        self.width = width 
        self.height = height 


