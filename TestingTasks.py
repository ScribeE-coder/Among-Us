import pygame 

pygame.init() 

SCREEN_WIDTH = 640 
SCREEN_HEIGHT = 640 

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()




running = True 
while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 

    window.fill((0, 0, 0))
    pygame.display.update()
    clock.tick(60)