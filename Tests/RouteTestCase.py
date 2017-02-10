import unittest
import sys

sys.path.append('..\Src')

from Src.Route import Route


class RouteTestCase(unittest.TestCase):
    def test_properties(self):
        route = Route('A', 5)
        self.assertTrue(route.town, 'A')
        self.assertTrue(route.distance, 5)

    def test_equal(self):
        route = Route('A', 5)
        route2 = Route('A', 5)

        self.assertEqual(route, route2)


if __name__ == '__main__':
    unittest.main()
