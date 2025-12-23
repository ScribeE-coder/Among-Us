import pygame

import CrewMate

# walking right and left defaulted to None for now working on monster transform
class Impostor(): 
    def __init__(self, imp_img, x, y, width, height, window, walk_right, walk_left, speed=2): 
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
        self.obstacles = None 
        
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
    
    # if close to crewmate, kill mechanism otherwise do nothing, will have countdown mechanism 
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
        self.speed = speed 
        self.window = window 
        
        self.monster_transform_list = monster_transform_list
        self.walk_right = walk_right 
        self.walk_left = walk_left 
        self.stationary_monster = self.monster_transform_list[-1]

        # attributes for monster animation
        self.current_animation_frame = 0 
        self.last_update = pygame.time.get_ticks() 
        self.animation_playing = False 
        self.animation_complete = False 
        self.animation_frame_count = 0

        self.direction = None 
        self.is_moving = False
        self.current_frame = 0 

        self.regular_imp_right = None 
        self.regular_imp_left = None 

        # attributes for attacking animation 
        self.monster_attack_list = None 
        self.attacking = False 
        self.has_attacked = False # having has_attacked attribute will be useful for countdown mechanics later 

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

    def update_animation(self): 
        now = pygame.time.get_ticks() 

        if self.is_moving: 
            if now - self.last_update > 100: # 100 ms = 10 frames per second  
                self.last_update = now 
                self.current_frame = (self.current_frame + 1) % len(self.walk_right) 

        # set current image based on direction
        if self.direction == "right":  
            self.monster = self.walk_right[self.current_frame] 
        
        elif self.direction == "left": 
            self.monster = self.walk_left[self.current_frame]
        
        elif self.direction == "up": 
            self.monster = self.walk_right[self.current_frame]
        
        elif self.direction == "down": 
            self.monster = self.walk_left[self.current_frame] 

    def monster_move(self, keys): 
        self.is_moving = False
        
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

        if self.is_moving: 
            self.update_animation()

        if not self.is_moving: 
            self.monster = self.stationary_monster

    def attack_animation(self): 
        now = pygame.time.get_ticks()
        self.monster_attack_frame_count = 0 

        if now - self.last_update > 100: 
            self.last_update = now 
            self.current_frame = (self.current_frame + 1 ) % len(self.monster_attack_list)
            self.monster_attack_frame_count += 1 

        self.monster = self.monster_attack_list[self.current_frame]

        if self.monster_attack_frame_count >= len(self.monster_attack_list): 
            self.has_attacked = True 
            self.attacking = False 

    def attack(self, keys):
        if not self.attacking: 
            self.attacking = True   
            self.attack_animation()
        else: 
            return  

    def draw(self): 
        self.window.blit(self.monster, (self.x, self.y))

    
