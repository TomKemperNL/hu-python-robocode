import pygame
import math


class Tank:
    def __init__(self, pos):
        self.pos = pos
        self.orientation = 0
        self.barrel_orientation = 0
        self.size = 10
        self.speed = 5
        self.color = 'red'

    def move(self):
        self.pos = (self.pos[0], self.pos[1] + self.speed)

    def draw(self, surface):
        pygame.draw.polygon(surface, self.color, [
            (self.pos[0] - self.size, self.pos[1] - self.size), (self.pos[0] + self.size, self.pos[1] - self.size),
            (self.pos[0] + self.size, self.pos[1] + self.size), (self.pos[0] - self.size, self.pos[1] + self.size)], 2)

        barrel_size = self.size * 2
        barrelX = self.pos[0] + (math.sin(math.radians(self.barrel_orientation)) * barrel_size)
        barrelY = self.pos[1] - (math.cos(math.radians(self.barrel_orientation)) * barrel_size)
        pygame.draw.line(surface, self.color, self.pos, (barrelX, barrelY), 5)
