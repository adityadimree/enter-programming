import pygame
from pygame.locals import *

class Sq(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((0, 200, 255))

pygame.init() # Init Pygame
win = pygame.display.set_mode((800, 600))##sets up the game window of 800x800
# Create 4 squares
s1, s2, s3, s4 = Sq(), Sq(), Sq(), Sq()

#Game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE):
            run = False
    # Draw squares in corner
    win.blit(s1.surf, (40, 40))
    win.blit(s2.surf, (40, 530))
    win.blit(s3.surf, (730, 40))
    win.blit(s4.surf, (730, 530))

    pygame.display.flip()
