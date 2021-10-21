import pygame, sys
from tank import Tank

from pygame.locals import *

pygame.init()
DISPLAY = pygame.display.set_mode((800, 600))
FPS = 60

loc = 0
tock = pygame.time.Clock()

t1 = Tank((100, 100))
t1.orientation = 0
t2 = Tank((700, 500))
t2.orientation = 45
t2.barrel_orientation = 45

while True:
    DISPLAY.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)

    t1.move()
    t1.color = (0, 7, 111)
    #t2.move()
    t2.color = (229, 78, 208)

    t1.draw(DISPLAY)
    t2.draw(DISPLAY)
    pygame.display.update()
    tock.tick(FPS)
