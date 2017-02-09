class Route:
    """Classes for the route.
    """

    def __init__(self, town: str, distance: int):
        """Constructor.
        town: str, represents the city connected
        distance: int, that's the distance among two towns
        """
        self.__town = town
        self.__distance = distance

    def __eq__(self, other):
        return self.__town == other.town and self.__distance == other.distance

    @property
    def town(self):
        """town property - str: that connected with another town
        """
        return self.__town

    @property
    def distance(self):
        """distance property - int: that represents the distance from town to  this town
        """
        return self.__distance
