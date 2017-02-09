from Src.Route import Route


class RouteGraph:
    """Classes for manipulates the routes among towns and trips.
    """
    def __init__(self, routes: str):
        """Constructor.
        routes: str, represents the list of towns connected with their distance separated by comma.

        Example: AB5,BC4,CD8,DC8,DE6,AD5,CE2,EB3,AE7
        """
        self.__graph = self.__create(routes)

    def __create(self, routes: str):
        graph = {}
        routes = routes.replace(' ', '')

        for r in routes.split(','):

            if r[0] in graph:
                graph[r[0]].append(Route(r[1], int(r[2:])))
            else:
                graph[r[0]] = [Route(r[1], int(r[2:]))]

        return graph

    def get_distance_route(self, path: str):
        """Calculates the distance of route according on list of cities.
        path - str: it is a list of cities in the route. Each city must be separated with '-' charactere

        Example:A-B-C
        """
        towns = path.split('-')
        distance = 0

        if towns[0] not in self.__graph:
            return 'NO SUCH ROUTE'

        for i, town in enumerate(towns[:-1]):
            route = [t for t in self.__graph[town] if t.town == towns[i + 1]]
            if not route:
                return 'NO SUCH ROUTE'

            distance += route[0].distance

        return distance

    def get_number_stops_from_trip(self, town_start: str, town_end: str, stop_count: int):
        """Calculates the number of stops in the trip according on two cities (start at city and end at city).
        town_start - str: it is a city where starts the trip. It can be the same town in the town_end.
        town_end - str: it is a city that ends the trips. It can be the same town in the town_start.
        stop_count - str: it is a limit (less or equal) of number of stops in the trip.
        """
        queue = [(town_start, [town_start])]
        stops = []

        while queue:
            (town, path) = queue.pop(0)

            for next_town in self.__graph[town]:
                if next_town.town == town_end:
                    if len(path[1:] + [next_town]) <= stop_count:
                        stops.append(path + [next_town])
                else:
                    queue.append((next_town.town, path + [next_town]))

        return len(stops)

    def get_number_stops_from_circular_trip(self, town_start: str, town_end: str, stop_count: int):
        """Calculates the number of stops in the trip according on two cities (start at city and end at city).
        If there is other route in town_end and stop_count didn't reach. It will continue walking.
        town_start - str: it is a city where starts the trip.
        town_end - str: it is a city that ends the trips.
        stop_count - str: it is a limit (less or equal) of number of stops in the trip.
        """
        queue = [(town_start, [town_start])]
        stops = []

        while queue:
            (town, path) = queue.pop(0)

            for next_town in self.__graph[town]:
                if next_town.town == town_end and len(path[1:] + [next_town]) == stop_count:
                    stops.append(path + [next_town])
                elif len(path) < stop_count:
                    queue.append((next_town.town, path + [next_town]))

        return len(stops)

    def get_shorest_distance_route(self, town_start: str, town_end: str):
        """Calculates and gets the shorest distance among two towns.
        town_start - str: it is a city where starts the trip. It can be the same town in the town_end.
        town_end - str: it is a city that ends the trips. It can be the same town in the town_start.
        stop_count - str: it is a limit (less or equal) of number of stops in the trip.
        """
        distances = []
        queue = [(town_start, [town_start])]

        while queue:
            (town, path) = queue.pop(0)
            for next_town in self.__graph[town]:
                if next_town.town == town_end:
                    distances.append(path + [next_town])
                elif next_town not in path[1:]:
                    queue.append((next_town.town, path + [next_town]))

        return min([sum([d.distance for d in dt[1:]]) for dt in distances])

    def get_all_different_routes(self, town_start: str, town_end: str, distance_limit: int):
        """Calculates and find the all the  routes among two towns.
        town_start - str: it is a city where starts the trip. It can be the same town in the town_end.
        town_end - str: it is a city that ends the trips. It can be the same town in the town_start.
        distance_limit - str: routes with distance less than distance_limit are computed.
        """
        queue = [(town_start, [town_start])]
        trips = []

        while queue:
            (town, path) = queue.pop(0)

            for next_town in self.__graph[town]:
                distance = next_town.distance + sum([p.distance for p in path[1:]]) if path[1:] else 0

                if next_town.town == town_end and distance < distance_limit:
                    trip = '{0}{1}'.format(path[0], ''.join([p.town for p in path[1:]]), next_town.town)

                    if trip not in trips:
                        trips.append(trip)

                if distance < distance_limit:
                    queue.append((next_town.town, path + [next_town]))

        return len(trips)
