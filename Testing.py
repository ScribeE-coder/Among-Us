import pygame
from image_loading import load_sequence 
from CrewMate import CrewMate 
from Obstacle import Obstacle, Rectangle_Obstacle, Circular_Obstacle, Sprite_Obstacle

""" This is just a file to test different functions."""
pygame.init() 

SCREEN_WIDTH = 640 
SCREEN_HEIGHT = 640 
divisor = 15 

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
clock = pygame.time.Clock() 

"""Testing new load_sequence function so main file isn't so fucking long omfg I'm so fucked"""
cafeteria = load_sequence("amongUs_cafeteria", 1, SCREEN_WIDTH, SCREEN_HEIGHT) 
cafeteriaUpperEMedbayHallway1 = load_sequence("cafeteriaUpperEMedbayHallway", 1, SCREEN_WIDTH, SCREEN_HEIGHT)

yellow_crew = load_sequence("idle", 1, SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor) 
idle_crew = load_sequence("idle", 1, SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)

crew_walking_right = load_sequence("crewWalk", 7, SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor) 
crew_walking_left = [pygame.transform.flip(sprite, True, False) for sprite in crew_walking_right]
crewDeadListy = load_sequence("crewDead", 9, SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)

obstacles = []
centers = {"upper_right": (443, 180), 
           "emergency": (312, 332),
           "upper_left": (173, 182), 
           "bottom_right": (444, 474),
           "bottom_left": (175, 473)
           }  

table_radius = 50

upper_right_table = Circular_Obstacle(centers.get("upper_right")[0], centers.get("upper_right")[1], table_radius) # type: ignore
emergency_table = Circular_Obstacle(centers.get("emergency")[0], centers.get("emergency")[1], table_radius)  # type: ignore
upper_left_table = Circular_Obstacle(centers.get("upper_left")[0], centers.get("upper_left")[1], table_radius) # type: ignore
bottom_right_table = Circular_Obstacle(centers.get("bottom_right")[0], centers.get("bottom_right")[1], table_radius)  # type: ignore
bottom_left_table = Circular_Obstacle(centers.get("bottom_left")[0], centers.get("bottom_left")[1], table_radius)  # type: ignore

tables = [upper_right_table, emergency_table, upper_left_table, bottom_right_table, bottom_left_table]  
rooms = {
    "cafeteria": [cafeteria, tables, {"doorToMedBayHallway": (9, 309), 
                                      "doorToStorageHallway": (321, 625), 
                                      "doortoAsteroidsHallway": (629, 313)}], 
    "caf_upperE_medbay_hallway": [cafeteriaUpperEMedbayHallway1, None, {"doorToMedBay": (424, 414)}]
         } 

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
        elif event.type == pygame.MOUSEBUTTONDOWN: 
            pos = pygame.mouse.get_pos()
            print(pos)

    test_crew.move(keys)
    if test_crew.x < rooms["caf_upperE_medbay_hallway"][2]["doorToMedBay"][0] and test_crew.y < rooms["caf_upperE_medbay_hallway"][2]["doorToMedBay"][1]: 
        draw(cafeteriaUpperEMedbayHallway1, 0, 0)
    else: 
         draw(cafeteria, 0, 0)
    
    pygame.display.update() 
    clock.tick(60) 