import pygame, math, os

import CrewMate, Impostor

from Obstacle import Circular_Obstacle, Rectangle_Obstacle

from Impostor import Monster

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640 

pygame.init()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Among Us Clone")
clock = pygame.time.Clock()

def load_image(img_file): 
    file = pygame.image.load(img_file)
    return file 

def scale(img_file, scale_width, scale_height): 
    file = pygame.transform.scale(img_file, )(scale_width, scale_height)
    return file 

cafeteria = pygame.image.load("images/amongUs_caf.PNG") 
cafeteria = pygame.transform.scale(cafeteria, (SCREEN_WIDTH, SCREEN_HEIGHT))

yellow_crew = pygame.image.load("images/amongUs_yellowCrew.jpeg")
yellow_crew = pygame.transform.scale(yellow_crew, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))

idle_crew = pygame.image.load("images/idle.png")
idle_crew = pygame.transform.scale(idle_crew, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))

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

monsterTransform1 = pygame.image.load("images/impTransform1.png")
monsterTransform2 = pygame.image.load("images/impTransform2.png")
monsterTransform3 = pygame.image.load("images/impTransform3.png")
monsterTransform4 = pygame.image.load("images/impTransform4.png")
monsterTransform5 = pygame.image.load("images/impTransform5.png")
monsterTransform6 = pygame.image.load("images/impTransform6.png")
monsterTransform7 = pygame.image.load("images/impTransform7.png")
monsterTransform8 = pygame.image.load("images/impTransform8.png")
monsterTransform9 = pygame.image.load("images/impTransform9.png")
monsterTransform10 = pygame.image.load("images/impTransform10.png")
monsterTransform11 = pygame.image.load("images/impTransform11.png")
monsterTransform12 = pygame.image.load("images/impTransform12.png")
monsterTransform13 = pygame.image.load("images/impTransform13.png")

monsterTransform1 = pygame.transform.scale(monsterTransform1, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
monsterTransform2 = pygame.transform.scale(monsterTransform2, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
monsterTransform3 = pygame.transform.scale(monsterTransform3, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
monsterTransform4 = pygame.transform.scale(monsterTransform4, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
monsterTransform5 = pygame.transform.scale(monsterTransform5, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
monsterTransform6 = pygame.transform.scale(monsterTransform6, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
monsterTransform7 = pygame.transform.scale(monsterTransform7, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
monsterTransform8 = pygame.transform.scale(monsterTransform8, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
monsterTransform9 = pygame.transform.scale(monsterTransform9, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
monsterTransform10 = pygame.transform.scale(monsterTransform10, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
monsterTransform11 = pygame.transform.scale(monsterTransform11, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
monsterTransform12 = pygame.transform.scale(monsterTransform12, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
monsterTransform13 = pygame.transform.scale(monsterTransform13, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))

monster_transform_list = [monsterTransform1, monsterTransform2, monsterTransform3, monsterTransform4, monsterTransform5, monsterTransform6, monsterTransform7, monsterTransform8, monsterTransform9, monsterTransform10, monsterTransform11, monsterTransform12, monsterTransform13]

monsterWalk1 = pygame.image.load("images/monsterWalk1.png")
monsterWalk2 = pygame.image.load("images/monsterWalk2.png")
monsterWalk3 = pygame.image.load("images/monsterWalk3.png")
monsterWalk4 = pygame.image.load("images/monsterWalk4.png")
monsterWalk5 = pygame.image.load("images/monsterWalk5.png")
monsterWalk6 = pygame.image.load("images/monsterWalk6.png")
monsterWalk7 = pygame.image.load("images/monsterWalk7.png")

monsterWalk1 = pygame.transform.scale(monsterWalk1, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
monsterWalk2 = pygame.transform.scale(monsterWalk2, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
monsterWalk3 = pygame.transform.scale(monsterWalk3, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
monsterWalk4 = pygame.transform.scale(monsterWalk4, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
monsterWalk5 = pygame.transform.scale(monsterWalk5, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
monsterWalk6 = pygame.transform.scale(monsterWalk6, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
monsterWalk7 = pygame.transform.scale(monsterWalk7, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15)) 

monster_walk_right = [monsterWalk1, monsterWalk2, monsterWalk3, monsterWalk4, monsterWalk5, monsterWalk6, monsterWalk7]
monster_walk_left = [pygame.transform.flip(sprite, True, False) for sprite in monster_walk_right] 

# animation cycle for monster attacking 
monsterAttack1 = pygame.image.load('images/monsterAttack1.png')
monsterAttack2 = pygame.image.load('images/monsterAttack2.png')
monsterAttack3 = pygame.image.load('images/monsterAttack3.png')
monsterAttack4 = pygame.image.load('images/monsterAttack4.png')
monsterAttack5 = pygame.image.load('images/monsterAttack5.png')
monsterAttack6 = pygame.image.load('images/monsterAttack6.png')
monsterAttack7 = pygame.image.load('images/monsterAttack7.png')
monsterAttack8 = pygame.image.load('images/monsterAttack8.png')
monsterAttack9 = pygame.image.load('images/monsterAttack9.png')
monsterAttack10 = pygame.image.load('images/monsterAttack10.png')
monsterAttack11 = pygame.image.load('images/monsterAttack11.png')
monsterAttack12 = pygame.image.load('images/monsterAttack12.png')

monsterAttack1 = pygame.transform.scale(monsterAttack1, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
monsterAttack2 = pygame.transform.scale(monsterAttack2, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
monsterAttack3 = pygame.transform.scale(monsterAttack3, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
monsterAttack4 = pygame.transform.scale(monsterAttack4, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
monsterAttack5 = pygame.transform.scale(monsterAttack5, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
monsterAttack6 = pygame.transform.scale(monsterAttack6, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
monsterAttack7 = pygame.transform.scale(monsterAttack7, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
monsterAttack8 = pygame.transform.scale(monsterAttack8, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
monsterAttack9 = pygame.transform.scale(monsterAttack9, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
monsterAttack10 = pygame.transform.scale(monsterAttack10, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
monsterAttack11 = pygame.transform.scale(monsterAttack11, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))
monsterAttack12 = pygame.transform.scale(monsterAttack12, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))

monster_attack_cycle = [monsterAttack1, monsterAttack2, monsterAttack3, monsterAttack4, monsterAttack5, monsterAttack6, monsterAttack7, monsterAttack8, monsterAttack9, monsterAttack10, monsterAttack11, monsterAttack12]

obstacles = [] 

centers = {"upper_right": (443, 180), 
           "emergency": (312, 332),
           "upper_left": (173, 182), 
           "bottom_right": (444, 474),
           "bottom_left": (175, 473)
           }    

table_radius = 50
    
yellow_crew = CrewMate.CrewMate(idle_crew, 320, 380, SCREEN_WIDTH/17, SCREEN_WIDTH/17, crew_walking_right, crew_walking_left, obstacles, window) 

monster_imp = Monster(monster_transform_list[0], 350, 380, SCREEN_WIDTH/17, SCREEN_HEIGHT/17, monster_transform_list, window, monster_walk_right, monster_walk_left)
monster_imp.monster_attack_list = monster_attack_cycle
monster_imp.regular_imp_left = crew_walking_left
monster_imp.regular_imp_right = crew_walking_right


upper_right_table = Circular_Obstacle(centers.get("upper_right")[0], centers.get("upper_right")[1], table_radius)
emergency_table = Circular_Obstacle(centers.get("emergency")[0], centers.get("emergency")[1], table_radius) 
upper_left_table = Circular_Obstacle(centers.get("upper_left")[0], centers.get("upper_left")[1], table_radius)
bottom_right_table = Circular_Obstacle(centers.get("bottom_right")[0], centers.get("bottom_right")[1], table_radius) 
bottom_left_table = Circular_Obstacle(centers.get("bottom_left")[0], centers.get("bottom_left")[1], table_radius) 

tables = [upper_right_table, emergency_table, upper_left_table, bottom_right_table, bottom_left_table]  

for table in tables: 
    obstacles.append(table)

# rectangular obstacles 
caf_rect_obstacle = Rectangle_Obstacle(128, 50, 340, 1)
obstacles.append(caf_rect_obstacle)

monster_imp.obstacles = obstacles

 # put your images on your created display    
def draw(): 
    window.blit(cafeteria, (0, 0))
    yellow_crew.crew_draw() 
    monster_imp.draw()
    
    """ Drawing to see where exactly boundaries are for collision detection
    pygame.draw.rect(window, (255, 0, 0), caf_rect_obstacle.rect, 1)  # Red outline
    pygame.draw.rect(window, (255, 0, 0), yellow_crew.rect, 2)
    """ 

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
                monster_imp.current_animation_frame = 0
                monster_imp.animation_frame_count = 0

            if event.key == pygame.K_0:
                if monster_imp.animation_complete:
                    monster_imp.monster_attack_frame_count = 0
                    monster_imp.attacking = True 
                    monster_imp.attack_complete = False
                    monster_imp.current_attack_frame = 0
    
    if monster_imp.attacking: 
        monster_imp.attack()

    # only update animation when cycle has started again 
    if monster_imp.animation_playing:
        monster_imp.monster_transform()
   
    elif not monster_imp.animation_playing and not monster_imp.attacking:
        monster_imp.monster_move(keys)

    yellow_crew.crew_move(keys) 
    draw()
    pygame.display.update()
    clock.tick(60)