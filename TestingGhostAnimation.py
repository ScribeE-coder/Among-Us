import pygame 
from image_loading import load_sequence 
from CrewMate import CrewMate 
from Ghost import Ghost 
from Impostor import Monster, Impostor 

pygame.init() 

SCREEN_WIDTH = 640 
SCREEN_HEIGHT = 640 
divisor = 15

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock() 

# loading in images for testing 
cafeteria = load_sequence("amongUs_cafeteria", 1, SCREEN_WIDTH, SCREEN_HEIGHT) 

test_crew_idle = load_sequence("idle", 1, SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
test_crew_dead_imgs = load_sequence("crewDead", 9, SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
test_ghost_move_right = load_sequence("ghost", 48, SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
test_ghost_move_left = [pygame.transform.flip(sprite, True, False) for sprite in test_ghost_move_right]
test_crew_walk_right_imgs = load_sequence("crewWalk", 7, SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
test_crew_walk_left_imgs = [pygame.transform.flip(sprite, True, False) for sprite in test_crew_walk_right_imgs]

test_imp_idle = load_sequence("idle", 1, SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
test_imp_walk_imgs = load_sequence("crewWalk", 7, SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
test_imp_transform_imgs = load_sequence("impTransform", 13, SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
test_monster_walk_right_imgs = load_sequence("monsterWalk", 7, SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor)
test_monster_walk_left_imgs = [pygame.transform.flip(sprite, True, False) for sprite in test_monster_walk_right_imgs]
test_monster_attack_imgs = load_sequence("monsterAttack", 12, SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor) 

# setting up sprites for testing 
test_crew = CrewMate(test_crew_idle[0], 320, 250, SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor, test_crew_walk_right_imgs, test_crew_walk_left_imgs, None, window, test_crew_dead_imgs)
test_imp = Monster(test_imp_idle[0], 330, 260, SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor, test_imp_transform_imgs, window, test_monster_walk_right_imgs, test_monster_walk_left_imgs)
test_ghost = Ghost(test_ghost_move_right[0], 320, 250, SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor, test_ghost_move_right, test_ghost_move_left, 'crew', [], window)
test_imp.monster_attack_list = test_monster_attack_imgs 
test_imp.regular_imp_left = test_crew_walk_left_imgs
test_imp.regular_imp_right = test_crew_walk_right_imgs 

def draw(): 
    window.blit(cafeteria[0], (0, 0))
    test_crew.draw()
    test_imp.draw()

running = True 
while running: 
    keys = pygame.key.get_pressed()
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_t: # t key triggers monster transformation 
                test_imp.animation_complete = False 
                test_imp.animation_playing = True 
                test_imp.current_animation_frame = 0 
                test_imp.animation_frame_count = 0

            elif event.key == pygame.K_0: 
               if test_imp.animation_complete: 
                    test_imp.monster_attack_frame_count = 0 
                    test_imp.attacking = True 
                    test_imp.attack_complete = False 
                    test_imp.current_attack_frame = 0 

    if test_imp.attacking: 
        test_imp.attack(test_crew)

    if test_imp.animation_playing: 
        test_imp.monster_transform() 

    elif not test_imp.animation_playing and not test_imp.attacking: 
        test_imp.monster_move(keys) 

    if test_imp.kill_landed: 
        test_crew.killed_animation_playing = True 
        test_imp.kill_landed = False 

    if test_crew.killed_animation_playing and isinstance(test_crew, CrewMate): 
        test_crew.killed_animation()

    if test_crew.killed_animation_complete: 
        test_ghost = Ghost(test_ghost_move_right[0], test_crew.x, test_crew.y, SCREEN_WIDTH/divisor, SCREEN_HEIGHT/divisor, test_ghost_move_right, test_ghost_move_left, 'crew', [], window)
        test_crew = test_ghost 

    window.fill((0, 0, 0)) 
    draw()
    test_crew.move(keys)
    test_imp.monster_move(keys)

    pygame.display.update()
    clock.tick(60)