import pygame, math, os

import CrewMate, Impostor

from Obstacle import Circular_Obstacle, Rectangle_Obstacle

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640 

pygame.init()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Among Us Clone")
clock = pygame.time.Clock()

cafeteria = pygame.image.load("images/amongUs_caf.PNG") 
cafeteria = pygame.transform.scale(cafeteria, (SCREEN_WIDTH, SCREEN_HEIGHT))

yellow_crew = pygame.image.load("images/amongUs_yellowCrew.jpeg")
yellow_crew = pygame.transform.scale(yellow_crew, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))

crew_walk1 = pygame.image.load("images/crewWalk1.png") 
crew_walk2 = pygame.image.load("images/crewWalk2.png")
crew_walk3 = pygame.image.load("images/crewWalk3.png") 
crew_walk4 = pygame.image.load("images/crewWalk4.png") 
crew_walk5 = pygame.image.load("images/crewWalk5.png") 
crew_walk6 = pygame.image.load("images/crewWalk6.png") 
crew_walk7 = pygame.image.load("images/crewWalk7.png")

# squishing down images to scale 
crew_walk1 = pygame.transform.scale(crew_walk1, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
crew_walk2 = pygame.transform.scale(crew_walk2, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15)) 
crew_walk3 = pygame.transform.scale(crew_walk3, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15)) 
crew_walk4 = pygame.transform.scale(crew_walk4, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
crew_walk5 = pygame.transform.scale(crew_walk5, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
crew_walk6 = pygame.transform.scale(crew_walk6, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
crew_walk7 = pygame.transform.scale(crew_walk7, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15)) 

crew_walking_right = [crew_walk1, crew_walk2, crew_walk3, crew_walk4, crew_walk5, crew_walk6, crew_walk7] 
crew_walking_left = [pygame.transform.flip(sprite, True, False) for sprite in crew_walking_right]

impTransform1 = pygame.image.load("images/impTransform1.png")
impTransform2 = pygame.image.load("images/impTransform2.png")
impTransform3 = pygame.image.load("images/impTransform3.png")
impTransform4 = pygame.image.load("images/impTransform4.png")
impTransform5 = pygame.image.load("images/impTransform5.png")
impTransform6 = pygame.image.load("images/impTransform6.png")
impTransform7 = pygame.image.load("images/impTransform7.png")
impTransform8 = pygame.image.load("images/impTransform8.png")
impTransform9 = pygame.image.load("images/impTransform9.png")
impTransform10 = pygame.image.load("images/impTransform10.png")
impTransform11 = pygame.image.load("images/impTransform11.png")
impTransform12 = pygame.image.load("images/impTransform12.png")
impTransform13 = pygame.image.load("images/impTransform13.png")

impTransform1 = pygame.transform.scale(impTransform1, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
impTransform2 = pygame.transform.scale(impTransform2, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
impTransform3 = pygame.transform.scale(impTransform3, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
impTransform4 = pygame.transform.scale(impTransform4, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
impTransform5 = pygame.transform.scale(impTransform5, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
impTransform6 = pygame.transform.scale(impTransform6, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
impTransform7 = pygame.transform.scale(impTransform7, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
impTransform8 = pygame.transform.scale(impTransform8, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
impTransform9 = pygame.transform.scale(impTransform9, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
impTransform10 = pygame.transform.scale(impTransform10, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
impTransform11 = pygame.transform.scale(impTransform11, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
impTransform12 = pygame.transform.scale(impTransform12, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
impTransform13 = pygame.transform.scale(impTransform13, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))

imp_walk1 = None 
imp_walk2 = None 

imp_transform_list = [impTransform1, impTransform2, impTransform3, impTransform4, impTransform5, impTransform6, impTransform7, impTransform8, impTransform9, impTransform10, impTransform11, impTransform12, impTransform13]

imp_movement_list = [] 

obstacles = [] 

centers = {"upper_right": (443, 180), 
           "emergency": (312, 332),
           "upper_left": (173, 182), 
           "bottom_right": (444, 474),
           "bottom_left": (175, 473)
           }    

table_radius = 50
    
yellow_crew = CrewMate.CrewMate(yellow_crew, 320, 380, SCREEN_WIDTH/17, SCREEN_WIDTH/17, crew_walking_right, crew_walking_left, obstacles, window) 

monster_imp = Impostor.Impostor(imp_transform_list[0], 350, 380, SCREEN_WIDTH/17, SCREEN_HEIGHT/17, imp_transform_list, window)

upper_right_table = Circular_Obstacle(centers.get("upper_right")[0], centers.get("upper_right")[1], table_radius)
emergency_table = Circular_Obstacle(centers.get("emergency")[0], centers.get("emergency")[1], table_radius) 
upper_left_table = Circular_Obstacle(centers.get("upper_left")[0], centers.get("upper_left")[1], table_radius)
bottom_right_table = Circular_Obstacle(centers.get("bottom_right")[0], centers.get("bottom_right")[1], table_radius) 
bottom_left_table = Circular_Obstacle(centers.get("bottom_left")[0], centers.get("bottom_left")[1], table_radius) 

tables = [upper_right_table, emergency_table, upper_left_table, bottom_right_table, bottom_left_table]  

for table in tables: 
    obstacles.append(table)

# rectangular obstacles 
caf_rect_obstacle = Rectangle_Obstacle(128, 50, 340, 0)
obstacles.append(caf_rect_obstacle) 

 # put your images on your created display    
def draw(): 
    window.blit(cafeteria, (0, 0))
    yellow_crew.crew_draw() 
    monster_imp.draw()

running = True 

while running: 
    keys = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos() 
            print(pos)
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                
                # reset and start animation will implement timer later
                monster_imp.animation_complete = False
                monster_imp.animation_playing = True
                monster_imp.current_frame = 0
                monster_imp.animation_frame_count = 0

    # only update animation when cycle has started again
    if monster_imp.animation_playing:
        monster_imp.monster_transform()

    yellow_crew.crew_move(keys) 
    monster_imp.imp_move(keys)
    draw()
    pygame.display.update()
    clock.tick(60)