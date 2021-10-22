import math


class Point():
    def __init__(self, arg1, arg2=None):
        if arg2 is None:
            self.x = arg1[0]
            self.y = arg1[1]
        else:
            self.x = arg1
            self.y = arg2

    def __getitem__(self, item):
        if item == 0:
            return self.x
        elif item == 1:
            return self.y
        else:
            raise Exception("Nope, only got 2")

    def __len__(self):
        return 2

    def move(self, angle, distance):
        newY = self.y + math.cos(math.radians(angle)) * distance
        newX = self.x + math.sin(math.radians(angle)) * distance
        return Point(newX, newY)

    def __eq__(self, other):
        return other.x == self.x and other.y == self.y

    def __repr__(self):
        return f'({self.x}, {self.y})'
