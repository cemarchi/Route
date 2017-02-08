from DirectedGraph import DirectedGraph


class Router:
    def __init__(self, routes: str):
        self.__graph = DirectedGraph.create_graph(routes)

    def get_route_information(self):
        route_info = 'Output #1:' + str(self.__get_distance_route('A-B-C'))
        route_info += '\nOutput #2:' + str(self.__get_distance_route('A-D'))
        route_info += '\nOutput #3:' + str(self.__get_distance_route('A-D-C'))
        route_info += '\nOutput #4:' + str(self.__get_distance_route('A-E-B-C-D'))
        route_info += '\nOutput #5:' + str(self.__get_distance_route('A-E-D'))
        route_info += '\nOutput #6:' + str(self.__get_number_stops_from_trip('C', 'C', 3))
        route_info += '\nOutput #7:' + str(self.__get_number_stops_from_circular_trip('A', 'C', 4))
        route_info += '\nOutput #8:' + str(self.__get_shorest_distance_route('A', 'C'))
        route_info += '\nOutput #9:' + str(self.__get_shorest_distance_route('B', 'B'))
        route_info += '\nOutput #10:' + str(self.__get_all_differente_routes('C', 'C', 30))

        return route_info

    def __get_distance_route(self, path: str):

        nodes = path.split('-')
        distance = 0

        if nodes[0] not in self.__graph:
            return 'NO SUCH ROUTE'

        for i, node in enumerate(nodes[:-1]):
            edge = [n for n in self.__graph[node] if n.node == nodes[i + 1]]
            if not edge:
                return 'NO SUCH ROUTE'

            distance += edge[0].weight

        return distance

    def __get_number_stops_from_trip(self, city_start: str, city_end: str, stop_count: int):
        queue = [(city_start, [city_start])]
        stops = []

        while queue:
            (node, path) = queue.pop(0)

            for next_node in self.__graph[node]:
                if next_node.node == city_end:
                    if len(path[1:] + [next_node]) <= stop_count:
                        stops.append(path + [next_node])
                else:
                    queue.append((next_node.node, path + [next_node]))

        return len(stops)

    def __get_number_stops_from_circular_trip(self, city_start: str, city_end: str, stop_count: int):
        queue = [(city_start, [city_start])]
        stops = []

        while queue:
            (node, path) = queue.pop(0)

            for next_node in self.__graph[node]:
                if next_node.node == city_end and len(path[1:] + [next_node]) == stop_count:
                    stops.append(path + [next_node])
                elif len(path) < stop_count:
                    queue.append((next_node.node, path + [next_node]))

        return len(stops)

    def __get_shorest_distance_route(self, city_start: str, city_end: str):
        distances = []
        queue = [(city_start, [city_start])]

        while queue:
            (node, path) = queue.pop(0)
            for next_node in self.__graph[node]:
                if next_node.node == city_end:
                    distances.append(path + [next_node])
                elif next_node not in path[1:]:
                    queue.append((next_node.node, path + [next_node]))

        return min([sum([d.weight for d in dt[1:]]) for dt in distances])

    def __get_all_differente_routes(self, city_start: str, city_end: str, distance_limit: int):

        queue = [(city_start, [city_start])]
        trips = []

        while queue:
            (node, path) = queue.pop(0)

            for next_node in self.__graph[node]:
                distance = next_node.weight + sum([p.weight for p in path[1:]]) if path[1:] else 0

                if next_node.node == city_end and distance < distance_limit:
                    trip = '{0}{1}'.format(path[0], ''.join([p.node for p in path[1:]]), next_node.node)

                    if trip not in trips:
                        trips.append(trip)

                if distance < distance_limit:
                    queue.append((next_node.node, path + [next_node]))

        return len(trips)