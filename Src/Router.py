from Src.DirectedGraph import DirectedGraph


class Router:
    def __init__(self, routes: str):
        self.__graph = DirectedGraph.create_graph(routes)

    def get_route_information(self):
        route_info = []

        route_info.append(self.__get_distance_route('A-B-C'))
        route_info.append(self.__get_distance_route('A-D'))
        route_info.append(self.__get_distance_route('A-D-C'))
        route_info.append(self.__get_distance_route('A-E-B-C-D'))
        route_info.append(self.__get_distance_route('A-E-D'))

        route_info.append(self.__get_number_stops_from_trip('C', 'C', 3))
        route_info.append(self.__get_number_stops_from_trip('A', 'C', 4))
        route_info.append(self.__get_shorest_distance_route('A', 'C'))
        route_info.append(self.__get_shorest_distance_route('B', 'B'))
        route_info.append(self.__get_all_differente_routes('A-E-D'), 30)

        print(route_info)

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

    def __get_number_trips(self, city_start: str, city_end: str, stop_count: int):
        return len(self.__get_trips(city_start, city_end, stop_count))

    def __get_number_stops_from_trip(self, city_start: str, city_end: str, stop_count: int):
        return len(list(self.__get_trips(city_start, city_end, stop_count)))

    def __get_shorest_distance_route(self, city_start: str, city_end: str):
        distances = []
        queue = [(city_start, [city_start])]

        while queue:
            (node, path) = queue.pop(0)
            for next_node in [e for e in self.__graph[node]]:
                if next_node.node == city_end:
                    distances.append(path + [next_node])
                else:
                    queue.append((next_node.node, path + [next_node]))

        return min([sum([d.weight for d in dt[1:]]) for dt in distances])

    def __get_trips(self, city_start: str, city_end: str, stop_count: int):

        queue = [(city_start, [city_start])]

        while queue:
            (node, path) = queue.pop(0)
            for next_node in [e for e in self.__graph[node]]:
                if next_node.node == city_end:
                    if len(path[1:] + [next_node]) <= stop_count:
                        yield path + [next_node]
                else:
                    queue.append((next_node.node, path + [next_node]))
