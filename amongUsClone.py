import pygame, math, os 

SCREEN_WIDTH = 640 
SCREEN_HEIGHT = 640 

pygame.init()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Among Us")
clock = pygame.time.Clock()

cafeteria = pygame.image.load(r"C:\Users\kidmu\Among-US\images\amongUs_caf.PNG") 
cafeteria = pygame.transform.scale(cafeteria, (SCREEN_WIDTH, SCREEN_HEIGHT))

yellow_crew = pygame.image.load(r"C:\Users\kidmu\Among-US\images\amongUs_yellowCrew.jpeg")
yellow_crew = pygame.transform.scale(yellow_crew, (SCREEN_WIDTH/15, SCREEN_HEIGHT/15))

crew_walk1 = pygame.image.load(r"\Users\kidmu\Among-Us\images\crewWalk1.png") 
crew_walk2 = pygame.image.load(r"\Users\kidmu\Among-Us\images\crewWalk2.png")
crew_walk3 = pygame.image.load(r"\Users\kidmu\Among-Us\images\crewWalk3.png") 
crew_walk4 = pygame.image.load(r"\Users\kidmu\Among-Us\images\crewWalk4.png") 
crew_walk5 = pygame.image.load(r"\Users\kidmu\Among-Us\images\crewWalk5.png") 
crew_walk6 = pygame.image.load(r"\Users\kidmu\Among-Us\images\crewWalk6.png") 
crew_walk7 = pygame.image.load(r"\Users\kidmu\Among-Us\images\crewWalk7.png")

walking_right = [crew_walk1, crew_walk2, crew_walk3, crew_walk4, crew_walk5, crew_walk6, crew_walk7] 
walking_left = [pygame.transform.flip(sprite, True, False) for sprite in walking_right]

# walking up and down mechanics only needed for other maps not current one 
walk_up = None 
walk_down = None

impostor = None 

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

""" the next step is to work on crewmate movement animation"""
class CrewMate(): 
    def __init__(self, crew_img, x, y, width, height, speed=2, killed=False): 
        self.crew = crew_img 
        self.x = x 
        self.y = y 
        self.width = width 
        self.height = height 
        self.speed = speed
        self.killed = killed 
        self.crew_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        #crewmate collision properties 
        self.radius = self.width / 2 
        self.center_x = self.x + self.width / 2 
        self.center_y = self.y + self.height / 2 

        #attributes for walking animation
        self.walk_right = None 
        self.walk_left = None 
        self.walk_up = None 
        self.walk_down = None 
        self.current_frame = 0 
        self.animation_speed = 0.2 

        # timer that keeps track of when pygame started up (in miliseconds)
        self.last_update = pygame.time.get_ticks() 

        # direction tracking
        self.direction = "right"
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
            return None 
        elif self.direction == "down": 
            return None 

    
    # check for whether crewmate is colliding with other objects 
    def collision_table_check(self, obstacles):
        for object in obstacles: 
            # calculating distance between centers 
            distance = math.sqrt((self.center_x - object.center_x ) ** 2 + (self.center_y - object.center_y) ** 2) 

            # collision detected 
            if distance < (self.radius + object.radius): 
                return True      
    
    def crew_move(self, keys): 
        old_x = self.x  
        old_y = self.y 

        if keys[pygame.K_w]:
            # move upwards 
            self.y -= self.speed
       
        if keys[pygame.K_a]: 
            # move to the left 
            self.x -= self.speed 
        
        if keys[pygame.K_s]: 
            #move downwards 
            self.y += self.speed
        
        if keys[pygame.K_d]:  
            #move to the right
            self.x += self.speed

        # update center after movement 
        self.center_x = self.x + self.width / 2 
        self.center_y = self.y + self.height / 2 

        # collision check after movement 
        if self.collision_table_check(obstacles): 
            self.x = old_x
            self.y = old_y 

            # update center after moving backwards 
            self.center_x = self.x + self.width / 2 
            self.center_y = self.y + self.height / 2
        
    def crew_draw(self): 
        window.blit(self.crew, (self.x, self.y))

# will work on later 
class Impostor(): 
    def __init__(self, imp_img, x, y, width, height, speed=2): 
        self.imp_img = imp_img 
        self.x = x 
        self.y = y 
        self.width = width 
        self.height = height

    def imp_move(self): 
        return None 
    
    #checks whether imp is close enough to crew to kill 
    def crew_proximity_check(self): 
        return False 
    
    # if close to crewmate, kill mechanism otherwise do nothing 
    def kill(self): 
        if self.crew_proximity_check(): 
            return None 
        else: 
            return None  

table_radius = 50
    
yellow_crew = CrewMate(yellow_crew, 320, 380, SCREEN_WIDTH/17, SCREEN_WIDTH/17) 

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

running = True 

while running: 
    # keys = list of all possible keys that can be pressed on the keyboard 
    keys = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False

    yellow_crew.crew_move(keys) 
    draw()
    pygame.display.update()
    clock.tick(60) 