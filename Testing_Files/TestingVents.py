import sys, os 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pygame 
from image_loading import load_sequence 
from CrewMate import CrewMate 
from Obstacle import Obstacle, Rectangle_Obstacle, Circular_Obstacle, Sprite_Obstacle 
from Impostor import Monster 
from Vent import Vent

pygame.init() 

SCREEN_WIDTH = 640 
SCREEN_HEIGHT = 640 
divisor = 15
vent_divisor = 16.2

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

cafeteria_imgs = load_sequence('amongUs_cafeteria', 1, SCREEN_WIDTH, SCREEN_HEIGHT)
cafeteriaUpperEMedbayHallway1 = load_sequence("cafeteriaUpperEMedbayHallway", 1, SCREEN_WIDTH, SCREEN_HEIGHT)

test_imp_img = load_sequence('idle', 1, SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
test_imp_walking_right_imgs = load_sequence('crewWalk', 7, SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
test_imp_walking_left_imgs = [pygame.transform.flip(sprite, True, False) for sprite in test_imp_walking_right_imgs] 
test_imp_transform_imgs = load_sequence("impTransform", 13, SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)

# loading in vent sprite sheet and splitting to get individual images 
vent_animation_sheet = pygame.image.load("images/amongUsVent1.png") 
frame_count = 8 # number of frames in the sprite sheet
frame_width = vent_animation_sheet.get_width() // frame_count # getting width of individual sprite from sprite sheet 
icon_bounds = [(11, 58), (70, 117), (129, 176), (187, 242), (252, 307), (318, 368), (380, 427)]
frame_height = vent_animation_sheet.get_height()
caf_vent_frames = [] # the frames needed for the animation cycle

for start, end in icon_bounds: 
    frame_rect = pygame.Rect(start, 0, end - start, frame_height)
    frame = vent_animation_sheet.subsurface(frame_rect)
    frame = pygame.transform.scale(frame, (SCREEN_WIDTH/vent_divisor, SCREEN_HEIGHT/vent_divisor))
    caf_vent_frames.append(frame)


imp_venting_images = load_sequence('Venting', 7, SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)

table_radius = 50 

centers = {"upper_right": (443, 180), 
           "emergency": (312, 332),
           "upper_left": (173, 182), 
           "bottom_right": (444, 474),
           "bottom_left": (175, 473)
           } 

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

caf_vent_img = caf_vent_frames[0]
caf_vent = Vent(565, 379, SCREEN_WIDTH/vent_divisor, SCREEN_HEIGHT/vent_divisor, window, caf_vent_frames)

vents = {"cafeteria": [caf_vent, imp_venting_images]}

rooms = {
    "cafeteria": [cafeteria_imgs, tables, {"caf_upperE_medbay_hallway": [doorToMedBayHallway, (550, 310)]}], 
    
    "caf_upperE_medbay_hallway": [cafeteriaUpperEMedbayHallway1, None, {"cafeteria": [HallwayBackToCaf, (23, 310)]}]
         } 

test_imp = Monster(test_imp_img[0], 320, 250, SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor, test_imp_transform_imgs, window, test_imp_walking_right_imgs, test_imp_walking_left_imgs)
test_imp.regular_imp_left = test_imp_walking_left_imgs 
test_imp.regular_imp_right = test_imp_walking_right_imgs

curr_room_img = rooms["cafeteria"][0]
curr_room_name = "cafeteria"

test_imp.venting_info = vents
test_imp.curr_room_name = curr_room_name
test_imp.venting_animation_frames = test_imp.venting_info[test_imp.curr_room_name][1]

vent_count = 0 

def draw(imgs, xcor, ycor): 
    for img in imgs: 
        window.blit(img, (xcor, ycor))

    window.blit(caf_vent_img, (565, 379))
    test_imp.draw()
    caf_vent.draw()

running = True 
while running: 
    keys = pygame.key.get_pressed()
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 
        elif event.type == pygame.MOUSEBUTTONDOWN: 
            pos = pygame.mouse.get_pos()
            print(pos)

    window.fill((0, 0, 0))
    test_imp.monster_move(keys)
    draw(curr_room_img, 0, 0)

    if caf_vent.open_vent_check(test_imp): 
        caf_vent.vent_animation()
        test_imp.vent_animation()
    else: 
        # resetting everything so animation can play repeatedly 
        caf_vent.animation_complete = False
        test_imp.venting_animation_complete = False 
        test_imp.venting_current_animation_frame = 0 
        test_imp.venting_animation_frame_count = 0
        caf_vent.current_animation_frame = 0 
        caf_vent.animation_frame_count = 0 

    pygame.display.update() 
    clock.tick(60)