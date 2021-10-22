from pygame.locals import *

turn_rate = 10


class ManualStrategy:
    def __init__(self):
        self.increase_speed = False
        self.decrease_speed = False
        self.turn_left = False
        self.turn_right = False
        self.turn_turret_left = False
        self.turn_turret_right = False

    def reset(self):
        self.increase_speed = False
        self.decrease_speed = False
        self.turn_left = False
        self.turn_right = False
        self.turn_turret_left = False
        self.turn_turret_right = False

    def dispatch(self, event):
        if event.type == KEYDOWN:
            if event.key == K_a:
                self.turn_left = True
            if event.key == K_d:
                self.turn_right = True
            if event.key == K_w:
                self.increase_speed = True
            if event.key == K_s:
                self.decrease_speed = True
            if event.key == K_q:
                self.turn_turret_left = True
            if event.key == K_e:
                self.turn_turret_right = True
        elif event.type == KEYUP:
            if event.key == K_a:
                self.turn_left = False
            if event.key == K_d:
                self.turn_right = False
            if event.key == K_w:
                self.increase_speed = False
            if event.key == K_s:
                self.decrease_speed = False
            if event.key == K_q:
                self.turn_turret_left = False
            if event.key == K_e:
                self.turn_turret_right = False

    def __call__(self, *args, **kwargs):
        tank = args[0]

        if self.increase_speed:
            tank.accelerate()
        if self.decrease_speed:
            tank.decelerate()
        if self.turn_left:
            tank.turn(-turn_rate)
        if self.turn_right:
            tank.turn(turn_rate)
        if self.turn_turret_left:
            tank.turn_turret(-turn_rate)
        if self.turn_turret_right:
            tank.turn_turret(turn_rate)


