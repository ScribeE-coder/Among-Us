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

doorToMedBayHallway = Rectangle_Obstacle(-20, 295, 35, 50)
doorToStorageHallway = Rectangle_Obstacle(290, 625, 65, 30)
doortoAsteroidsHallway = Rectangle_Obstacle(629, 285, 65, 60)
HallwayBackToCaf = Rectangle_Obstacle(626, 301, 65, 30)

""" rooms dictionary includes the name of the room, a list containing the image for that room, any obstacles there, and a dictionary containing the names of connecting hallways, 
the rectangle corresponding to the door, and the coordinates for where sprite should be once it walks through"""
rooms = {
    "cafeteria": [cafeteria, tables, {"caf_upperE_medbay_hallway": [doorToMedBayHallway, (550, 310)]}], 
    
    "caf_upperE_medbay_hallway": [cafeteriaUpperEMedbayHallway1, None, {"cafeteria": [HallwayBackToCaf, (23, 310)]}]
         } 

""" in order to switch rooms need to create a rectangle object associated with the coordinates for each hallway; once you have that rectangle object, you then need to check 
for whether the player is colliding with that rectangle; if so, switch rooms"""

test_crew = CrewMate(idle_crew[0], 320, 250, SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor, crew_walking_right, crew_walking_left, obstacles, window, crewDeadListy)

def draw(imgs, xcor, ycor): 
    for img in imgs: 
        window.blit(img, (xcor, ycor))
    test_crew.draw()

curr_room_img = rooms["cafeteria"][0] #always starts off in the cafeteria [cafeteria, tables, dictionary]
curr_room_name = "cafeteria"
    
running = True 
while running: 
    keys = pygame.key.get_pressed()
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 
        elif event.type == pygame.MOUSEBUTTONDOWN: 
            pos = pygame.mouse.get_pos()
            print(pos)
    
    window.fill((0, 0, 0)) # fill the entire screen with black before drawing any rooms to prevent images bleeding through each other 
    
    draw(curr_room_img, 0, 0)
    test_crew.move(keys)
    curr_hallways_available = rooms[curr_room_name][2]
    
    for name, hallway_listy in curr_hallways_available.items(): 
        door = hallway_listy[0] # this should work as long as the first item of the list is always your rectangle object for collision detection 
        if test_crew.rect.colliderect(door.rect):
            curr_room_name = name  
            curr_room_img = rooms[curr_room_name][0] 

            test_crew.x = curr_hallways_available[curr_room_name][1][0]
            test_crew.y = curr_hallways_available[curr_room_name][1][1]
    
    """ need to see where rectangles are for collision purposes"""
    #pygame.draw.rect(window, (255,0, 0), doorToMedBayHallway.rect, 1)
    #pygame.draw.rect(window, (255, 0, 0), doorToStorageHallway.rect, 1)
    #pygame.draw.rect(window, (255, 0, 0), doortoAsteroidsHallway.rect, 1)
    pygame.draw.rect(window, (255, 0, 0), HallwayBackToCaf.rect, 1)
    
    pygame.display.update() 
    clock.tick(60) 