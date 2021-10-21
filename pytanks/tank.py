import pygame
import math

from point import Point


class Tank:
    def __init__(self, pos):
        self.pos = Point(pos)
        self.orientation = 0
        self.barrel_orientation = 0
        self.size = 10
        self.speed = 5
        self.color = 'red'

    def move(self):
        self.pos = self.pos.move(self.orientation, self.speed)

    def draw(self, surface):
        pygame.draw.polygon(surface, self.color, [
            (self.pos[0] - self.size, self.pos[1] - self.size), (self.pos[0] + self.size, self.pos[1] - self.size),
            (self.pos[0] + self.size, self.pos[1] + self.size), (self.pos[0] - self.size, self.pos[1] + self.size)], 2)

        barrel_size = self.size * 2
        pygame.draw.line(surface, self.color, self.pos, self.pos.move(self.barrel_orientation, barrel_size), 5)
