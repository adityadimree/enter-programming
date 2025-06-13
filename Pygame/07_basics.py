#Program to set background color of my game window
import pygame

#initialize pygame modules
pygame.init()

#initialize the game screen
screen = pygame.display.set_mode((500,500))

#setting the loop up
running = True

while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#if the code from 18th line to 25th line is outside the scope of while loop then the screen color will not be red as python interpreter performs line by line execution and the interpretation will wait for an event at the end of 16 line (maybe)
    color = (0,0,255)

    #filling the screen
    screen.fill(color)

    #if you do not write this then the color will not change because hamne screen pehle bana di hai bina color set  kre toh voh esa hi rahega. baad me jo changes kiye hai unka affect karane ke liye hame update krna padegha screen ko !!
    pygame.display.flip()