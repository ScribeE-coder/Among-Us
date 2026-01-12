import pygame, math, os

import CrewMate, Impostor, Ghost

from Obstacle import Circular_Obstacle, Rectangle_Obstacle

from Impostor import Monster

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640 
divisor = 15 

pygame.init()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Among Us Clone")
clock = pygame.time.Clock()

# function makes file clean and easier to read 
def load_img(file_path, scale_width, scale_height): 
    img = pygame.image.load(file_path)
    img = pygame.transform.scale(img, ((scale_width, scale_height)))
    return img 

cafeteria = load_img("images/amongUS_caf.PNG", SCREEN_WIDTH, SCREEN_HEIGHT) 

yellow_crew = load_img("images/amongUs_yellowCrew.jpeg", SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
idle_crew = load_img("images/idle.png", SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor) 

crew_walk1 = load_img("images/crewWalk1.png", SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
crew_walk2 = load_img("images/crewWalk2.png", SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
crew_walk3 = load_img("images/crewWalk3.png", SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
crew_walk4 = load_img("images/crewWalk4.png", SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
crew_walk5 = load_img("images/crewWalk5.png", SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
crew_walk6 = load_img("images/crewWalk6.png", SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
crew_walk7 = load_img("images/crewWalk7.png", SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)


crew_walking_right = [crew_walk1, crew_walk2, crew_walk3, crew_walk4, crew_walk5, crew_walk6, crew_walk7] 
crew_walking_left = [pygame.transform.flip(sprite, True, False) for sprite in crew_walking_right]

monsterTransform1 = load_img("images/impTransform1.png", SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
monsterTransform2 = load_img("images/impTransform2.png", SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
monsterTransform3 = load_img("images/impTransform3.png", SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
monsterTransform4 = load_img("images/impTransform4.png", SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
monsterTransform5 = load_img("images/impTransform5.png", SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
monsterTransform6 = load_img("images/impTransform6.png", SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
monsterTransform7 = load_img("images/impTransform7.png", SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
monsterTransform8 = load_img("images/impTransform8.png", SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
monsterTransform9 = load_img("images/impTransform9.png", SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
monsterTransform10 = load_img("images/impTransform10.png", SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
monsterTransform11 = load_img("images/impTransform11.png", SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
monsterTransform12 = load_img("images/impTransform12.png", SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
monsterTransform13 = load_img("images/impTransform13.png", SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)

monster_transform_list = [monsterTransform1, monsterTransform2, monsterTransform3, monsterTransform4, monsterTransform5, monsterTransform6, monsterTransform7, monsterTransform8, monsterTransform9, monsterTransform10, monsterTransform11, monsterTransform12, monsterTransform13]

monsterWalk1 = load_img("images/monsterWalk1.png", SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
monsterWalk2 = load_img("images/monsterWalk2.png", SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
monsterWalk3 = load_img("images/monsterWalk3.png", SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
monsterWalk4 = load_img("images/monsterWalk4.png", SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
monsterWalk5 = load_img("images/monsterWalk5.png", SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor) 
monsterWalk6 = load_img("images/monsterWalk6.png", SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor) 
monsterWalk7 = load_img("images/monsterWalk7.png", SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)


monster_walk_right = [monsterWalk1, monsterWalk2, monsterWalk3, monsterWalk4, monsterWalk5, monsterWalk6, monsterWalk7]
monster_walk_left = [pygame.transform.flip(sprite, True, False) for sprite in monster_walk_right] 

# animation cycle for monster attacking 

monsterAttack1 = load_img('images/monsterAttack1.png', SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
monsterAttack2 = load_img('images/monsterAttack2.png', SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
monsterAttack3 = load_img('images/monsterAttack3.png', SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
monsterAttack4 = load_img('images/monsterAttack4.png', SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
monsterAttack5 = load_img('images/monsterAttack5.png', SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
monsterAttack6 = load_img('images/monsterAttack6.png', SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
monsterAttack7 = load_img('images/monsterAttack7.png', SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
monsterAttack8 = load_img('images/monsterAttack8.png', SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
monsterAttack9 = load_img('images/monsterAttack9.png', SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
monsterAttack10 = load_img('images/monsterAttack10.png', SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
monsterAttack11 = load_img('images/monsterAttack11.png', SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
monsterAttack12 = load_img('images/monsterAttack12.png', SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)

monster_attack_cycle = [monsterAttack1, monsterAttack2, monsterAttack3, monsterAttack4, monsterAttack5, monsterAttack6, monsterAttack7, monsterAttack8, monsterAttack9, monsterAttack10, monsterAttack11, monsterAttack12]

crewDead1 = load_img('images/crewDead1.png', SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
crewDead2 = load_img('images/crewDead2.png', SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
crewDead3 = load_img('images/crewDead4.png', SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
crewDead4 = load_img('images/crewDead4.png', SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
crewDead5 = load_img('images/crewDead5.png', SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
crewDead6 = load_img('images/crewDead6.png', SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
crewDead7 = load_img('images/crewDead7.png', SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor) 
crewDead8 = load_img('images/crewDead8.png', SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor) 
crewDead9 = load_img('images/crewDead9.png', SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)

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

yellow_ghost = Ghost()

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
    # if yellow crew is killed, play kill animation, then reassign yellow crew to ghost 
    if yellow_crew.killed: 
        yellow_crew.been_killed() 
    
    draw()
    pygame.display.update()
    clock.tick(60)