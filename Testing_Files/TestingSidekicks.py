import pygame
from Sidekicks import Sidekick
from image_loading import load_sequence

pygame.init() 

SCREEN_WIDTH = 640 
SCREEN_HEIGHT = 640 
divisor = 15
clock = pygame.time.Clock() 

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

cafeteria = load_sequence("amongUs_cafeteria", 1, SCREEN_WIDTH, SCREEN_HEIGHT)
medbay_sheet = load_sequence("medBay", 1, SCREEN_WIDTH, SCREEN_HEIGHT)
medbay_room = medbay_sheet[0].subsurface(pygame.Rect(6, 18, 521, 519))
scanner = medbay_sheet[0].subsurface(pygame.Rect(545, 19, 147, 93))
computer = medbay_sheet[0].subsurface(pygame.Rect(694, 19, 104, 123))

def draw(): 
    window.blit(cafeteria[0], (0, 0))
    return 


running = True 
while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False

    window.fill((0, 0, 0))
    draw() 
    pygame.display.update()
    clock.tick()
    
