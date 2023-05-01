import pytest
from LLzip.LLzip import LinkedList, zip_lists

# Test case 1 Lists have same length and values
def test_zip_lists_case1():
    list1 = LinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(5)

    list2 = LinkedList()
    list2.append(1)
    list2.append(3)
    list2.append(5)

    result = LinkedList()
    result.head = zip_lists(list1, list2)

    assert str(result) == "{ 1 } -> { 1 } -> { 3 } -> { 3 } -> { 5 } -> { 5 } -> NULL"


# Test case 2 Lists have different lengths
def test_zip_lists_case2():
    list1 = LinkedList()
    list1.append(1)
    list1.append(3)

    list2 = LinkedList()
    list2.append(2)
    list2.append(4)
    list2.append(6)

    result = LinkedList()
    result.head = zip_lists(list1, list2)

    assert str(result) == "{ 1 } -> { 2 } -> { 3 } -> { 4 } -> { 6 } -> NULL"

# Test case 3 One list is empty
def test_zip_lists_case3():
    list1 = LinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(5)

    list2 = LinkedList()

    result = LinkedList()
    result.head = zip_lists(list1, list2)

    assert str(result) == "{ 1 } -> { 3 } -> { 5 } -> NULL"
    
# Test case 4 Lists have same length, but different values
def test_zip_lists_case4():
    list1 = LinkedList()
    list1.append(1)

    list2 = LinkedList()
    list2.append(2)

    result = LinkedList()
    result.head = zip_lists(list1, list2)

    assert str(result) == "{ 1 } -> { 2 } -> NULL"

#Test case 5 Both lists are empty
def test_zip_lists_both_empty():
    list1 = LinkedList()
    list2 = LinkedList()
    result = LinkedList()
    result.head = zip_lists(list1, list2)
    assert str(result) == "Empty LinkedList"

