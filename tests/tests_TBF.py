import pytest
from TBF.breath_first import Node, breadth_first

def test_breadth_first_traversal():
    # Create a tree for testing
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    # Perform breadth-first traversal
    result = breadth_first(root)

    # Check if the result matches the expected output
    assert result == [1, 2, 3, 4, 5, 6, 7]

def test_breadth_first_empty_tree():
    # Test an empty tree
    result = breadth_first(None)
    assert result == "Empty tree"


def test_breadth_first_single_node_tree():
    # Test a tree with a single node
    root = Node(1)
    result = breadth_first(root)
    assert result == [1]

def test_breadth_first_left_skewed_tree():
    # Test a left-skewed tree
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(3)
    root.left.left.left = Node(4)
    result = breadth_first(root)
    assert result == [1, 2, 3, 4]


def test_breadth_first_right_skewed_tree():
    # Test a right-skewed tree
    root = Node(1)
    root.right = Node(2)
    root.right.right = Node(3)
    root.right.right.right = Node(4)
    result = breadth_first(root)
    assert result == [1, 2, 3, 4]