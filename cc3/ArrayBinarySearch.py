"""
    BinarySearch(arr, search_key) -> int

    Perform a binary search on a sorted array to find the index of the first occurrence
    of the search key. If the search key is not found, return -1.

    Parameters:
    arr (list): A sorted list of elements to search.
    search_key: The value to search for in the list.

    Returns:
    int: The index of the first occurrence of the search key in the list, or -1 if
     the search key is not found.
"""

def BinarySearch (arr, search_key):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == search_key:
            return mid

        elif arr[mid] < search_key:
            left = mid + 1

        else:
            right = mid - 1

    return -1
if (__name__=="__main__"):
 print(BinarySearch ( [1, 2, 3, 4, 5, 6, 7], 9))