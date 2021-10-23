from bullet import Bullet
from point import Point

max_speed = 5
min_speed = int(max_speed * - 0.5)


class Tank:
    def __init__(self, pos):
        self.pos = Point(pos)
        self.orientation = 0
        self.barrel_orientation = 0
        self.size = 10
        self.speed = 0
        self.color = 'red'
        self.game = None

    def fire(self):
        bullet = Bullet(self.get_barrel_end(), self.barrel_orientation)
        self.game.add_object(bullet)

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

    def get_barrel_end(self):
        barrel_size = self.size * 2
        return self.pos.move(self.barrel_orientation, barrel_size)

    def draw(self, surface):
        surface.draw_tank(self)
