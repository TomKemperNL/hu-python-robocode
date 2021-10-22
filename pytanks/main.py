import pygame, sys

from display import Display
from game import Game
from manual_strategy import ManualStrategy
from silly_strategy import SillyStrategy
from tank import Tank

from pygame.locals import *

pygame.init()
display = Display(pygame.display.set_mode((1024, 768)))

current_game = Game(display)

t1 = Tank((100, 100))
t1.color = (0, 7, 111)
t1Strat = ManualStrategy()

current_game.add_tank(t1, t1Strat)

t2 = Tank((700, 500))
t2.color = (229, 78, 208)
t2Strat = SillyStrategy(-5, False)

current_game.add_tank(t2, t2Strat)

FPS = 60
tock = pygame.time.Clock()

while True:
    events = pygame.event.get()

    for event in events:
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)
    current_game.step(events)

    pygame.display.update()
    tock.tick(FPS)
