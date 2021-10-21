class SillyStrategy:
    def __init__(self, turn_rate, forward=True):
        self.turn_rate = turn_rate
        self.forward = forward

    def __call__(self, *args, **kwargs):
        tank = args[0]

        tank.turn(self.turn_rate)
        tank.turn_turret(-self.turn_rate)
        if self.forward:
            tank.accelerate()
        else:
            tank.decelerate()

    def dispatch(self, event):
        pass
