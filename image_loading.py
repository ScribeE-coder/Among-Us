import pygame 

# function makes file clean and easier to read 
def load_img(file_path, scale_width, scale_height): 
    img = pygame.image.load(file_path)
    img = pygame.transform.scale(img, ((scale_width, scale_height)))
    return img 

def load_sequence(name, count, width, height): 
    return [load_img(f"images/{name}{i}.png", width, height) for i in range(1, count + 1)] 

