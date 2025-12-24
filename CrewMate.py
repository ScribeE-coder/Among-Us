import pygame, math, Sprite

from Sprite import Sprite

class CrewMate(Sprite): 
    def __init__(self, crew_img, x, y, width, height, walk_right, walk_left, obstacles, window, speed=2, killed=False): 
        super().__init__(x, y, width, height, walk_right, walk_left, window)
        self.crew = crew_img 
        self.stationary_crew = crew_img # need this so animation cycle doesn't freeze mid sprite when no movement detected
        self.x = x 
        self.y = y 
        self.width = width 
        self.height = height 
        self.speed = speed
        self.killed = killed 
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

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
        
        # TODO:not currently being used 
        self.animation_speed = 0.2 

        # timer that keeps track of when pygame started up (in miliseconds)
        self.last_update = pygame.time.get_ticks() 

        # direction tracking
        self.direction = None 
        self.is_moving = False 

        self.obstacles = obstacles 
        self.window = window

        self.tasks = [] 
        self.has_tasks = True 

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
    
    # TODO: check for whether crewmate is colliding with other objects 
    def collision_check(self, obstacles):
        for obstacle in obstacles: 
            colliding = obstacle.check_collision(self)  
            # if im colliding with an object then you don't need to check for the other objects 
            if colliding: 
                return True 
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

        # updating rectangle with new coordinates after movement 
        self.rect.x = self.x 
        self.rect.y = self.y

        # update center after movement 
        self.center_x = self.x + self.width / 2 
        self.center_y = self.y + self.height / 2 

        # collision check after movement 
        collision = self.collision_check(self.obstacles)

        # if collision is found, move backwards 
        if collision: 
            self.x = old_x
            self.y = old_y 

            # update center after moving backwards 
            self.center_x = self.x + self.width / 2 
            self.center_y = self.y + self.height / 2

            # update rectangle after moving backwards 
            self.rect.x = self.x 
            self.rect.y = self.y 

        # update animation
        if self.is_moving:
            self.update_animation()  

        else: 
            self.crew = self.stationary_crew  

    # TODO: displaying current tasks on screen
    def display_tasks(): 
        return None

    # TODO: as player completes tasks, they should be removed from task list 
    def update_tasks(): 
        return None 
        
    def crew_draw(self): 
        self.window.blit(self.crew, (self.x, self.y))