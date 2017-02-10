from RouteGraph import RouteGraph


class RailroadService:
    """Classes for railroad service.
    """
    def __init__(self, routes: str):
        """Constructor.
        routes: str, represents the list of towns connected with their distance separated by comma.

        Example: AB5,BC4,CD8,DC8,DE6,AD5,CE2,EB3,AE7
        """
        self.__route_graph = RouteGraph(routes)

    def get_route_information(self):
        """Gets all of information about the routes.
        """
        route_info = 'Output #1:' + str(self.__route_graph.get_distance_route('A-B-C'))
        route_info += '\nOutput #2:' + str(self.__route_graph.get_distance_route('A-D'))
        route_info += '\nOutput #3:' + str(self.__route_graph.get_distance_route('A-D-C'))
        route_info += '\nOutput #4:' + str(self.__route_graph.get_distance_route('A-E-B-C-D'))
        route_info += '\nOutput #5:' + str(self.__route_graph.get_distance_route('A-E-D'))
        route_info += '\nOutput #6:' + str(self.__route_graph.get_number_stops_from_trip('C', 'C', 3))
        route_info += '\nOutput #7:' + str(self.__route_graph.get_number_stops_from_circular_trip('A', 'C', 4))
        route_info += '\nOutput #8:' + str(self.__route_graph.get_shorest_distance_route('A', 'C'))
        route_info += '\nOutput #9:' + str(self.__route_graph.get_shorest_distance_route('B', 'B'))
        route_info += '\nOutput #10:' + str(self.__route_graph.get_all_different_routes('C', 'C', 30))

        return route_info

