def merge_sort(arr):
    """
    Sorts the input array using the merge sort algorithm.

    Parameters:
    - arr (list): The array to be sorted.

    Returns:
    - None: The input array is sorted in place.
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        merge(left, right, arr)


def merge(left, right, arr):
    """
    Merges two sorted subarrays into a single sorted array.

    Parameters:
    - left (list): The left subarray.
    - right (list): The right subarray.
    - arr (list): The original array to be updated with the merged elements.

    Returns:
    - None: The input array is updated with the merged elements.
    """
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    if i == len(left):
        arr[k:] = right[j:]
    else:
        arr[k:] = left[i:]

# arr = [8,4,23,42,16,15]
arr= [2,3,4,52,8,5,15,9]
merge_sort(arr)
print(arr)