import sys, os 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pygame, math, os
from CrewMate import CrewMate 
from Obstacle import Circular_Obstacle, Rectangle_Obstacle
from Impostor import Monster
from Ghost import Ghost
from Vent import Vent 
import assets 

pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640 
SPRITE_DIVISOR = 15 
VENT_SPRITE_SHEET_DIVISOR = 16.2
SCREEN_WIDTH_DIVISOR = 17 
SCREEN_HEIGHT_DIVISOR = 17 


# setting up the window users will see when they play the game
window = assets.window
pygame.display.set_caption("Among Us Clone") # can remove bc of assets 
clock = pygame.time.Clock()

caf_obstacles = assets.caf_obstacles
yellow_crew = assets.characters["yellow_crew"]
monster_imp = assets.characters["monster_imp"]
caf_vent = assets.vents["cafeteria"]
ghost_listy_right = assets.sprite_imgs["ghost_move_right_sheet"]
ghost_listy_left = assets.sprite_imgs["ghost_move_left_sheet"]
vent_animation_sheet = assets.sprite_imgs["vent_animation_sheet"]

doorToMedBayHallway = Rectangle_Obstacle(-20, 295, 35, 50)
doorToStorageHallway = Rectangle_Obstacle(290, 625, 65, 30)
doortoAsteroidsHallway = Rectangle_Obstacle(629, 285, 65, 60)
HallwayBackToCaf = Rectangle_Obstacle(626, 301, 65, 30)

# TODO: add the rest of the rooms and hallways once you get all the images for this map
rooms = {
    "cafeteria": [assets.sprite_imgs["cafeteria"], caf_obstacles, {"caf_upperE_medbay_hallway": [doorToMedBayHallway, (550, 310)]}], 
    
    "caf_upperE_medbay_hallway": [assets.sprite_imgs["caf_upper_eng_Hallway1"], None, {"cafeteria": [HallwayBackToCaf, (23, 310)]}]
         } 

# creating rectangle obstacles for easier way to detect collisions 
caf_rect_obstacle = Rectangle_Obstacle(128, 50, 340, 1)
caf_obstacles.append(caf_rect_obstacle)

monster_imp.obstacles = caf_obstacles

curr_room = rooms["cafeteria"][0] 
curr_room_name = "cafeteria"

monster_imp.venting_info = {"cafeteria": [caf_vent, assets.sprite_imgs["imp_venting_image_sheet"]]}
monster_imp.curr_room_name = curr_room_name
monster_imp.venting_animation_frames = monster_imp.venting_info[curr_room_name][1]

"""COMMENT TO EXPLAIN WHY STRUCTURED LIKE THIS""" 
def draw(imgs, xcor, ycor): 
    for img in imgs: 
        window.blit(img, (xcor, ycor))

    if monster_imp.room == caf_vent.room_name and yellow_crew.room == caf_vent.room_name:
        caf_vent.draw()

    if yellow_crew.room == curr_room_name and monster_imp.room == curr_room_name:
        yellow_crew.draw()
        monster_imp.draw()

    elif yellow_crew.room == curr_room_name: 
        yellow_crew.draw() 

    elif monster_imp.room == curr_room_name: 
        monster_imp.draw()  

running = True 
while running: 
    keys = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
 
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos() 
            #print(pos)
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                monster_imp.animation_complete = False
                monster_imp.animation_playing = True
                monster_imp.current_animation_frame = 0
                monster_imp.animation_frame_count = 0   

            # without the isinstance check, monster is allowed to attack crew ghost and it causes issues in the loop
            if event.key == pygame.K_0 and not isinstance(yellow_crew, Ghost):
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

    curr_hallways_available = rooms[curr_room_name][2]
    for name, hallway_listy in curr_hallways_available.items(): 
        door = hallway_listy[0]
        if yellow_crew.rect.colliderect(door.rect): 
            curr_room_name = name 
            curr_room = rooms[curr_room_name][0]
            yellow_crew.room = curr_room_name 

            yellow_crew.x = curr_hallways_available[curr_room_name][1][0]
            yellow_crew.y = curr_hallways_available[curr_room_name][1][1]

        # should probably find a way to not split these into two different conditionals when they're doing the same thing 
        elif monster_imp.rect.colliderect(door.rect): 
            curr_room_name = name 
            curr_room = rooms[curr_room_name][0]
            monster_imp.room = curr_room_name 

            monster_imp.x = curr_hallways_available[curr_room_name][1][0]
            monster_imp.y = curr_hallways_available[curr_room_name][1][1]

    if caf_vent.open_vent_check(monster_imp): 
        caf_vent.vent_animation()
        monster_imp.vent_animation()
    else: 
        caf_vent.animation_complete = False 
        caf_vent.current_animation_frame = 0 
        caf_vent.animation_frame_count = 0 

        monster_imp.venting_animation_complete = False 
        monster_imp.venting_current_animation_frame = 0 
        monster_imp.venting_animation_frame_count = 0 
    
    window.fill((0, 0, 0))
    draw(curr_room, 0, 0)
    pygame.display.update()
    clock.tick(60)