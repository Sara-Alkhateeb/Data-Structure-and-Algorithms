from graph_breadth_first.graph_breadth_first import Node , breadth_first

def test_breadth_first():
    # Test 1: Empty Graph
    graph = Node("A")
    result = breadth_first(graph)
    assert [node.value for node in result] == ["A"], "Test Case 1 Failed"

    # Test 2: Single Node
    graph = Node("A")
    result = breadth_first(graph)
    assert [node.value for node in result] == ["A"], "Test Case 2 Failed"

    # Test 3: Disconnected Graph
    A = Node("A")
    B = Node("B")
    C = Node("C")
    A.edges = [B]
    C.edges = []
    result = breadth_first(A)
    assert set([node.value for node in result]) == {"A", "B"}, "Test Case 3 Failed"

    # Test 4: Linear Graph
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
    assert [node.value for node in result] == ["A", "B", "C", "D", "E"], "Test Case 4 Failed"

    # Test 5: Complete Graph
    A = Node("A")
    B = Node("B")
    C = Node("C")
    D = Node("D")
    A.edges = [B, C, D]
    B.edges = [A, C, D]
    C.edges = [A, B, D]
    D.edges = [A, B, C]
    result = breadth_first(A)
    assert set([node.value for node in result]) == {"A", "B", "C", "D"}, "Test Case 5 Failed"
