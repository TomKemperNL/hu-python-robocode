import pygame, sys
from tank import Tank

from pygame.locals import *

pygame.init()
DISPLAY = pygame.display.set_mode((1024, 768))
FPS = 60

loc = 0
tock = pygame.time.Clock()

t1 = Tank((100, 100))
t1.color = (0, 7, 111)
t2 = Tank((700, 500))
t2.color = (229, 78, 208)

command_interval = 5
counter = 0

while True:
    DISPLAY.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)

    if counter != 0 and counter % command_interval == 0:
        t1.turn(10)
        t1.turn_turret(-10)
        t1.accelerate()

        t2.turn(-10)
        t2.turn_turret(10)
        t2.decelerate()
        counter = 0

    t1.move()
    t2.move()
    t1.draw(DISPLAY)
    t2.draw(DISPLAY)
    counter += 1

    pygame.display.update()
    tock.tick(FPS)
