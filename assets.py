import pygame 
from image_loading import load_sequence
from CrewMate import CrewMate 
from Impostor import Monster
from Obstacle import Circular_Obstacle, Rectangle_Obstacle
from Vent import Vent 

pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640 
SPRITE_DIVISOR = 15 
VENT_SPRITE_SHEET_DIVISOR = 16.2
SCREEN_WIDTH_DIVISOR = 17 
SCREEN_HEIGHT_DIVISOR = 17 

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Among Us Clone")

"""Instead of loading in sprites this way, it would probably be better to have a global dictionary, and then add parameters to the funciton
that can just be passed into the function itself; flipping can be split into a separate function, vent animation sheet can be its own thing"""
def load_sprites(): 
    cafeteria = load_sequence("amongUs_cafeteria", 1, SCREEN_WIDTH, SCREEN_HEIGHT) 
    idle_crew = load_sequence("idle", 1, SCREEN_WIDTH/SPRITE_DIVISOR, SCREEN_HEIGHT/SPRITE_DIVISOR)

    crew_walking_right_sheet = load_sequence("crewWalk", 7, SCREEN_WIDTH/SPRITE_DIVISOR, SCREEN_HEIGHT/SPRITE_DIVISOR) 
    crew_walking_left_sheet = [pygame.transform.flip(sprite, True, False) for sprite in crew_walking_right_sheet]

    monster_transform_list = load_sequence("impTransform", 13, SCREEN_WIDTH/SPRITE_DIVISOR, SCREEN_HEIGHT/SPRITE_DIVISOR)

    monster_walking_right_sheet = load_sequence("monsterWalk", 7, SCREEN_WIDTH/SPRITE_DIVISOR, SCREEN_HEIGHT/SPRITE_DIVISOR)
    monster_walking_left_sheet = [pygame.transform.flip(sprite, True, False) for sprite in monster_walking_right_sheet]

    monster_attack_sheet = load_sequence("monsterAttack", 12, SCREEN_WIDTH/SPRITE_DIVISOR, SCREEN_HEIGHT/SPRITE_DIVISOR)

    crew_dead_listy = load_sequence("crewDead", 9, SCREEN_WIDTH/SPRITE_DIVISOR, SCREEN_HEIGHT/SPRITE_DIVISOR)

    ghost_move_right_sheet = load_sequence("ghost", 16, SCREEN_WIDTH/SPRITE_DIVISOR, SCREEN_HEIGHT/SPRITE_DIVISOR) 
    ghost_move_left_sheet = [pygame.transform.flip(sprite, True, False) for sprite in ghost_move_right_sheet]

    stat_ghost_sheet = load_sequence("stationary_ghost", 1, SCREEN_WIDTH/SPRITE_DIVISOR, SCREEN_HEIGHT/SPRITE_DIVISOR)

    caf_upper_eng_Hallway1 = load_sequence("cafeteriaUpperEMedbayHallway", 1, SCREEN_WIDTH, SCREEN_HEIGHT)
    
    vent_animation_sheet = pygame.image.load("images/amongUsVent1.png")

    imp_venting_image_sheet = load_sequence('Venting', 7, SCREEN_WIDTH/SPRITE_DIVISOR, SCREEN_HEIGHT/SPRITE_DIVISOR)

    return {
        "cafeteria": cafeteria, 
        "idle_crew": idle_crew, 
        "crew_walking_right_sheet": crew_walking_right_sheet, 
        "crew_walking_left_sheet": crew_walking_left_sheet, 
        "monster_transform_list": monster_transform_list, 
        "monster_walking_right_sheet": monster_walking_right_sheet, 
        "monster_walking_left_sheet": monster_walking_left_sheet, 
        "monster_attack_sheet": monster_attack_sheet, 
        "crew_dead_listy": crew_dead_listy, 
        "ghost_move_right_sheet": ghost_move_right_sheet, 
        "ghost_move_left_sheet": ghost_move_left_sheet, 
        "stat_ghost_sheet": stat_ghost_sheet, 
        "caf_upper_eng_Hallway1": caf_upper_eng_Hallway1, 
        "vent_animation_sheet": vent_animation_sheet, 
        "imp_venting_image_sheet": imp_venting_image_sheet
    }

sprite_imgs = load_sprites()

def create_obstacles():
    table_radius = 50
    centers = {
        "upper_right": (443, 180),
        "emergency": (312, 332),
        "upper_left": (173, 182),
        "bottom_right": (444, 474),
        "bottom_left": (175, 473),
    }
    return {name: Circular_Obstacle(x, y, table_radius) for name, (x, y) in centers.items()}

obstacles = create_obstacles()

# CrewMate and Monster need a list for collision detection, easier to type cast into a list vs. restructuring both classes
caf_obstacles = list(obstacles.values())
caf_obstacles.append(Rectangle_Obstacle(128, 50, 340, 1))

def create_characters():
    yellow_crew = CrewMate(sprite_imgs["idle_crew"][0], 320, 250, SCREEN_WIDTH/SCREEN_WIDTH_DIVISOR, SCREEN_HEIGHT/SCREEN_HEIGHT_DIVISOR, sprite_imgs["crew_walking_right_sheet"], sprite_imgs["crew_walking_left_sheet"], caf_obstacles, window, sprite_imgs["crew_dead_listy"])
    yellow_crew.ghosty = sprite_imgs["stat_ghost_sheet"][0]

    monster_imp = Monster(350, 255, SCREEN_WIDTH/SCREEN_WIDTH_DIVISOR, SCREEN_HEIGHT/SCREEN_HEIGHT_DIVISOR, sprite_imgs["monster_transform_list"], window, sprite_imgs["monster_walking_right_sheet"], sprite_imgs["monster_walking_left_sheet"])
    monster_imp.monster_attack_list = sprite_imgs["monster_attack_sheet"]
    monster_imp.regular_imp_right = sprite_imgs["crew_walking_right_sheet"]
    monster_imp.regular_imp_left = sprite_imgs["crew_walking_left_sheet"]

    return {"yellow_crew": yellow_crew, "monster_imp": monster_imp}

characters = create_characters()

def create_vent_animation_frames():
    sheet = sprite_imgs["vent_animation_sheet"]
    frame_height = sheet.get_height()
    icon_bounds = [(11, 58), (70, 117), (129, 176), (187, 242), (252, 307), (318, 368), (380, 427)]  # where each vent sprite sits on the sheet
    frames = []
    for start, end in icon_bounds:
        frame = sheet.subsurface(pygame.Rect(start, 0, end - start, frame_height))
        frame = pygame.transform.scale(frame, (SCREEN_WIDTH / VENT_SPRITE_SHEET_DIVISOR, SCREEN_HEIGHT / VENT_SPRITE_SHEET_DIVISOR))
        frames.append(frame)
    return frames

caf_vent_animation_frames = create_vent_animation_frames()

def create_vents():
    caf_vent = Vent(565, 379, SCREEN_WIDTH / VENT_SPRITE_SHEET_DIVISOR, SCREEN_HEIGHT / VENT_SPRITE_SHEET_DIVISOR, window, caf_vent_animation_frames)
    caf_vent.room_name = "cafeteria"
    return {caf_vent.room_name: caf_vent}

vents = create_vents()