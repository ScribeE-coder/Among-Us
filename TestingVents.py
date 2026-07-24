import pygame 
from image_loading import load_sequence 
from CrewMate import CrewMate 
from Obstacle import Obstacle, Rectangle_Obstacle, Circular_Obstacle, Sprite_Obstacle 
from Impostor import Monster 

pygame.init() 

SCREEN_WIDTH = 640 
SCREEN_HEIGHT = 640 
divisor = 15

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

cafeteria_imgs = load_sequence('amongUs_cafeteria', 1, SCREEN_WIDTH, SCREEN_HEIGHT)
cafeteriaUpperEMedbayHallway1 = load_sequence("cafeteriaUpperEMedbayHallway", 1, SCREEN_WIDTH, SCREEN_HEIGHT)

test_imp_img = load_sequence('idle', 1, SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
test_imp_walking_right_imgs = load_sequence('crewWalk', 7, SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
test_imp_walking_left_imgs = [pygame.transform.flip(sprite, True, False) for sprite in test_imp_walking_right_imgs] 
test_imp_transform_imgs = load_sequence("impTransform", 13, SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)

# loading in vent sprite sheet 
vent_animation:list = load_sequence('amongUsVent', 1, SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)

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

rooms = {
    "cafeteria": [cafeteria_imgs, tables, {"caf_upperE_medbay_hallway": [doorToMedBayHallway, (550, 310)]}], 
    
    "caf_upperE_medbay_hallway": [cafeteriaUpperEMedbayHallway1, None, {"cafeteria": [HallwayBackToCaf, (23, 310)]}]
         } 

test_imp = Monster(test_imp_img[0], 320, 250, SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor, test_imp_transform_imgs, window, test_imp_walking_right_imgs, test_imp_walking_left_imgs)

def draw(imgs, xcor, ycor): 
    for img in imgs: 
        window.blit(img, xcor, ycor)

    test_imp.draw()

curr_room_img = cafeteria_imgs[0]
curr_room_name = "cafeteria"


running = True 
while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 

    window.fill((0, 0, 0))
    pygame.display.update() 
    clock.tick(60)