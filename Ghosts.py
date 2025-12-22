import pygame 

class Ghost: 
    def __init__(self, ghost_type, x, y, has_tasks:bool): 
        self.ghost_type = ghost_type
        self.x = x 
        self.y = y
        self.width = 0 
        self.height = 0  
        self.has_tasks = has_tasks 

        pygame.Rect(self.x, self.y, self.width, self.height) 

    def ghost_move(self, keys): 
        if keys[pygame.K_w]: 
            self.y -= 1 
        
        if keys[pygame.K_a]: 
            self.x -= 1 
        
        if keys[pygame.K_s]: 
            self.y += 1 
        
        if keys[pygame.K_d]: 
            self.x += 1 