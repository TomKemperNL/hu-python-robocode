import pygame, sys

from manual_strategy import ManualStrategy
from silly_strategy import SillyStrategy
from tank import Tank

from pygame.locals import *

pygame.init()
DISPLAY = pygame.display.set_mode((1024, 768))
FPS = 60

loc = 0
tock = pygame.time.Clock()

t1 = Tank((100, 100))
t1.color = (0, 7, 111)
t1Strat = ManualStrategy()
t2 = Tank((700, 500))
t2.color = (229, 78, 208)
t2Strat = SillyStrategy(-5, False)

command_interval = 5
counter = 0

tanks = [
    (t1, t1Strat),
    (t2, t2Strat)
]

while True:
    DISPLAY.fill((255, 255, 255))

    for event in pygame.event.get():
        for t, tstrat in tanks:
            tstrat.dispatch(event)

        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)

    if counter != 0 and counter % command_interval == 0:
        for t, tstrat in tanks:
            tstrat(t)
        counter = 0

    for t, tstrat in tanks:
        t.move()
        t.draw(DISPLAY)
    counter += 1

    pygame.display.update()
    tock.tick(FPS)
