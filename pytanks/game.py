command_interval = 5


class Game:
    def __init__(self, display):
        self.objects = []
        self.tanks = []
        self.display = display
        self.counter = 0

    def add_object(self, obj):
        self.objects.append(obj)

    def remove_object(self, obj):
        self.objects.remove(obj)

    def add_tank(self, tank, strat):
        self.tanks.append((tank, strat))
        tank.game = self

    def step(self, events):
        self.display.clear()

        for event in events:
            for t, tstrat in self.tanks:
                tstrat.dispatch(event)

        if self.counter != 0 and self.counter % command_interval == 0:
            for t, tstrat in self.tanks:
                tstrat(t)
            counter = 0

        for g in self.objects:
            g.move()
            g.draw(self.display)

        for t, tstrat in self.tanks:
            t.move()
            t.draw(self.display)
        self.counter += 1
