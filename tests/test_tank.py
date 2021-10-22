import context
import unittest
import tank
from point import Point


class TestTank(unittest.TestCase):
    def test_can_create_tank(self):
        tank.Tank((0, 0))

    def test_can_reverse(self):
        t = tank.Tank((10, 10))
        t.orientation = 0
        t.speed = -5
        t.move()

        self.assertEqual(Point(10, 5), t.pos)

    def test_can_forward(self):
        t = tank.Tank((10, 10))
        t.orientation = 0
        t.speed = 5
        t.move()

        self.assertEqual(Point(10, 15), t.pos)

    def test_turn_slightly(self):
        t = tank.Tank((10, 10))
        t.speed = 1
        t.orientation = 10
        t.move()
        self.assertNotEqual(10, t.pos.x, "Can turn slightly left")

        t = tank.Tank((10, 10))
        t.speed = 1
        t.orientation = -10
        t.move()
        self.assertNotEqual(10, t.pos.x, "Can turn slightly and right")


if __name__ == '__main__':
    unittest.main()
