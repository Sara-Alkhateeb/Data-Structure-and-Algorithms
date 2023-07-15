class Node:
    def __init__(self, value=None):
        """
        Initialize a Node object.

        Args:
            value: The value to be stored in the node.
        """
        self.value = value

    def __str__(self):
        """
        Return the string representation of the node's value.
        """
        return str(self.value)


class Edge:
    def __init__(self, vertex, weight=0):
        """
        Initialize an Edge object.

        Args:
            vertex: The vertex connected by the edge.
            weight: The weight of the edge (default is 0).
        """
        self.vertex = vertex
        self.weight = weight


class Graph:
    def __init__(self):
        """
        Initialize an empty Graph object with an adjacency list.
        """
        self.adj_list = {}

    def add_node(self, value):
        """
        Add a node to the graph with the given value.

        Args:
            value: The value of the node to be added.

        Returns:
            The newly added node.
        """
        new_vertex = Node(value)
        self.adj_list[new_vertex] = []
        return new_vertex

    def add_edge(self, node1, node2, weight=0):
        """
        Add an edge between two nodes in the graph.

        Args:
            node1: The first node to connect.
            node2: The second node to connect.
            weight: The weight of the edge (default is 0).

        Returns:
            None if either node does not exist in the graph.
        """
        if node1 not in self.adj_list.keys() or node2 not in self.adj_list.keys():
            return "This node does not exist"

        edge1 = Edge(node2, weight)
        self.adj_list[node1].append(edge1)

        edge2 = Edge(node1, weight)
        self.adj_list[node2].append(edge2)

    def get_vertices(self):
        """
        Get all the vertices in the graph.

        Returns:
            A collection of all vertices in the graph.
        """
        return self.adj_list.keys()

    def get_neighbors(self, vertex):
        """
        Get the neighbors of a given vertex.

        Args:
            vertex: The vertex to retrieve neighbors for.

        Returns:
            A collection of edges connected to the given vertex.
        """
        if vertex in self.adj_list:
            return self.adj_list[vertex]
        else:
            return []

    def size(self):
        """
        Get the total number of vertices in the graph.

        Returns:
            The number of vertices in the graph.
        """
        return len(self.adj_list)

    def __str__(self):
        """
        Return the string representation of the graph.

        Returns:
            The graph representation as a string.
        """
        output = ''
        for vertex in self.adj_list.keys():
            output += f'{vertex} -> '
            for edge in self.adj_list[vertex]:
                output += f'{edge.vertex}({edge.weight}) -> '
            output += '\n'
        return output


# Test the graph
graph = Graph()

a = graph.add_node("A")
b = graph.add_node("B")
c = graph.add_node("C")
d = graph.add_node("D")

graph.add_edge(a, b)
graph.add_edge(a, c)
graph.add_edge(c, b)
graph.add_edge(d, b)
graph.add_edge(d, c)

print('************************************')
print("Graph")
print(graph)
print('************************************')
for vertex in graph.get_vertices():
    print("vertex:", vertex)
print('************************************')
for vertex in graph.get_vertices():
    print("Neighbors of", vertex, ":", [edge.vertex.value for edge in graph.get_neighbors(vertex)], end="\n")
print('************************************')
print("Size of the graph:", graph.size())
print('************************************')
