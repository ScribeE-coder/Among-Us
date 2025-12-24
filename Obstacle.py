import pygame, math

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
        if not other.rect: 
            raise TypeError('Other object needs to have Rect attribute to detect collision') 
        else: 
            return self.rect.colliderect(other.rect) 

class Circular_Obstacle(Obstacle): 
    def __init__(self, x, y, radius): 
        super().__init__(x, y)
        self.radius = radius 
        self.obstacle_type = 'Circular'

    def check_collision(self, other): 
        if not other.center_y: 
            raise TypeError('Other object needs to have center attributes to detect collision')
        distance = math.sqrt((other.center_x - self.center_x) ** 2 + (other.center_y - self.center_y) ** 2) 





