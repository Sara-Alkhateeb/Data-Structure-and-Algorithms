from cc3.ArrayBinarySearch import BinarySearch 

def test_arr1():
    actual=BinarySearch([42,4,5,13,42], 10)
    expected=-1
    assert actual == expected

def test_evenArr():
    actual=BinarySearch([2,1,5,-8], 1)
    expected=1
    assert actual == expected