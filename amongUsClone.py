import pygame, math, os 

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

imp_transform_list = [impTransform1, impTransform2, impTransform3, impTransform4, impTransform5, impTransform6, impTransform7, impTransform8, impTransform9, impTransform10, impTransform11, impTransform12, impTransform13]
obstacles = [] 

centers = {"upper_right": (443, 180), 
           "emergency": (312, 332),
           "upper_left": (173, 182), 
           "bottom_right": (444, 474),
           "bottom_left": (175, 473)
           }

class Obstacle(): 
    def __init__(self, x, y, radius): 
        self.x = x 
        self.y = y
        self.radius = radius 
        self.center_x = self.x 
        self.center_y = self.y       

class CrewMate(): 
    def __init__(self, crew_img, x, y, width, height, walk_right, walk_left, speed=2, killed=False): 
        self.crew = crew_img 
        self.stationary_crew = crew_img # need this so animation cycle doesn't freeze mid sprite when no movement detected
        self.x = x 
        self.y = y 
        self.width = width 
        self.height = height 
        self.speed = speed
        self.killed = killed 
        self.crew_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        # crewmate collision properties 
        self.radius = self.width / 2 
        self.center_x = self.x + self.width / 2 
        self.center_y = self.y + self.height / 2 

        # attributes for walking animation
        self.walk_right = walk_right 
        self.walk_left = walk_left
        
        self.walk_up = self.walk_right
        self.walk_down = self.walk_left 
        
        self.current_frame = 0 
        self.animation_speed = 0.2 

        # timer that keeps track of when pygame started up (in miliseconds)
        self.last_update = pygame.time.get_ticks() 

        # direction tracking
        self.direction = None 
        self.is_moving = False 

    def update_animation(self): 
        now = pygame.time.get_ticks()

        if self.is_moving: 
            if now - self.last_update > 100: # 100 ms = 10 frames per second  
                self.last_update = now 
                self.current_frame = (self.current_frame + 1) % len(self.walk_right) 
        
        """ self.current_frame + 1 moves to next frame in sequence % len(self.walk_right) ensures we loop back to 
        0 when we reach the end of the list no index range errors"""

        # set current image based on direction
        if self.direction == "right": 
            self.crew = self.walk_right[self.current_frame]
        
        elif self.direction == "left": 
            self.crew = self.walk_left[self.current_frame]
        
        elif self.direction == "up": 
            self.crew = self.walk_right[self.current_frame]
        
        elif self.direction == "down": 
            self.crew = self.walk_left[self.current_frame] 
    
    # check for whether crewmate is colliding with other objects 
    def collision_check(self, obstacles):
        for object in obstacles: 
            # calculating distance between centers 
            distance = math.sqrt((self.center_x - object.center_x ) ** 2 + (self.center_y - object.center_y) ** 2) 

            # collision detected 
            if distance < (self.radius + object.radius): 
                return True 
        else: 
            return False      
    
    def crew_move(self, keys): 
        self.is_moving = False
        old_x = self.x  
        old_y = self.y 

        if keys[pygame.K_w]:
            # move upwards 
            self.y -= self.speed
            self.direction = "up"
            self.is_moving = True 
       
        if keys[pygame.K_a]: 
            # move to the left 
            self.x -= self.speed 
            self.direction = "left"
            self.is_moving = True 
        
        if keys[pygame.K_s]: 
            #move downwards 
            self.y += self.speed
            self.direction = "down"
            self.is_moving = True 
        
        if keys[pygame.K_d]:  
            #move to the right
            self.x += self.speed
            self.direction = "right"
            self.is_moving = True   

        # update animation
        if self.is_moving:
            self.update_animation()  

        else: 
            self.crew = self.stationary_crew 

        # update center after movement 
        self.center_x = self.x + self.width / 2 
        self.center_y = self.y + self.height / 2 

        # collision check after movement 
        if self.collision_check(obstacles): 
            self.x = old_x
            self.y = old_y 

            # update center after moving backwards 
            self.center_x = self.x + self.width / 2 
            self.center_y = self.y + self.height / 2    
        
    def crew_draw(self): 
        window.blit(self.crew, (self.x, self.y))

# walking right and left defaulted to None for now working on monster transform
class Impostor(): 
    def __init__(self, imp_img, x, y, width, height, monster_transform_list, walk_right=None, walk_left=None, speed=2): 
        self.imp = imp_img 
        self.x = x 
        self.y = y 
        self.width = width 
        self.height = height
        self.speed = speed 
        self.has_killed = False 
        self.monster_transform_list = monster_transform_list
        self.imp_rect = pygame.Rect(self.x, self.y, self.width, self.height) 

        # attributes for walking animation
        self.walk_right = walk_right 
        self.walk_left = walk_left
        self.walk_up = self.walk_right 
        self.walk_down = self.walk_left 

        self.current_frame = 0 
        self.last_update = pygame.time.get_ticks() 
        self.animation_playing = False 
        self.animation_complete = False 
        self.animation_frame_count = 0 

    def monster_animation(self): 
        if self.animation_complete: 
            return 

        if not self.animation_playing: 
            self.animation_playing = True 
        
        now = pygame.time.get_ticks() 
        
        if now - self.last_update > 100:  
                self.last_update = now 
                self.current_frame = (self.current_frame + 1) % len(self.monster_transform_list)
                self.animation_frame_count += 1 

        #checking if we've shown all frames 
        if self.animation_frame_count >= len(self.monster_transform_list): 
            self.animation_complete = True 
            self.animation_playing = False 
            self.current_frame = 0 
            self.imp = self.monster_transform_list[self.current_frame] 
        
        self.imp = self.monster_transform_list[self.current_frame]

    def monster_transform(self): 
        self.monster_animation()
    
    def imp_move(self, keys):
        if keys[pygame.K_UP]: 
            self.y -= 1 
        
        if keys[pygame.K_DOWN]: 
            self.y += 1 
        
        if keys[pygame.K_RIGHT]: 
            self.x += 1 

            
    def collision_check(self): 
        return False 
    
    #checks whether imp is close enough to crew to kill 
    def crew_proximity_check(self, crew: CrewMate): 
        prox_range_x = None 
        prox_range_y = None 
        
        if abs(self.x - crew.x) <= prox_range_x: 
            return True 
        elif abs(self.y - crew.y) <= prox_range_y: 
            return True 
        else: 
            return False 
    
    # if close to crewmate, kill mechanism otherwise do nothing 
    def kill(self): 
        if self.crew_proximity_check(): 
            return None 
        else: 
            return None 

    def draw(self): 
        window.blit(self.imp, (self.x, self.y)) 

table_radius = 50
    
yellow_crew = CrewMate(yellow_crew, 320, 380, SCREEN_WIDTH/17, SCREEN_WIDTH/17, crew_walking_right, crew_walking_left) 

monster_imp = Impostor(imp_transform_list[0], 350, 380, SCREEN_WIDTH/17, SCREEN_HEIGHT/17, imp_transform_list)

upper_right_table = Obstacle(centers.get("upper_right")[0], centers.get("upper_right")[1], table_radius)
emergency_table = Obstacle(centers.get("emergency")[0], centers.get("emergency")[1], table_radius) 
upper_left_table = Obstacle(centers.get("upper_left")[0], centers.get("upper_left")[1], table_radius)
bottom_right_table = Obstacle(centers.get("bottom_right")[0], centers.get("bottom_right")[1], table_radius) 
bottom_left_table = Obstacle(centers.get("bottom_left")[0], centers.get("bottom_left")[1], table_radius) 

tables = [upper_right_table, emergency_table, upper_left_table, bottom_right_table, bottom_left_table] 

for table in tables: 
    obstacles.append(table)
 
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
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                # Reset and start animation
                monster_imp.animation_complete = False
                monster_imp.animation_playing = True
                monster_imp.current_frame = 0
                monster_imp.animation_frame_count = 0

    # Update animation if it's playing
    if monster_imp.animation_playing:
        monster_imp.monster_transform()

    yellow_crew.crew_move(keys) 
    monster_imp.imp_move(keys)
    draw()
    pygame.display.update()
    clock.tick(60)