import pygame
from random import randint

pygame.init()
screen = pygame.display.set_mode((700,700))
done = False

x = 0
y = 0
changeX = 10
changeY = 10
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if x >= 600:
            changeX = -1 *randint(0,20)
        else:
            changeX = randint(0,20)

        x += changeX

        if y >= 600:
            changeY = -1 * randint(0,20)
        else:
            changeY = randint(0,20)

        y += changeY

    pygame.draw.rect(screen, (0,x%255,y%255), pygame.Rect(x,y,60,60))
    pygame.display.flip()

