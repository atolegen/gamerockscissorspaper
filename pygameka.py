import pygame
from pygame.locals import *
 

pygame.init()
pygame.display.set_caption("Scissors-paper-stone")

window = pygame.display.set_mode((600, 600))
 
image_sprite = [pygame.image.load("stone.png"),
                pygame.image.load("scissors.png"),
                pygame.image.load("paper.png")]
 
DEFAULT_IMAGE_SIZE = (50, 50)
for i in range(len(image_sprite)):
    image_sprite[i] = pygame.transform.scale(image_sprite[i], DEFAULT_IMAGE_SIZE)

clock = pygame.time.Clock()
 

value = 0
music = pygame.mixer.music.load('music.mp3') 
pygame.mixer.music.play(-1)

run = True
x=50
y=50 
i=0

while run:

    window.blit(image_sprite[i],(x,y))
 
    for event in pygame.event.get():
        if event.type==QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 2
    if keys[pygame.K_RIGHT]:
        x += 2
    if keys[pygame.K_UP]:
        y -= 2
    if keys[pygame.K_DOWN]:
        y += 2
    if keys[pygame.K_1]:
        i=0
    if keys[pygame.K_2]:
        i=1   
    if keys[pygame.K_3]:
        i=2 
    if keys[pygame.K_q]:
        run=False

 
    pygame.display.flip()
    clock.tick(120)

    window.fill((0, 0, 0))
