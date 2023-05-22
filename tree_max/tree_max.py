class Node():
   def __init__(self, value):
      """
        Initialize a new node with the given value.

        Args:
            value: The value to assign to the node.
      """
      self.value =value
      self.left= None
      self.right = None

class Binary_Tree ():
    def __init__(self):
        """
        Initialize an empty binary tree.
        """
        self.root=None
    
    def find_maximum_value(self):
        """
    Find the maximum value stored in the binary tree.

    Returns:
        The maximum value found in the binary tree.
        or
        ValueError: If the binary tree is empty.

        """
        if self.root is None:
            return ("The binary tree is empty.")

        max_value = None  # Initialize the maximum value as None

        stack = [self.root]

        while stack:
            node = stack.pop()
            value = int(node.value)

            # Update the maximum value if it is None or the current node value is greater
            if max_value is None or value > max_value:
                max_value = value

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return max_value



    
B_tree = Binary_Tree()

node1=Node("2")
B_tree.root=node1

node2=Node("7")
node1.left=node2

node3=Node("5")

node1.right=node3

node3.left=Node("9")

node2.left=Node("2")

node4 =Node("6")
node2.right=node4

node4.left=Node("5")

node4.left=Node("11")


# B_tree.root = Node(555)
# B_tree.root.left = Node(3)
# B_tree.root.right = Node(81)
# B_tree.root.left.left = Node(9)
# B_tree.root.left.right = Node(2)

print(B_tree.find_maximum_value())

