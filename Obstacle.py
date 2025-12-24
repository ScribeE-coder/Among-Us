import pygame, math, Impostor, Sprite 
from Sprite import Sprite 

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
        self.type = 'Rectangle'

    def check_collision(self, other): 
        if not other.rect: 
            raise AttributeError('Other object needs to have Rect attribute to detect collision') 
        else: 
            return self.rect.colliderect(other.rect) 

class Circular_Obstacle(Obstacle): 
    def __init__(self, x, y, radius): 
        super().__init__(x, y)
        self.radius = radius 
        self.type = 'Circular'

    def check_collision(self, other): 
        if not other.center_y or not other.radius: 
            raise AttributeError('Other object needs to have center attributes to detect collision')
        
        # calculating distance betweeen centers 
        distance = math.sqrt((other.center_x - self.center_x) ** 2 + (other.center_y - self.center_y) ** 2) 

        if distance < (self.radius + other.radius): 
            return True 
        else: 
            return False
        
class Sprite_Obstacle(Obstacle): 
    def __init__(self, x, y, width, height): 
        super().__init__(x, y)
        self.width = width 
        self.height = height 
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height) 

    def check_collision(self, other): 
        if not isinstance(other, Sprite): 
            raise TypeError('Other object must be instance of Sprite class')
        elif self == other: 
            return False 
        else: 
            return self.rect.colliderect(other.rect)