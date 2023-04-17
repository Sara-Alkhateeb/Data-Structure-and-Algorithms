# Linked-List
A linked list is a linear data structure in which each element, called a node, stores a value and a reference to the next node. This Code uses to insert an element into a linked list, create a new node with the value and link it to the previous node's reference. To check if a value is in the linked list, traverse the list by following the node references until find the value or reach the end of the list.

## Whiteboard Process
![](../class05%20whiteborad.png)


## Approach & Efficiency
## 1. Algorithm :
`Node class`
- Create a class called `Node` with attributes:
- `value` to store the value of the node
- `next` to store a reference to the next node in the list (initially None)

`LinkedList class`
- Create a class called LinkedList with attributes:
 
 head to store a reference to the first node in the list (initially None)
    Implement the following methods:
     __init__(self) to initialize the linked list with an empty head node
     __str__(self) to return a string representation of the linked list
     insert(self, value) to insert a new node with the given value at the beginning of the list
     includes(self, value) to check if a node with the given value is present in the list

- The insert method works as follows:

   Create a new Node object with the given value
   Set the next attribute of the new node to the current head of the list
   Set the head attribute of the list to the new node

- The includes method works as follows:

  Start at the head of the list
  While the current node is not None:
  If the value of the current node is equal to the given value, return True
  Move to the next node
  If the value is not found in the list, return False

## 2. BigO
   
Insert method:
Time Complexity: O(1)
Space Complexity: O(1)

includes method:
Time Complexity: O(n)
Space Complexity: O(1)

## Solution
### [click here to the LinkedList code](./linkedlist.py)
### [click here to the Test code](../tests/test_linkedlist.py)
### To run the code:
    -on your terminal follow these command:
       1. source .venv/bin/activate.
       2. pip install pytest.
       3. pytest.