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
        self.stack_pre_order= []
        self.stack_in_order=[]
        self.stack_post_order=[]

    def pre_order(self, root):
        """
        Perform a pre-order traversal on the binary tree.

        Args:
            root: The root node of the tree or subtree to traverse.

        Returns:
            A list of values in the order encountered during pre-order traversal.
        """
        if root is None:
            return  None
        if root is not None:
           self.stack_pre_order.append(root.value)
        if root.left is not None:
            self.pre_order(root.left)
        if root.right is not None:
            self.pre_order(root.right)
        return self.stack_pre_order


    def in_order(self , root):
        """
        Perform an in-order traversal on the binary tree.

        Args:
            root: The root node of the tree or subtree to traverse.

        Returns:
            A list of values in the order encountered during in-order traversal.
        """
        if root is None:
            return  None
       
        if root.left is not None:
            self.in_order(root.left)
        if root is not None:
            self.stack_in_order.append(root.value)
        if root.right is not None:
            self.in_order(root.right)
        return self.stack_in_order
        
    def post_order(self, root):
        """
        Perform a post-order traversal on the binary tree.

        Args:
            root: The root node of the tree or subtree to traverse.

        Returns:
            A list of values in the order encountered during post-order traversal.
        """
        if root is None:
            return  None
        if root.left is not None:
            self.post_order(root.left)

        if root.right is not None:
            self.post_order(root.right)

        if root is not None:
            self.stack_post_order.append(root.value)
        return self.stack_post_order

class BinarySearchTree(Binary_Tree):
    def __init__ (self):
        """
        Initialize an empty binary search tree.
        """
        Binary_Tree.__init__(self)

    def add(self, value):
        """
        Add a new node with the given value to the binary search tree.

        Args:
            value: The value to add to the tree.
        """
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if value < current_node.value:
                    if current_node.left is None:
                        current_node.left = new_node
                        break
                    else:
                        current_node = current_node.left

                else:
                    if current_node.right is None:
                        current_node.right = new_node
                        break
                    else:
                        current_node = current_node.right

    def contains(self, value):
        """
        Check if the binary search tree contains a node with the given value.

        Args:
            value: The value to search for in the tree.

        Returns:
            True if the value is found, False otherwise.
        """
        current_node = self.root
        while current_node is not None:
            if value == current_node.value:
                return True
            elif value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False
        
         


bst = BinarySearchTree()
B_tree =Binary_Tree()

node1=Node("A")
B_tree.root=node1

node2=Node("B")
node1.left=node2

node3=Node("C")
node1.right=node3

node2.left=Node("D")
node2.right=Node("E")

node3.left=Node("F")


print(B_tree.pre_order(B_tree.root))
print("********************************")
print(B_tree.in_order(B_tree.root))
print("********************************")
print(B_tree.post_order(B_tree.root))

bst.add(50)
bst.add(300)
bst.add(21)
bst.add(11)
bst.add(5)
bst.add(15)

print(bst.pre_order(bst.root))
print(bst.in_order(bst.root))
print(bst.post_order(bst.root))

print(bst.contains(7))  # Output: False
print(bst.contains(15))  # Output: True

      
