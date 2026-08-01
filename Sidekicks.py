import pygame 

pygame.init() 

class Sidekick(): 
    def __init__(self, img, x, y, width, height, master, window):
        self.img = img 
        self.x = x 
        self.y = y 
        self.width = width 
        self.height = height 
        self.master = master 
        self.window = window

    def move(self): 
        offset = 3 
        self.x = self.master.x - offset 
        self.y = self.master.y - offset
        return 

    def draw(self):
        self.window.blit(self.img, (self.x, self.y))
        return 
