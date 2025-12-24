import pygame, CrewMate, Sprite

from Sprite import Sprite

# walking right and left defaulted to None for now working on monster transform
class Impostor(Sprite): 
    def __init__(self, imp_img, x, y, width, height, window, walk_right, walk_left, speed=2): 
        super().__init__(imp_img, x, y, width, height, walk_right, walk_left, window)
        self.imp = imp_img 
        self.x = x 
        self.y = y 
        self.width = width 
        self.height = height
        self.speed = speed 
        self.has_killed = False 
        self.imp_rect = pygame.Rect(self.x, self.y, self.width, self.height) 

        # attributes for walking animation
        self.walk_right = walk_right 
        self.walk_left = walk_left
        self.walk_up = self.walk_right 
        self.walk_down = self.walk_left 
        self.animation_speed = 0.2 
        self.direction = None 
        self.is_moving = False 

        # attributes for collision
        self.obstacles = [] 
        
        self.window = window 

    def imp_move_animation(self): 
       now = pygame.time.get_ticks() 

       if self.is_moving: 
           if now - self.last_update > 100: 
               self.last_update = now 
               self.current_frame = (self.current_frame + 1) % len(self.walk_right)
       
       if self.direction == 'right':
           self.imp = self.walk_right[self.current_frame] 

       if self.direction == 'left': 
           self.imp = self.walk_left[self.current_frame] 

       if self.direction == 'up': 
           self.imp = self.walk_right[self.current_frame]

       if self.direction == 'down': 
           self.imp = self.walk_left[self.current_frame] 
    
    def imp_move(self, keys):
        self.is_moving = False 
        
        if keys[pygame.K_UP]: 
            self.direction = 'up'
            self.y -= 1 
            self.is_moving = True 
        
        if keys[pygame.K_DOWN]: 
            self.direction = 'down'
            self.y += 1
            self.is_moving = True  
        
        if keys[pygame.K_RIGHT]: 
            self.direction = 'right'
            self.x += 1 
            self.is_moving = True 

        if keys[pygame.K_LEFT]: 
            self.direction = 'left'
            self.x -= 1 
            self.is_moving = True 

        if self.is_moving: 
            self.imp_move_animation()
    
    # TODO: will check if imp is colliding with object to stop phasing through objects     
    def collision_check(self): 
        return False 
    
    # TODO: checks whether imp is close enough to crew to kill 
    def crew_proximity_check(self, crew: CrewMate): 
        prox_range_x = None 
        prox_range_y = None 
        
        if abs(self.x - crew.x) <= prox_range_x: 
            return True 
        elif abs(self.y - crew.y) <= prox_range_y: 
            return True 
        else: 
            return False 
    
    # TODO: if close to crewmate, kill mechanism otherwise do nothing, will have countdown mechanism 
    def kill(self): 
        if self.crew_proximity_check(): 
            return None 
        else: 
            return None 

    def draw(self): 
        self.window.blit(self.imp, (self.x, self.y)) 

class Monster(): 
    def __init__(self, monster_img, x, y, width, height, monster_transform_list, window, walk_right, walk_left, speed=2): 
        self.monster = monster_img 
        self.x = x
        self.y = y 
        self.width = width 
        self.height = height
        self.center_x = self.x + self.width / 2
        self.center_y = self.y + self.height /2 
        self.speed = speed 
        self.window = window 
        
        self.monster_transform_list = monster_transform_list
        self.walk_right = walk_right 
        self.walk_left = walk_left 
        
        # when standing still and transformed
        self.stationary_monster = self.monster_transform_list[-1]

        # when standing still and haven't transformed 
        self.stationary_imp = self.monster_transform_list[0]

        # attributes for monster animation
        self.current_animation_frame = 0 
        self.last_update = pygame.time.get_ticks() 
        self.animation_playing = False 
        self.animation_complete = False 
        self.animation_frame_count = 0

        self.direction = None 
        self.is_moving = False
        self.current_frame = 0 

        # will need regular imp walking cycle when transformation hasn't been completed
        self.regular_imp_right = None 
        self.regular_imp_left = None 

        # attributes for attacking animation 
        self.monster_attack_list = []
        self.attacking = False 
        self.attack_complete = False # having has_attacked attribute will be useful for countdown mechanics later 
        self.current_attack_frame = 0 
        self.attack_frame_count = 0 

        # rectangle for collision purposes
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.obstacles = [] # list of obstacles needed for collision
        self.radius = self.width / 2 

    def create_monster_attack_direction(self): 
        if self.monster_attack_list: 
            self.monster_attack_right = self.monster_attack_list 
            self.monster_attack_left = [pygame.transform.flip(sprite, True, False) for sprite in self.monster_attack_right]

    """ Creates the animation cycle that plays when you transform into a monster"""
    def monster_animation(self): 
        if self.animation_complete: 
            return 

        if not self.animation_complete: 
            self.animation_playing = True 
    
        now = pygame.time.get_ticks() 
    
        if now - self.last_update > 100:   
            self.last_update = now 
            self.current_animation_frame = (self.current_animation_frame + 1) % len(self.monster_transform_list)
            self.animation_frame_count += 1 
        
            # set the image immediately after updating the frame
            self.monster = self.monster_transform_list[self.current_animation_frame]

        # Check if we've shown all frames 
        if self.animation_frame_count >= len(self.monster_transform_list): 
            self.animation_complete = True 
            self.animation_playing = False
            self.monster = self.monster_transform_list[-1]

    def monster_transform(self):
        self.monster_animation()

    """ Creates the walking cycle pre and post monster transformation"""
    def update_animation(self): 
        now = pygame.time.get_ticks() 

        if self.is_moving: 
            if now - self.last_update > 100: # 100 ms = 10 frames per second  
                self.last_update = now 
                
                if self.animation_complete: 
                    self.current_frame = (self.current_frame + 1) % len(self.walk_right) 
                
                elif not self.animation_complete:
                    self.current_frame = (self.current_frame + 1) % len(self.regular_imp_right)

        # set current image based on direction
        if self.direction == "right": 
            if self.animation_complete: 
                self.monster = self.walk_right[self.current_frame]
            else:
                self.monster = self.regular_imp_right[self.current_frame] 
        
        elif self.direction == "left": 
            if self.animation_complete:
                self.monster = self.walk_left[self.current_frame]
            else: 
                self.monster = self.regular_imp_left[self.current_frame]
        
        elif self.direction == "up":
            if self.animation_complete: 
                self.monster = self.walk_right[self.current_frame]
            else: 
                self.monster = self.regular_imp_right[self.current_frame]
        
        elif self.direction == "down": 
            if self.animation_complete:
                self.monster = self.walk_left[self.current_frame] 
            else: 
                self.monster = self.regular_imp_left[self.current_frame] 

    def monster_move(self, keys): 
        self.is_moving = False
        old_x = self.x 
        old_y = self.y
        
        if keys[pygame.K_UP]: 
            self.direction = 'up'
            self.y -= 1
            self.is_moving = True 

        if keys[pygame.K_DOWN]: 
            self.direction = 'down' 
            self.y += 1 
            self.is_moving = True 

        if keys[pygame.K_LEFT]: 
            self.direction = 'left'
            self.x -= 1 
            self.is_moving = True 

        if keys[pygame.K_RIGHT]:
            self.direction = 'right'
            self.x += 1 
            self.is_moving = True  

        self.rect.x = self.x
        self.rect.y = self.y 

        self.center_x = self.x + self.width / 2 
        self.center_y = self.y + self.height / 2 

        collision = self.collision_check(self.obstacles)

        # if collision, then need to update x, y coordinates then call animation on those coordinates 
        if collision: 
            self.x = old_x 
            self.y = old_y 
            
            self.center_x = self.x + self.width / 2 
            self.center_y = self.y + self.height / 2 
            self.rect.x = self.x 
            self.rect.y = self.y 

        if self.is_moving: 
            self.update_animation()

        if not self.is_moving and self.animation_complete: 
            self.monster = self.stationary_monster
        
        elif not self.is_moving and not self.animation_complete: 
            self.monster = self.stationary_imp      

    def attack_animation(self): 
        now = pygame.time.get_ticks() 

        if now - self.last_update > 100: 
            self.last_update = now
            
            if self.direction == 'right': 
                self.current_attack_frame = (self.current_attack_frame + 1) % len(self.monster_attack_right) 
            if self.direction == 'left': 
                self.current_attack_frame = (self.current_attack_frame + 1) % len(self.monster_attack_left)
            if self.direction == 'up': 
                self.current_attack_frame = (self.current_attack_frame + 1) % len(self.monster_attack_right)
            if self.direction == 'down': 
                self.current_attack_frame = (self.current_attack_frame + 1) % len(self.monster_attack_left)
            
            self.monster_attack_frame_count += 1 

        self.monster = self.monster_attack_list[self.current_attack_frame]

        if self.monster_attack_frame_count >= len(self.monster_attack_list): 
            self.attack_complete = True 
            self.attacking = False
            self.monster = self.stationary_monster

    def attack(self): 
            if len(self.monster_attack_list) != 0: 
                self.create_monster_attack_direction() 
            self.attack_animation() 

    def collision_check(self, obstacles): 
        for obstacle in obstacles: 
            colliding = obstacle.check_collision(self)
            if colliding: 
                return True 
        else: 
            return False 

    def draw(self): 
        self.window.blit(self.monster, (self.x, self.y))