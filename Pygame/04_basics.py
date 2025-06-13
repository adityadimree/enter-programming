import pygame

#initializing pygame modules
pygame.init()

#intializing a screen
game_screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Game")#pygame is an object here with an attribute display

#running the game loop and looking for events
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
