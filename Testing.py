import pygame
from image_loading import load_sequence 
from CrewMate import CrewMate 

pygame.init() 

SCREEN_WIDTH = 640 
SCREEN_HEIGHT = 640 
divisor = 15 

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
clock = pygame.time.Clock() 

"""Testing new load_sequence function so main file isn't so fucking long omfg I'm so fucked"""
cafeteria = load_sequence("amongUs_cafeteria", 1, SCREEN_WIDTH, SCREEN_HEIGHT) 
yellow_crew = load_sequence("idle", 1, SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor) 
idle_crew = load_sequence("idle", 1, SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)

crew_walking_right = load_sequence("crewWalk", 7, SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor) 
crew_walking_left = [pygame.transform.flip(sprite, True, False) for sprite in crew_walking_right]
crewDeadListy = load_sequence("crewDead", 9, SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)

obstacles = [] 

test_crew = CrewMate(idle_crew[0], 320, 250, SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor, crew_walking_right, crew_walking_left, obstacles, window, crewDeadListy)

def draw(imgs, xcor, ycor): 
    for img in imgs: 
        window.blit(img, (xcor, ycor))
    test_crew.draw()
    
running = True 
while running: 
    keys = pygame.key.get_pressed()
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 

    test_crew.move(keys)
    
    draw(cafeteria, 0, 0)
    test_crew.draw()
    pygame.display.update() 
    clock.tick(60) 