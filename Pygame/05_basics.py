#getting the size of my window
import pygame

pygame.init()

screen = pygame.display.set_mode()

#get the default size, meaning the size of your default screen.
(x, y) = screen.get_size()

pygame.quit()

print((x,y))