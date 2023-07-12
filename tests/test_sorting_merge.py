import pytest
from sorting.merge.merge import merge_sort


def test_merge_sort():
    unsorted_array = [8, 4, 23, 42, 16, 15]
    expected_sorted_array = [4, 8, 15, 16, 23, 42]
    merge_sort(unsorted_array)
    assert unsorted_array == expected_sorted_array