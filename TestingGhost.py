import pygame 
from image_loading import load_sequence 
from CrewMate import CrewMate 
from Ghost import Ghost 
from Impostor import Monster, Impostor 

pygame.init() 

SCREEN_WIDTH = 640 
SCREEN_HEIGHT = 640 
divisor = 17 

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock() 
divisor = 17 

# loading in images for testing 
cafeteria = load_sequence("amongUs_cafeteria", 1, SCREEN_WIDTH, SCREEN_HEIGHT) 

test_crew_idle = load_sequence("idle", 1, SCREEN_WIDTH, SCREEN_HEIGHT)
test_crew_dead_imgs = load_sequence("crewDead", 7, SCREEN_WIDTH, SCREEN_HEIGHT)
test_crew_ghost_imgs = load_sequence("ghost", 48, SCREEN_WIDTH, SCREEN_HEIGHT)
test_crew_walk_right_imgs = load_sequence("crewWalk", 7, SCREEN_WIDTH, SCREEN_HEIGHT)
test_crew_walk_left_imgs = [pygame.transform.flip(sprite, True, False) for sprite in test_crew_walk_right_imgs]

test_imp_walk_imgs = load_sequence("crewWalk", 7, SCREEN_WIDTH, SCREEN_HEIGHT)
test_imp_transform_imgs = load_sequence("impTransform", 13, SCREEN_WIDTH, SCREEN_HEIGHT)
test_monster_walk_imgs = load_sequence("monsterWalk", 7, SCREEN_WIDTH, SCREEN_HEIGHT)
test_monster_attack_imgs = load_sequence("monsterAttack", 12, SCREEN_WIDTH, SCREEN_HEIGHT) 


# setting up sprites for testing 
test_crew = CrewMate(test_crew_idle[0], 320, 250, SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor, )


running = True 
while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False

    window.fill((0, 0, 0)) 