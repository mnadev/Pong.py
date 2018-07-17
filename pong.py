import pygame
from random import randint

pygame.init()

screen = pygame.display.set_mode((700,700))

pygame.display.set_caption('Pong')

done = False



ballX = 350
ballY = 250
xSpeed = 5
ySpeed = 5

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    enemyX = 50
    paddleX, paddleY = pygame.mouse.get_pos()

    if ballX >= 680:
        xSpeed = -1 * xSpeed

    if ballY >= 680:
        ySpeed = -1 * ySpeed

    if ballX <=  20:
        xSpeed = -1 * xSpeed

    if ballY <=  20:
        ySpeed = -1 * ySpeed

    ballX += xSpeed
    ballY += ySpeed

    screen.fill((0,0,0))

    pygame.draw.rect( screen, (0,125,225), pygame.Rect(paddleX,650,60,30) )
    pygame.draw.circle(screen, (0, 125, 225), (ballX,ballY), 20)

    pygame.draw.rect(screen, (0, 125, 225), pygame.Rect(enemyX, 40, 60, 30))

    pygame.display.flip()

