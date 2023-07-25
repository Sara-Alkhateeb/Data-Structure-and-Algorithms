def is_connected(graph, node1, node2):
    if node1 not in graph or node2 not in graph:
        return False

    visited = set()
    queue = [node1]

    while queue:
        current_node = queue.pop(0)

        if current_node == node2:
            return True

        visited.add(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.append(neighbor)

    return False

# Example usage:
graph = {
        'A': ['B', 'C'],
        'B': ['D', 'A'],
        'C': ['A', 'D'],
        'D': ['B', 'C', 'F'],
        'E': ['F'],
        'F': ['E', 'G'],
        'G': ['F']
    }

# print(is_connected(graph, 'D', 'E'))  # Output: True
print(is_connected(graph, 'D', 'G'))  # Output: True


