from graph_breadth_first.graph_breadth_first import Node, breadth_first

def test_empty_graph():
    graph = Node("A")
    result = breadth_first(graph)
    assert [node.value for node in result] == ["A"]

def test_single_node():
    graph = Node("A")
    result = breadth_first(graph)
    assert [node.value for node in result] == ["A"]

def test_disconnected_graph():
    A = Node("A")
    B = Node("B")
    C = Node("C")
    A.edges = [B]
    C.edges = []
    result = breadth_first(A)
    assert set([node.value for node in result]) == {"A", "B"}

def test_linear_graph():
    A = Node("A")
    B = Node("B")
    C = Node("C")
    D = Node("D")
    E = Node("E")
    A.edges = [B]
    B.edges = [C]
    C.edges = [D]
    D.edges = [E]
    result = breadth_first(A)
    assert [node.value for node in result] == ["A", "B", "C", "D", "E"]

def test_complete_graph():
    A = Node("A")
    B = Node("B")
    C = Node("C")
    D = Node("D")
    A.edges = [B, C, D]
    B.edges = [A, C, D]
    C.edges = [A, B, D]
    D.edges = [A, B, C]
    result = breadth_first(A)
    assert set([node.value for node in result]) == {"A", "B", "C", "D"}


