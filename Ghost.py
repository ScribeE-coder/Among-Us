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

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height) 
        self.ghost_time = pygame.time.get_ticks() 

        self.ghost_animation_listy = []
        self.current_frame = 0
        self.last_update = pygame.time.get_ticks()

        # guards against crewmate animation checks running after transition
        self.killed_animation_playing = False
        self.killed_animation_complete = False
    

    # will update this later when crew tasks are fully implemented 
    def tasks_empty(self): 
        if not self.tasks: 
            return 0 

    def move(self, keys): 
        if keys[pygame.K_w]: 
            self.y -= 1 
        
        if keys[pygame.K_a]: 
            self.x -= 1 
        
        if keys[pygame.K_s]: 
            self.y += 1 
        
        if keys[pygame.K_d]: 
            self.x += 1 

    def ghost_animation(self): 
        now = pygame.time.get_ticks() 
        if now - self.ghost_time > 100: 
            self.ghost_time = now 
            self.current_animation_frame = (self.current_animation_frame + 1) % len(self.ghost_animation_listy) 
            self.animation_frame_count += 1 

    # if ghost still has tasks those tasks should still be displayed 
    def still_tasks(self): 
        if self.has_tasks: 
            return True 
        else: 
            return False

    # TODO: function will display crew's current tasks in window 
    def display_tasks(self): 
        raise NotImplementedError
        
    def draw(self): 
        self.window.blit(self.img, (self.x, self.y))