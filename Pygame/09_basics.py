#we are going to do a fun thing in this one. A ever color changing game window

import pygame

pygame.init()

screen = pygame.display.set_mode((700,700))#beware! in order to implement any changes done to the game window after this line, make sure to call the flip function.

pygame.display.set_caption("Color changing window")

color = "blue"



running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if color == "blue":
        color = "red"
    else:
        color = "blue"

    screen.fill(color)

    pygame.display.flip()#you need to write this one or else screen balck ki black hi reh jayegi. This happens because as soon as the 7th line is executed the screen is displayed on the computer display, all the changes made to the screen object after the 7th line are done back of the scene but to implement these changes on the computer display, to the outside world, we have to call the flip function.RULE OF THUMB: flip function should be called after all the changes are done to the screen object.
#pygame.display.flip()