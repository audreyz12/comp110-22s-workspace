import pygame
from pygame import mixer

pygame.init()
screen = pygame.display.set_mode((900, 600))
clock = pygame.time.Clock()

# Starting the mixer
mixer.init()
  
# Loading the song
MUSIC_FILE_PATH: str = "/Users/audrey/Desktop/school/comp110-22s-workspace/hack110/RhythmGame/heatwaves.ogg"
mixer.music.load(MUSIC_FILE_PATH)
  
# Setting the volume
mixer.music.set_volume(5)
  
# Start playing the song
mixer.music.play(loops=1)


left_arrow = pygame.image.load('/Users/audrey/Desktop/school/comp110-22s-workspace/hack110/RhythmGame/left_arrow.png').convert_alpha()  # or .convert_alpha()
left_arrow = pygame.transform.scale(left_arrow, (50, 50))
left = left_arrow.get_rect()
left.center = (200, 300)

up_arrow = pygame.image.load('/Users/audrey/Desktop/school/comp110-22s-workspace/hack110/RhythmGame/up_arrow.png').convert_alpha()  # or .convert_alpha()
up_arrow = pygame.transform.scale(up_arrow, (50, 50))
up = up_arrow.get_rect()
up.center = (350, 300)

down_arrow = pygame.image.load('/Users/audrey/Desktop/school/comp110-22s-workspace/hack110/RhythmGame/down_arrow.png').convert_alpha()  # or .convert_alpha()
down_arrow = pygame.transform.scale(down_arrow, (50, 50))
down = down_arrow.get_rect()
down.center = (500, 300)

right_arrow = pygame.image.load('/Users/audrey/Desktop/school/comp110-22s-workspace/hack110/RhythmGame/right_arrow.png').convert_alpha()  # or .convert_alpha()
right_arrow = pygame.transform.scale(right_arrow, (50, 50))
right = right_arrow.get_rect()
right.center = (650, 300)

arrows = [left, up, down, right]

run = True
while run:

    clock.tick(60)

    screen.fill((255, 255, 255))

    screen.blit(left_arrow, left)
    screen.blit(up_arrow, up) 
    screen.blit(down_arrow, down)
    screen.blit(right_arrow, right)

    left.y += 10
    if left.y > 600:
        left.y = -150
        left.x = 200
    
    up.y += 10
    if up.y > 600:
        up.y = -150
        up.x = 350
    
    down.y += 10
    if down.y > 600:
        down.y = -150
        down.x = 500
    
    right.y += 10
    if right.y > 600:
        right.y = -150
        right.x = 650

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()