import pygame 

class Vent: 
    def __init__(self, x, y, width, height, window): 
        self.x = x 
        self.y = y  
        self.width = width 
        self.height = height 
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.window = window 
        self.last_update = pygame.time.get_ticks() 
        self.animation_complete = False 

    # checking whether sprite can actually vent before animation plays 
    def open_vent_check(self, sprite): 
        if sprite.can_vent and self.rect.colliderect(sprite.rect):
            return True
        else: 
            return False
        
    def vent_animation(self): 
        if self.animation_complete: 
            return 
        now = pygame.time.get_ticks() 
        if now - self.last_update > 100: 
            self.last_update = now 



    def draw(self): 
        return 
