import pygame
import random
from pygame import mixer # Load the required library

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((700,700))

pygame.display.set_caption('Pong')

done = False

ballX = 350
ballY = 250

enemyX = 50

randX = random.randrange(0,2)
randY = random.randrange(0,2)
xSpeed = -1 * random.randrange(2,6) if randX == 0 else 1 * random.randrange(2,6)
ySpeed = -1 * random.randrange(2,6) if randY == 0 else 1 * random.randrange(2,6)
p1Score = 0
p2Score = 0

startScr = True
gameRun = True
gameOver = False
scoreScr = False

startList = ['Start','Scores','Exit']

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if gameRun:

        paddleX, paddleY = pygame.mouse.get_pos()
        #print(str(ballX - paddleX) + "," + str(ballY - paddleY))


        if ballX >= 680:
            xSpeed = -1 * random.randrange(2, 6)

        if ballY >= 630:
            if ballX >= paddleX - 20 and ballX <= paddleX + 60:
                ySpeed = -1 * random.randrange(2, 6)
            else:
                p1Score += 1
                ballX = 350
                ballY = 250
                enemyX = 50
                randX = random.randrange(0, 2)
                randY = random.randrange(0, 2)
                xSpeed = -1 * random.randrange(2, 6) if randX == 0 else 1 * random.randrange(2, 6)
                ySpeed = -1 * random.randrange(2, 6) if randY == 0 else 1 * random.randrange(2, 6)

        if ballX <= 20:
            xSpeed = 1 * random.randrange(2, 6)

        if ballY <= 70:
            if ballX >= enemyX - 20 and ballX <= enemyX + 60:
                ySpeed = 1 * random.randrange(2, 6)
            else:
                p2Score += 1
                ballX = 350
                ballY = 250
                enemyX = 50
                randX = random.randrange(0, 2)
                randY = random.randrange(0, 2)
                xSpeed = -1 * random.randrange(2, 6) if randX == 0 else 1 * random.randrange(2, 6)
                ySpeed = -1 * random.randrange(2, 6) if randY == 0 else 1 * random.randrange(2, 6)

        if ballX - enemyX > 40 and enemyX <= 640:
            diff = abs(ballX - enemyX)
            enemyX += random.randrange(diff % 5, diff % 5 + 3)
        elif ballX - enemyX < -40 and enemyX >= 0:
            diff = abs(ballX - enemyX)
            enemyX -= random.randrange(diff % 5, diff % 5 + 3)
        else:
            enemyX += 0




        ballX += xSpeed
        ballY += ySpeed

        screen.fill((0, 0, 0))

        myfont = pygame.font.SysFont('Arial', 50)
        scoreShow = myfont.render(str(p1Score) + "-" + str(p2Score), True, (0, 150, 255))
        screen.blit(scoreShow, (350, 10))

        pygame.draw.rect(screen, (0, 125, 225), pygame.Rect(paddleX, 650, 60, 30))
        pygame.draw.circle(screen, (0, 125, 225), (ballX, ballY), 20)

        pygame.draw.rect(screen, (0, 125, 225), pygame.Rect(enemyX, 40, 60, 30))
    elif gameOver:
        myfont = pygame.font.SysFont('Arial', 30)
        scoreTxt = myfont.render('You got a score of ' + score, True, (0, 0, 0))
        screen.blit(scoreTxt, (10, 10))
    elif scoreScr:
        myfont = pygame.font.SysFont('Arial', 30)
        txtStart = myfont.render('Start', True, (0, 0, 0))
        screen.blit(txtStart, (10, 10))
    else:
        myfont = pygame.font.SysFont('Arial', 30)
        for i in range(0,startList.__len__()):
            txtStart = myfont.render(startList[i], True, (0, 150, 255))
            screen.blit(txtStart, (250, 250 + i * 50))

    pygame.display.flip()

