import context
from unittest import TestCase
from point import Point


class TestPoint(TestCase):
    def test_can_construct_points(self):
        for p in [Point((1, 2)), Point(1, 2), Point(Point(1, 2))]:
            self.assertEqual(1, p.x, f'p.x not right for {p}')
            self.assertEqual(2, p.y, f'p.y not right for {p}')
            self.assertEqual(2, len(p), f'len not right for {p}')
