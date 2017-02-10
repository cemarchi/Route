import unittest
import sys

sys.path.append('..\Src')

from Src.RailroadService import RailroadService


class RailroadServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.__graph = 'AB5,BC4,CD8,DC8,DE6,AD5,CE2,EB3,AE7'

    def test_get_route_information(self):
        railroad_service = RailroadService(self.__graph)
        expected = 'Output #1: 9\n' \
             'Output #2: 5\n' \
             'Output #3: 13\n' \
             'Output #4: 22\n' \
             'Output #5: NO SUCH ROUTE\n' \
             'Output #6: 2\n' \
             'Output #7: 3\n' \
             'Output #8: 9\n' \
             'Output #9: 9\n' \
             'Output #10: 7'

        self.assertTrue(railroad_service.get_route_information(), expected)


if __name__ == '__main__':
    unittest.main()
