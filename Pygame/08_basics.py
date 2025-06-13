#Program to set the title of my display

import pygame

pygame.init()

screen = pygame.display.set_mode((600,600))

#Setting the title of the game window
pygame.display.set_caption("My Game Window")

#First we have to load the image
icon = pygame.image.load("spiderman-1366x768-yg38vlpoyierydqg.jpg")
#now we set the image
pygame.display.set_icon(icon)

#setting up the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#thats how you do it ! now only keep one thing in mind that is to LOAD the image first then set the icon.