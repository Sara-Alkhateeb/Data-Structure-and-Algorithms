import pytest
from graph_depth_first.depth_first import Graph 

def test_depth_first_traversal():
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
    traversal_result = graph.depth_first(root)

    expected_result = [node_A, node_B, node_C, node_G, node_D, node_E, node_H, node_F]
    assert traversal_result == expected_result

def test_depth_first_one_node():
    graph = Graph()
    node_A = graph.add_node("A")
   
    root = node_A
    traversal_result = graph.depth_first(root)

    expected_result = [node_A]
    assert traversal_result == expected_result