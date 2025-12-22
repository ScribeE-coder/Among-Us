import pygame

import CrewMate

# walking right and left defaulted to None for now working on monster transform
class Impostor(): 
    def __init__(self, imp_img, x, y, width, height, monster_transform_list, window, walk_right=None, walk_left=None, speed=2): 
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

        self.window = window 

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
        self.window.blit(self.imp, (self.x, self.y)) 
