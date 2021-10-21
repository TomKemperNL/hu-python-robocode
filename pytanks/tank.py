import pygame
import math

from point import Point

line_size = 2
max_speed = 5
min_speed = max_speed * - 0.5


class Tank:
    def __init__(self, pos):
        self.pos = Point(pos)
        self.orientation = 0
        self.barrel_orientation = 0
        self.size = 10
        self.speed = 0
        self.color = 'red'

    def move(self):
        self.pos = self.pos.move(self.orientation, self.speed)

    def turn(self, degrees):
        self.orientation += degrees

    def turn_turret(self, degrees):
        self.barrel_orientation += degrees

    def accelerate(self):
        self.speed += 1
        self.speed = min(self.speed, max_speed)

    def decelerate(self):
        self.speed -= 1
        self.speed = max(self.speed, min_speed)

    def draw(self, surface):
        tank_size = self.size * 3

        pygame.draw.polygon(surface, self.color, [
            self.pos.move(self.orientation + 45, 0.5 * tank_size),
            self.pos.move(self.orientation - 45, 0.5 * tank_size),
            self.pos.move(self.orientation + 45, 0.5 * - tank_size),
            self.pos.move(self.orientation - 45, 0.5 * -tank_size)], line_size)

        front_end = self.size * 2
        pygame.draw.polygon(surface, self.color, [
            self.pos.move(self.orientation + 45, 0.5 * tank_size),
            self.pos.move(self.orientation - 45, 0.5 * tank_size),
            self.pos.move(self.orientation, front_end)], line_size)

        barrel_size = self.size * 2
        barrel_thickness = line_size * 3
        pygame.draw.line(surface, self.color, self.pos, self.pos.move(self.barrel_orientation, barrel_size),
                         barrel_thickness)
