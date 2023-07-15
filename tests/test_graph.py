import  pytest
from graph.graph import Graph , Node, Edge

def test_graph():
    graph = Graph()

    # Verify the size of the empty graph is 0
    assert graph.size() == 0

    # Add a single node to the graph
    node1 = graph.add_node("A")

    # Verify the size of the graph is 1 after adding a node
    assert graph.size() == 1

    # Verify the neighbors of a single node are empty
    assert graph.get_neighbors(node1) == []

    # Add an edge to a non-existent node
    result = graph.add_edge(node1, Node("B"))
    assert result == "This node does not exist"

    # Add a new node and an edge connecting the two nodes
    node2 = graph.add_node("B")
    graph.add_edge(node1, node2, 5)

    # Verify the neighbors of node1 after adding an edge
    neighbors_node1 = [edge.vertex.value for edge in graph.get_neighbors(node1)]
    assert neighbors_node1 == ["B"]

    # Verify the neighbors of node2 after adding an edge
    neighbors_node2 = [edge.vertex.value for edge in graph.get_neighbors(node2)]
    assert neighbors_node2 == ["A"]

    # Verify the size of the graph after adding nodes and edges
    assert graph.size() == 2

    # Verify the string representation of the graph after adding nodes and edges
    expected_output = "A -> B(5) -> \nB -> A(5) -> \n"
    assert str(graph) == expected_output


# Run the test case
test_graph()

