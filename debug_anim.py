import pygame
from image_loading import load_sequence
from CrewMate import CrewMate

pygame.init()
window = pygame.display.set_mode((640, 640))
clock = pygame.time.Clock()

idle_crew = load_sequence("idle", 1, 640/15, 640/15)
crew_walking_right = load_sequence("crewWalk", 7, 640/15, 640/15)
crew_walking_left = [pygame.transform.flip(s, True, False) for s in crew_walking_right]
crewDeadListy = load_sequence("crewDead", 9, 640/15, 640/15)

crew = CrewMate(idle_crew[0], 320, 250, 640/15, 640/15, crew_walking_right, crew_walking_left, [], window, crewDeadListy)

# fake "d key held down" — keys object that returns True only for K_d
class FakeKeys:
    def __getitem__(self, k):
        return k == pygame.K_d

keys = FakeKeys()

seen_frames = set()
for tick in range(120):  # simulate 2 seconds at 60fps
    crew.move(keys)
    seen_frames.add(crew.current_frame)
    if tick % 20 == 0:
        print(f"tick {tick}: is_moving={crew.is_moving} direction={crew.direction} "
              f"current_frame={crew.current_frame} crew_is_walkframe={crew.crew in crew_walking_right}")
    pygame.time.wait(16)  # ~60fps so the 100ms timer actually elapses

print(f"\nframes cycled through: {sorted(seen_frames)}")
print("ANIMATION LOGIC WORKS" if len(seen_frames) > 3 else "ANIMATION STUCK")
pygame.quit()
