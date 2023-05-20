import pytest
from trees.trees import Binary_Tree, BinarySearchTree, Node

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


def test_instantiation_empty_tree():
    tree = BinarySearchTree()
    assert tree.root is None

def test_instantiation_single_node_tree():
    tree = BinarySearchTree()
    tree.add(5)
    assert tree.root is not None
    assert tree.root.value == 5
    assert tree.root.left is None
    assert tree.root.right is None

def test_add_children_to_node():
    tree = BinarySearchTree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    assert tree.root.left.value == 3
    assert tree.root.right.value == 7


def test_pre_order_traversal():
    tested = B_tree.pre_order(B_tree.root)
    assert tested == ["A", "B", "D", "E", "C", "F"]

def test_in_order_traversal():
    tested = B_tree.in_order(B_tree.root)
    assert tested == ["D", "B", "E", "A", "F", "C"]

def test_post_order_traversal():
    tested = B_tree.post_order(B_tree.root)
    assert tested == ["D", "E", "B", "F", "C", "A"]

def test_contains_existing_value():
    tree = BinarySearchTree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    assert tree.contains(7) == True

def test_contains_non_existing_value():
    tree = BinarySearchTree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    assert tree.contains(10) == False


