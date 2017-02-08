from Src.Edge import Edge


class DirectedGraph:
    @staticmethod
    def create_graph(routes: str):
        graph = {}
        routes = routes.replace(' ', '')

        for r in routes.split(','):

            if r[0] in graph:
                graph[r[0]].append(Edge(r[1], int(r[2:])))
            else:
                graph[r[0]] = [Edge(r[1], int(r[2:]))]

        return graph
