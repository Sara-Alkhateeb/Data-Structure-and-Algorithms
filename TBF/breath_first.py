class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def breadth_first(tree):
    """Performs breadth-first traversal on a binary tree.

    Args:
        tree (Node): The root node of the binary tree.

    Returns:
        list: A list containing the values of the nodes visited in breadth-first order.

    Raises:
        None

    """
    if tree is None:
        return "Empty tree"

    result = []
    queue = []
    queue.append(tree)

    while len(queue) > 0:
        node = queue.pop(0)
        result.append(node.value)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return result

# Define the nodes
root = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

# Build the tree
root.left = node2
root.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

# Call the breadth_first function
result = breadth_first(root)

# Print the result
print(result)
