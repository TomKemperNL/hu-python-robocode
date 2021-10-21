import context
from unittest import TestCase
from point import Point


class TestPoint(TestCase):
    def test_can_construct_points(self):
        for p in [Point((1, 2)), Point(1, 2), Point(Point(1, 2))]:
            self.assertEqual(1, p.x, f'p.x not right for {p}')
            self.assertEqual(2, p.y, f'p.y not right for {p}')
            self.assertEqual(2, len(p), f'len not right for {p}')

    def test_move_point(self):
        self.assertEqual(Point(1, 12), Point(1, 2).move(0, 10))
        self.assertEqual(Point(11, 2), Point(1, 2).move(90, 10))
        self.assertEqual(Point(1, -8), Point(1, 2).move(180, 10))
        self.assertEqual(Point(-9, 2), Point(1, 2).move(270, 10))
        self.assertEqual(Point(1, 12), Point(1, 2).move(360, 10))

        self.assertEqual(Point(1, 2), Point(1, 2).move(0, 0))
        self.assertEqual(Point(1, 2), Point(1, 2).move(90, 0))
        self.assertEqual(Point(1, 2), Point(1, 2).move(180, 0))
        self.assertEqual(Point(1, 2), Point(1, 2).move(270, 0))
        self.assertEqual(Point(1, 2), Point(1, 2).move(360, 0))
