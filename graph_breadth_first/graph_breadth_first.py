from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []

# Create a graph
A = Node("Pandora")
B = Node("Arendelle")
C = Node("Metroville")
D = Node("Monstroplolis")
E = Node("Naboo")
F = Node("Narnia")

A.edges = [B]
B.edges = [A, C , D]
C.edges = [F]
D.edges = [ B , C , F]
E.edges = [F , D]
F.edges = [E , C, D]

def breadth_first(vertex):
    nodes = []
    breadth = deque()
    visited = set()

    breadth.append(vertex)
    visited.add(vertex)

    while breadth:
        front = breadth.popleft()
        nodes.append(front)

        for child in front.edges:
            if child not in visited:
                visited.add(child)
                breadth.append(child)
    return nodes

# Test the breadth_first function
result = breadth_first(A)
print("Nodes visited in breadth-first order:", [node.value for node in result])
