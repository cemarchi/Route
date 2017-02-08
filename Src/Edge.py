class Edge:
    def __init__(self, node: str, weight: int):
        self.__node = node
        self.__weight = weight

    def __eq__(self, other):
        return self.__node == other.node and self.__weight == other.weight

    @property
    def node(self):
        return self.__node

    @node.setter
    def node(self, value):
        self.__node = value

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        self.__weight = value
