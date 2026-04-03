import pygame as pg 
from CrewMate import CrewMate

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640 
divisor = 15 

pg.init() 

window = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pg.time.Clock()

def load_img(file_path, scale_width, scale_height): 
    img = pg.image.load(file_path)
    img = pg.transform.scale(img, ((scale_width, scale_height)))
    return img 

cafeteria = load_img("images/amongUS_caf.PNG", SCREEN_WIDTH, SCREEN_HEIGHT) 
idle_crew = load_img("images/idle.png", SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor) 

crew_walk1 = load_img("images/crewWalk1.png", SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
crew_walk2 = load_img("images/crewWalk2.png", SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
crew_walk3 = load_img("images/crewWalk3.png", SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
crew_walk4 = load_img("images/crewWalk4.png", SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
crew_walk5 = load_img("images/crewWalk5.png", SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
crew_walk6 = load_img("images/crewWalk6.png", SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
crew_walk7 = load_img("images/crewWalk7.png", SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)

crew_walking_right = [crew_walk1, crew_walk2, crew_walk3, crew_walk4, crew_walk5, crew_walk6, crew_walk7] 
crew_walking_left = [pg.transform.flip(sprite, True, False) for sprite in crew_walking_right]

yellow_crew = CrewMate(idle_crew, 320, 250, SCREEN_WIDTH/17, SCREEN_HEIGHT/17, crew_walking_right, crew_walking_left, obstacles, window, crewDead_listy) 



if yellow_crew.kill_distance_check(monster_imp) and monster_imp.kill_cooldown_check() and monster_imp.attack_complete and not monster_imp.kill_registered:
    yellow_crew.been_killed(monster_imp) 

