import pygame 

class Vent: 
    def __init__(self, x, y, width, height, window, sprite_sheet): 
        self.x = x 
        self.y = y  
        self.width = width 
        self.height = height 
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.window = window 
        self.last_update = pygame.time.get_ticks() 
        self.sprite_sheet = sprite_sheet
        self.sprite_sheet = [self.sprite_sheet[i] for i in range(len(self.sprite_sheet) - 1)]
        self.vent_img = self.sprite_sheet[0] 
        self.animation_complete = False 
        self.animation_playing = False
        self.current_animation_frame = 0 
        self.animation_frame_count = 0
        self.room_name = ""

    # checking whether sprite can actually vent before animation plays 
    def open_vent_check(self, sprite): 
        if sprite.can_vent and self.rect.colliderect(sprite.rect):
            return True
        else: 
            return False
        
    def vent_animation(self): 
        if self.animation_complete: 
            return 

        if not self.animation_complete: 
            self.animation_playing = True 

            now = pygame.time.get_ticks() 
            if now - self.last_update > 100: 
                self.last_update = now 
                self.current_animation_frame = (self.current_animation_frame + 1) % len(self.sprite_sheet)
                self.animation_frame_count += 1 

                self.vent_img = self.sprite_sheet[self.current_animation_frame]

        if self.animation_frame_count >= len(self.sprite_sheet): 
            self.animation_complete = True 
            self.animation_playing = False 
            self.vent_img = self.sprite_sheet[0]
        return 

    def draw(self): 
        self.window.blit(self.vent_img, (self.x, self.y))
        return 
