import unittest
import sys

sys.path.append('..\Src')

from Src.Route import Route


class RouteTestCase(unittest.TestCase):
    def test_properties(self):
        route = Route('A', 5, 4)
        self.assertEqual(route.town, 'A')
        self.assertEqual(route.distance, 5)

    def test_equal(self):
        route = Route('A', 5, 4)
        route2 = Route('A', 5, 4)

        self.assertEqual(route, route2)


if __name__ == '__main__':
    unittest.main()
