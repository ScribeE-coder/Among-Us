import pygame 

class Obstacle(): 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
        self.center_x = self.x 
        self.center_y = self.y

    def check_collision(self): 
        raise NotImplementedError("Only Subclasses have collision methods")

class Rectangle_Obstacle(Obstacle): 
    def __init__(self, x , y, width, height): 
        super().__init__(x, y)  
        self.width = width 
        self.height = height 
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height) 
        self.obstacle_type = 'Rectangle'

    def check_collision(self, other): 
        return None 

class Circular_Obstacle(Obstacle): 
    def __init__(self, x, y, radius): 
        super().__init__(x, y)
        self.radius = radius 
        self.obstacle_type = 'Circular'

    def check_collision(self, other): 
        return None 




