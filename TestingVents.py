import pygame 
from image_loading import load_sequence 

pygame.init() 

SCREEN_WIDTH = 640 
SCREEN_HEIGHT = 640 
divisor = 15

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

cafeteria = load_sequence('amongUs_cafeteria', 1, SCREEN_WIDTH, SCREEN_HEIGHT)

test_imp = load_sequence('idle', 1, SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
test_imp_walking_right = load_sequence('crewWalk', 7, SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
test_imp_walking_left = [pygame.transform.flip(sprite, True, False) for sprite in test_imp_walking_right] 







def draw(imgs, xcor, ycor): 
    for img in imgs: 
        window.blit(img, xcor, ycor) 

running = True 
while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 

    window.fill((0, 0, 0))
    pygame.display.update() 
    clock.tick(60)