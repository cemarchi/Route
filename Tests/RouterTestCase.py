import unittest

from Src.Router import Router


class RouterTestCase(unittest.TestCase):
    def setUp(self):
        self.__graph = 'AB5,BC4,CD8,DC8,DE6,AD5,CE2,EB3,AE7'

    def test_router(self):
        router = Router(self.__graph)
        router.get_route_information()

        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
