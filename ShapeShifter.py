import pygame 

class ShapeShifter: 
    def __init__(self, imp_img, x, y, width, height, window, walk_right, walk_left, speed=2): 
        self.img_imp = imp_img 
        self.x = x 
        self.y = y 
        self.width = width 
        self.height = height 
        self.window = window 
        self.walk_right = walk_right 
        self.walk_left = walk_left 
        self.speed = speed 

    def ss_move_animation(self): 
        raise NotImplementedError 

    def ss_move(self): 
        raise NotImplementedError