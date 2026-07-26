import pygame 
from image_loading import load_sequence

pygame.init() 

class Sidekick(): 
    def __init__(self, img, x, y, width, height, main, window):
        self.img = img 
        self.x = x 
        self.y = y 
        self.width = width 
        self.height = height 
        self.main = main
        self.window = window

    def move(self): 
        main.x 
        return 

    def draw(self):
        self.window.blit(self.img, (self.x, self.y))
        return 
