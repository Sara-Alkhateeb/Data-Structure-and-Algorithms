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