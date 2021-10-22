import pygame


class Display:
    def __init__(self, pygame_display):
        self.surface = pygame_display
        pass

    def clear(self):
        self.surface.fill((255, 255, 255))

    def draw_tank(self, tank):
        line_size = 2
        tank_size = tank.size * 3

        pygame.draw.polygon(self.surface, tank.color, [
            tank.pos.move(tank.orientation + 45, 0.5 * tank_size),
            tank.pos.move(tank.orientation - 45, 0.5 * tank_size),
            tank.pos.move(tank.orientation + 45, 0.5 * - tank_size),
            tank.pos.move(tank.orientation - 45, 0.5 * -tank_size)], line_size)

        front_end = tank.size * 2
        pygame.draw.polygon(self.surface, tank.color, [
            tank.pos.move(tank.orientation + 45, 0.5 * tank_size),
            tank.pos.move(tank.orientation - 45, 0.5 * tank_size),
            tank.pos.move(tank.orientation, front_end)], line_size)

        barrel_thickness = line_size * 3
        pygame.draw.line(self.surface, tank.color, tank.pos, tank.get_barrel_end(),
                         barrel_thickness)

    def draw_bullet(self, bullet):
        pygame.draw.circle(self.surface, 'black', bullet.pos, 5, 5)
