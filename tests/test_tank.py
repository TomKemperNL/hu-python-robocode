import context
import unittest
import tank


class TestTank(unittest.TestCase):
    def test_can_create_tank(self):
        tank.Tank((0, 0))


if __name__ == '__main__':
    unittest.main()
