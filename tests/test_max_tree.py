import pytest
from tree_max.tree_max import Binary_Tree, Node

def test_find_maximum_value_empty_tree():
    B_tree = Binary_Tree()
    assert B_tree.find_maximum_value() == "The binary tree is empty."

def test_find_maximum_value():
    B_tree = Binary_Tree()
    B_tree.root = Node("2")
    B_tree.root.left = Node("7")
    B_tree.root.right = Node("5")
    B_tree.root.right.left = Node("9")
    B_tree.root.left.left = Node("2")
    B_tree.root.left.right = Node("6")
    B_tree.root.left.right.left = Node("5")
    B_tree.root.left.right.right = Node("11")
    assert B_tree.find_maximum_value() == 11

def test_find_maximum_value_single_node_tree():
    B_tree = Binary_Tree()
    B_tree.root = Node("5")
    assert B_tree.find_maximum_value() == 5

def test_find_maximum_value_negative_numbers():
    B_tree = Binary_Tree()
    B_tree.root = Node("-2")
    B_tree.root.left = Node("-7")
    B_tree.root.right = Node("-5")
    B_tree.root.right.left = Node("-9")
    B_tree.root.left.left = Node("-2")
    B_tree.root.left.right = Node("-6")
    B_tree.root.left.right.left = Node("-5")
    B_tree.root.left.right.right = Node("-11")
    assert B_tree.find_maximum_value() == -2

