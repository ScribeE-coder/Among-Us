import pygame
from image_loading import load_sequence 

pygame.init() 

SCREEN_WIDTH = 640 
SCREEN_HEIGHT = 640 

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
clock = pygame.time.Clock() 

"""Testing new load_sequence function so main file isn't so fucking long omfg I'm so fucked"""
cafeteria = load_sequence("amongUs_cafeteria", 1, SCREEN_WIDTH, SCREEN_HEIGHT) 

def draw(imgs, xcor, ycor): 
    for img in imgs: 
        window.blit(img, (xcor, ycor))
    
running = True 
while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 
    
    draw(cafeteria, 0, 0)
    pygame.display.update() 
    clock.tick(60) 