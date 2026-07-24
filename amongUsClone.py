import pygame, math, os
import Impostor 
from CrewMate import CrewMate 
from Obstacle import Circular_Obstacle, Rectangle_Obstacle
from Impostor import Monster
from image_loading import load_sequence
from Ghost import Ghost

pygame.init()
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640 
divisor = 15 

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Among Us Clone")
clock = pygame.time.Clock()

cafeteria = load_sequence("amongUs_cafeteria", 1, SCREEN_WIDTH, SCREEN_HEIGHT) 
idle_crew = load_sequence("idle", 1, SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)

crew_walking_right = load_sequence("crewWalk", 7, SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor) 
crew_walking_left = [pygame.transform.flip(sprite, True, False) for sprite in crew_walking_right]

monsterTransformList = load_sequence("impTransform", 13, SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)

monster_walk_right = load_sequence("monsterWalk", 7, SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
monster_walk_left = [pygame.transform.flip(sprite, True, False) for sprite in monster_walk_right]

monsterAttackCycle = load_sequence("monsterAttack", 12, SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)

crewDeadListy = load_sequence("crewDead", 9, SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)

ghost_listy_right = load_sequence("ghost", 16, SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor) 
ghost_listy_left = [pygame.transform.flip(sprite, True, False) for sprite in ghost_listy_right]

stat_ghosty = load_sequence("stationary_ghost", 1, SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)

cafeteriaUpperEMedbayHallway1 = load_sequence("cafeteriaUpperEMedbayHallway", 1, SCREEN_WIDTH, SCREEN_HEIGHT)

caf_obstacles = [] 

centers = {"upper_right": (443, 180), 
           "emergency": (312, 332),
           "upper_left": (173, 182), 
           "bottom_right": (444, 474),
           "bottom_left": (175, 473)
           }    

table_radius = 50
    
yellow_crew = CrewMate(idle_crew[0], 320, 250, SCREEN_WIDTH/17, SCREEN_HEIGHT/17, crew_walking_right, crew_walking_left, caf_obstacles, window, crewDeadListy)
yellow_crew.ghosty = stat_ghosty[0]

monster_imp = Monster(monsterTransformList[0], 350, 255, SCREEN_WIDTH/17, SCREEN_HEIGHT/17, monsterTransformList, window, monster_walk_right, monster_walk_left)
monster_imp.monster_attack_list = monsterAttackCycle
monster_imp.regular_imp_left = crew_walking_left # type: ignore
monster_imp.regular_imp_right = crew_walking_right # type: ignore

upper_right_table = Circular_Obstacle(centers.get("upper_right")[0], centers.get("upper_right")[1], table_radius) # type: ignore
emergency_table = Circular_Obstacle(centers.get("emergency")[0], centers.get("emergency")[1], table_radius)  # type: ignore
upper_left_table = Circular_Obstacle(centers.get("upper_left")[0], centers.get("upper_left")[1], table_radius) # type: ignore
bottom_right_table = Circular_Obstacle(centers.get("bottom_right")[0], centers.get("bottom_right")[1], table_radius)  # type: ignore
bottom_left_table = Circular_Obstacle(centers.get("bottom_left")[0], centers.get("bottom_left")[1], table_radius)  # type: ignore

tables = [upper_right_table, emergency_table, upper_left_table, bottom_right_table, bottom_left_table]  

doorToMedBayHallway = Rectangle_Obstacle(-20, 295, 35, 50)
doorToStorageHallway = Rectangle_Obstacle(290, 625, 65, 30)
doortoAsteroidsHallway = Rectangle_Obstacle(629, 285, 65, 60)
HallwayBackToCaf = Rectangle_Obstacle(626, 301, 65, 30)

rooms = {
    "cafeteria": [cafeteria, tables, {"caf_upperE_medbay_hallway": [doorToMedBayHallway, (550, 310)]}], 
    
    "caf_upperE_medbay_hallway": [cafeteriaUpperEMedbayHallway1, None, {"cafeteria": [HallwayBackToCaf, (23, 310)]}]
         } 

# storing vent location coordinates with the name of their location to be used later 
vents = {}

for table in tables: 
    caf_obstacles.append(table)

# rectangular obstacles 
caf_rect_obstacle = Rectangle_Obstacle(128, 50, 340, 1)
caf_obstacles.append(caf_rect_obstacle)

monster_imp.obstacles = caf_obstacles
tracker = 0 

curr_room = rooms["cafeteria"][0] 
curr_room_name = "cafeteria"


 # put your images on your created display    
def draw(imgs, xcor, ycor): 
    for img in imgs: 
        window.blit(img, (xcor, ycor))

    yellow_crew.draw() 
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
        monster_imp.attack(yellow_crew)

    # only update animation when cycle has started again 
    if monster_imp.animation_playing:
        monster_imp.monster_transform() # calls monster animation function
   
    elif not monster_imp.animation_playing and not monster_imp.attacking:
        monster_imp.monster_move(keys)

    yellow_crew.move(keys)

    if monster_imp.kill_landed:
        yellow_crew.killed_animation_playing = True 
        monster_imp.kill_landed = False 

    if yellow_crew.killed_animation_playing and isinstance(yellow_crew, CrewMate):
        yellow_crew.killed_animation()

        # crew mate now needs to be a ghost for the rest of the game 
        
        if yellow_crew.killed_animation_complete: 
            yellow_ghosty = Ghost(yellow_crew.ghosty, yellow_crew.x, yellow_crew.y, yellow_crew.width, yellow_crew.height, ghost_listy_right, ghost_listy_left, "crew", [], window)
            yellow_crew = yellow_ghosty
    
    window.fill((0, 0, 0))
    draw()
    pygame.display.update()
    clock.tick(60)