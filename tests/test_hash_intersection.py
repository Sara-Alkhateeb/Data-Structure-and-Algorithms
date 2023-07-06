import pytest
from tree_intersection.tree_intersection import tree_intersection


def test_tree_intersection():
    tree1 = [1, 2, 3, 4, 5, 6, 7]
    tree2 = [1, 2, 3, 4, 5, 6, 7]
    assert tree_intersection(tree1, tree2) == {1, 2, 3, 4, 5, 6, 7}
    tree1 = [1, 2, 3, 4, 5, 6, 7]
    tree2 = [1, 2, 3, 4, 5, 6, 8]
    assert tree_intersection(tree1, tree2) == {1, 2, 3, 4, 5, 6}
    tree1 = [1, 2, 3, 4, 5, 6, 7]
    tree2 = [8, 9, 10, 11, 12, 13, 14]
    assert tree_intersection(tree1, tree2) == set()