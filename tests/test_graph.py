import pytest
from graph.graph import Graph, Node, Edge

def test_empty_graph_size():
    graph = create_empty_graph()
    assert graph.size() == 0

def test_graph_size_after_adding_node():
    graph = create_empty_graph()
    node1 = add_node_to_graph(graph, "A")
    assert graph.size() == 1

def test_node_neighbors_empty():
    graph = create_empty_graph()
    node1 = add_node_to_graph(graph, "A")
    assert graph.get_neighbors(node1) == []

def test_add_edge_to_nonexistent_node():
    graph = create_empty_graph()
    node1 = add_node_to_graph(graph, "A")
    result = add_edge_to_nonexistent_node(graph, node1, Node("B"))
    assert result == "This node does not exist"

def test_node_neighbors():
    graph = create_empty_graph()
    node1 = add_node_to_graph(graph, "A")
    node2 = add_node_to_graph(graph, "B")
    add_edge_between_nodes(graph, node1, node2, 5)
    neighbors_node1 = [edge.vertex.value for edge in graph.get_neighbors(node1)]
    assert neighbors_node1 == ["B"]

def test_graph_size_after_adding_nodes_and_edges():
    graph = create_empty_graph()
    node1 = add_node_to_graph(graph, "A")
    node2 = add_node_to_graph(graph, "B")
    add_edge_between_nodes(graph, node1, node2, 5)
    assert graph.size() == 2

def test_graph_string_representation():
    graph = create_empty_graph()
    node1 = add_node_to_graph(graph, "A")
    node2 = add_node_to_graph(graph, "B")
    add_edge_between_nodes(graph, node1, node2, 5)
    expected_output = "A -> B(5) -> \nB -> A(5) -> \n"
    assert str(graph) == expected_output

def create_empty_graph():
    return Graph()

def add_node_to_graph(graph, value):
    return graph.add_node(value)

def add_edge_to_nonexistent_node(graph, node1, node2):
    return graph.add_edge(node1, node2)

def add_edge_between_nodes(graph, node1, node2, weight):
    graph.add_edge(node1, node2, weight)


