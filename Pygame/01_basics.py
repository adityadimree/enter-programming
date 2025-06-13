import pygame

#Initialize Pygame
pygame.init()

#settin up the game window
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hello Pygame")

#Game loop
running = True
while running:#running loops like this makes code more readable
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#Quit Pygame
pygame.quit()