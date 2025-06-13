#program to initialize a resizeable window
import pygame

#initialize pygame
pygame.init()

#create a resizable screen
screen = pygame.display.set_mode((500,500), pygame.RESIZABLE  )

pygame.display.set_caption("Resizeable window, i am going to create pubg soon")

#running the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#Quit pygame after closing the window. So closing does not mean that you closed pygame completely, it may still be functional in the background. Better practice to close it ;>
pygame.quit()
