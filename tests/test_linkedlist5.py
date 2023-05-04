import pytest
from reversedLL.reversedLL import LinkedList 

#Test case 1: Test empty linked list
def test_reversed_LL_case1():
    ll = LinkedList()
    ll.reversed_LL()
    assert str(ll) == "Empty LinkedList"

#Test case 2: Test linked list with one node
def test_reversed_LL_case2():
    ll = LinkedList()
    ll.append(1)
    ll.reversed_LL()
    assert str(ll) == "{ 1 } -> NULL"

#Test case 3: Test linked list with multiple nodes
def test_reversed_LL_case3():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.reversed_LL()
    assert str(ll) == "{ 3 } -> { 2 } -> { 1 } -> NULL"

#Test case 4: Test linked list with identical nodes
def test_reversed_LL_case4():
    ll = LinkedList()
    ll.append(1)
    ll.append(1)
    ll.append(1)
    ll.reversed_LL()
    assert str(ll) == "{ 1 } -> { 1 } -> { 1 } -> NULL"

#Test case 5: Test linked list with negative numbers
def test_reversed_LL_case5():
    ll = LinkedList()
    ll.append(-1)
    ll.append(-2)
    ll.append(-3)
    ll.reversed_LL()
    assert str(ll) == "{ -3 } -> { -2 } -> { -1 } -> NULL"

