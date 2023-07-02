# MergeSort
## Merge sort is defined as a sorting algorithm that works by dividing an array into smaller subarrays, sorting each subarray, and then merging the sorted subarrays back together to form the final sorted array.

# Trace


![cc](./Assest/p1.png)
## Unsorted Array


![cc](./Assest/p2.png)
## Devied the array into 2 parts by /2 (left and right )


![cc](./Assest/p3.png)
## Devied the left array into 2 parts by /2 (left and right )


![cc](./Assest/p4.png)
## Devied the left of the left array into 2 parts by /2 (left and right )

![cc](./Assest/p5.png)
## Here, 8 is greater than 4 so indix 0 will be 4 and indix 1 will be 8.

![cc](./Assest/p6.png)
## Here, 23 is greater than 4 so indix 0 will be 4 and then compare 23 with 8 so indix 1 will be 8 finally indix 2 will be 23.


![cc](./Assest/p9.png)
## done from the left array.

![cc](./Assest/p10.png)
## Devied the right array into 2 parts by /2 (left and right )

![cc](./Assest/p11.png)
## Devied the left of the right array into 2 parts by /2 (left and right )

![cc](./Assest/p12.png)
## Here, 42 is greater than 16 so indix 0 will be 42 and indix 1 will be 16.


![cc](./Assest/p14.png)
## Here, 16 is greater than 15 so indix 0 will be 15 and then compare 16 with 42 so indix 1 will be 16 finally indix 2 will be 42.

![cc](./Assest/p15.png)
## Here, 15 is greater than 4 so indix 0 will be 4 and also 15 graeter than 8 so indix 1 will be 8 .


![cc](./Assest/p16.png)


![cc](./Assest/p17.png)
## Here, 23 is greater than 15 so indix 2 will be 15.

![cc](./Assest/p18.png)
## Here, 23 is greater than 16 so indix 3 will be 16.

![cc](./Assest/p19.png)
## Here, 42 is greater than 23 so indix 4 will be 23.
![cc](./Assest/p20.png)
## Here, the end of the right array.


    - Finally, the array is completely sorted.


## Link of the code
### [click here to the sortingMerge code](./merge.py)
### [click here to the sortingMerge test](../../tests/test_sorting_merge.py)