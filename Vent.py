import pygame

class Vent: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y  
        
        # won't be needed until MUCH later 
        self.connects_to = None
        self.vent_animation_frames = [] 
        self.is_open = False 

        self.animation_complete = False

    def oepn_vent_check(self, sprite): 
        if (self.x - sprite.x) == 0 and (self.y - sprite.y) == 0: 
            return True 
        else: 
            return False 
        
    def vent_animation(self): 


