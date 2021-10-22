import pygame

from point import Point

bullet_speed = 20


class Bullet:
    def __init__(self, pos, angle):
        self.pos = Point(pos)
        self.angle = angle
        self.speed = bullet_speed

    def move(self):
        self.pos = self.pos.move(self.angle, self.speed)

    def draw(self, surface):
        surface.draw_bullet(self)
