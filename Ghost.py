import pygame, Sprite, CrewMate

from Sprite import Sprite 

""" Ghost class will need to be general enough to apply to both crew and imps"""

class Ghost(Sprite): 
    def __init__(self, img, x, y, width, height, walk_right, walk_left, ghost_type, tasks, window): 
        self.ghost_type = ghost_type # ghosts can either be crew or impostors 
        self.img = img 
        self.x = x 
        self.y = y
        self.width = width 
        self.height = height  
        self.tasks = tasks 
        self.walk_right = walk_right 
        self.walk_left = walk_left
        self.walk_up = self.walk_right 
        self.walk_down = self.walk_left
        self.ghost_type = ghost_type 
        self.tasks = tasks 
        self.window = window 
        self.speed = 0.5 

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height) 
        self.ghost_time = pygame.time.get_ticks() 

        self.ghost_animation_listy = []
        self.current_frame = 0
        self.last_update = pygame.time.get_ticks()

        # guards against crewmate animation checks running after transition
        self.killed_animation_playing = False
        self.killed_animation_complete = False

        self.is_moving = False 
    
    def tasks_empty(self): 
        if not self.tasks: 
            return True 
        else: 
            return False 

    #TODO: function will need to cross out tasks that have already been completed and remove from task list 
    def update_tasks(self, task_complete): 
        return None    
    
    def move(self, keys): 
        old_x = self.x 
        old_y = self.y 
        
        if keys[pygame.K_w]: 
            self.y -= self.speed
        
        if keys[pygame.K_a]: 
            self.x -= self.speed 
        
        if keys[pygame.K_s]: 
            self.y += self.speed 
        
        if keys[pygame.K_d]: 
            self.x += self.speed 
    
    def ghost_animation(self): 
        now = pygame.time.get_ticks() 
        if now - self.ghost_time > 100: 
            self.ghost_time = now 
            self.current_animation_frame = (self.current_animation_frame + 1) % len(self.ghost_animation_listy) 
            self.animation_frame_count += 1 

    # TODO: function will display crew's current tasks in window 
    def display_tasks(self): 
        raise NotImplementedError
        
    def draw(self): 
        self.window.blit(self.img, (self.x, self.y))