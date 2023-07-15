# class 32 - Tree intersection

Find common values in 2 binary trees.

## Whiteboard Process
<!-- Embedded whiteboard image -->
![whiteboard](../assest/treeintersection.jpg)

## Approach & Efficiency

time: O(n + m) because we loop throw both of the trees once
space: O(n + m) because we created hashtable which will store the first tree values, and we have values values which can be the min(n, m) so in worse case it will be O(n + m)

## Solution
### [click here to tree intersection code](./tree_intersection.py)
### [click here to tree intersection Test code](../tests/test_hash_intersection.py)