import pytest
from sorting.insertion.InsertionSort import insertion_sort


def test_insertion_sort():
    unsorted_array = [8, 4, 23, 42, 16, 15]
    expected_sorted_array = [4, 8, 15, 16, 23, 42]
    sorted_array = insertion_sort(unsorted_array)
    assert sorted_array == expected_sorted_array


