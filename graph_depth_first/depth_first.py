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

    def depth_first(graph, root):
        """
        Perform depth-first traversal starting from the specified node.

        Args:
            graph (Graph): The graph object to perform depth-first traversal on.
            root (Node): The node to start the depth-first traversal from.

        Returns:
            list: A collection of nodes in their pre-order depth-first traversal order.
        """
        visited = set()
        result = []

        def dfs(node):
            visited.add(node)
            result.append(node)

            for edge in graph.get_neighbors(node):
                neighbor = edge.vertex
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(root)
        return result

# Example Usage:
if __name__ == "__main__":
    graph = Graph()
    node_A = graph.add_node("A")
    node_B = graph.add_node("B")
    node_C = graph.add_node("C")
    node_D = graph.add_node("D")
    node_E = graph.add_node("E")
    node_F = graph.add_node("F")
    node_G = graph.add_node("G")
    node_H = graph.add_node("H")

    graph.add_edge(node_A, node_B)
    graph.add_edge(node_A, node_D)
    graph.add_edge(node_B, node_C)
    graph.add_edge(node_B, node_D)
    graph.add_edge(node_C, node_G)
    graph.add_edge(node_D, node_A)
    graph.add_edge(node_D, node_B)
    graph.add_edge(node_D, node_E)
    graph.add_edge(node_D, node_H)
    graph.add_edge(node_D, node_F)
    root = node_A
    traversal_result = Graph.depth_first(graph, root)

    print("Output:", ", ".join(str(node) for node in traversal_result))
