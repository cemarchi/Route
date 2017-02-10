import unittest
import sys

sys.path.append('..\Src')

from Src.RouteGraph import RouteGraph


class RouteGraphTestCase(unittest.TestCase):
    def setUp(self):
        self.__rout_graph = RouteGraph('AB5,BC4,CD8,DC8,DE6,AD5,CE2,EB3,AE7')

    def test_get_route_information(self):
        self.assertTrue(self.__rout_graph.get_distance_route('A-B-C'), 9)
        self.assertTrue(self.__rout_graph.get_distance_route('A-D'), 5)
        self.assertTrue(self.__rout_graph.get_distance_route('A-E-B-C-D'), 13)
        self.assertTrue(self.__rout_graph.get_distance_route('A-E-D'), 'NO SUCH ROUTE')

    def test_get_number_stops_from_trip(self):
        self.assertTrue(self.__rout_graph.get_number_stops_from_trip('C', 'C', 3), 2)

    def test_get_number_stops_from_circular_trip(self):
        self.assertTrue(self.__rout_graph.get_number_stops_from_circular_trip('A', 'C', 4), 2)

    def test_get_shorest_distance_route(self):
        self.assertTrue(self.__rout_graph.get_shorest_distance_route('A', 'C'), 9)
        self.assertTrue(self.__rout_graph.get_shorest_distance_route('B', 'B'), 9)

    def test_get_all_different_routes(self):
        self.assertTrue(self.__rout_graph.get_all_different_routes('C', 'C', 30), 7)


if __name__ == '__main__':
    unittest.main()
