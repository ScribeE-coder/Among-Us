import pygame, Sprite 

from Sprite import Sprite 

class Ghost(Sprite): 
    def __init__(self, ghost_img, ghost_type, x, y, tasks:list, window): 
        self.ghost_type = ghost_type # ghosts can either be crew or impostors 
        self.ghost_img = ghost_img 
        self.x = x 
        self.y = y
        self.width = 0 
        self.height = 0  
        self.tasks = tasks 
        self.has_tasks = True 
        self.window = window 

        if not self.tasks: 
            self.has_tasks = False

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

    # if ghost still has tasks those tasks should still be displayed 
    def display_tasks(self): 
        if self.has_tasks: 
            return True 
        else: 
            return False 
        
    def draw(self): 
        self.window.blit(self.ghost_img, (self.x, self.y))