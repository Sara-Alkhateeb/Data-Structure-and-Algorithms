import pytest
from LLkth.LLKth import LinkedList

# Test kth_from_end with k = 0
def test_kth_from_end_k_zero(ll):
    expected = "20"
    actual = str(ll.kth_from_end(0))
    assert expected == actual

# Test kth_from_end with k = 2
def test_kth_from_end_k_two(ll):
    expected = "4"
    actual = str(ll.kth_from_end(2))
    assert expected == actual

# Test kth_from_end with k greater than length of linked list
def test_kth_from_end_k_greater_than_length(ll):
    expected = "Invalid value of k"
    actual = str(ll.kth_from_end(15))
    assert expected == actual

def test_kth_from_end_k_greater_nigtev_num(ll):
    expected = "Invalid value of k"
    actual = str(ll.kth_from_end(-10))
    assert expected == actual

def test_kth_equal_length(ll):
    expected = "1"
    actual = str(ll.kth_from_end(5))
    assert expected == actual

# Test kth_from_end with empty linked list
# def test_kth_from_end_empty_linked_list():
#     ll = LinkedList()
#     expected = "Exception: Linked list is empty"
#     actual = (str(ll.kth_from_end(0)))
#     assert expected == actual

@pytest.fixture
def ll():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(20)

    return ll