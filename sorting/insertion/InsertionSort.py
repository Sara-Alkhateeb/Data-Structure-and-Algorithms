
def insertion_sort(unsortedArr):
        """
        Sorts an array using the Insertion Sort algorithm.

        Args:
        unsortedArr (list): The unsorted array.

        Returns:
        list: The sorted array.

        """
        for i in range (1, len(unsortedArr)):
            n = i
            while unsortedArr[n-1]> unsortedArr[n] and n> 0:
                unsortedArr[n-1], unsortedArr[n] = unsortedArr[n], unsortedArr[n-1]
                n-= 1
        return unsortedArr

unsorted_array = [8, 4, 23, 42, 16, 15]
sorted_array = insertion_sort(unsorted_array)
print(sorted_array)

    
