
"""This module defines a linked list data structure using two classes: Node and LinkedList."""


""""
The Node class represents a single node in the linked list, with two attributes:
value: The value stored in the node.
next: A reference to the next node in the linked list.
Methods: Node.__init__(self, value): Initializes a Node instance with a value and a reference to the next node.
Input: value (any type): The value to be stored in the node.
Output :None"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

""""
The LinkedList class represents the linked list itself, with one attribute:
head: A reference to the first node in the linked list.

Methods:
- LinkedList.__init__(self): Initializes an empty LinkedList instance with a null head node.
- LinkedList.__repr__(self): Returns a string representation of the linked list, with each node's value separated by an arrow.
- LinkedList.insert(self, value): Inserts a new node with the given value at the beginning of the linked list.
- LinkedList.includes(self, value): Checks if the linked list contains a node with the given value.
- LinkedList.__str__(self): Returns a string representation of the linked list, with each node's value enclosed in braces and separated by an arrow, and with the last node pointing to null.
Input:
value (any type): The value to be inserted into the linked list (for insert method).
value (any type): The value to be searched in the linked list (for includes method).
Output:
__repr__ returns a string representation of the linked list.
insert and includes methods do not return any value.
__str__ returns a string representation of the linked list.
"""
class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):

        output = ""
        
        if self.head is None:
            output = "Empty LinkedList"
        else:
            current = self.head
            while(current):
                output += f'{current.value} --> '
                current = current.next
            
            output += " None"
        return output
    
    def insert(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def includes(self,value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False
        
    def __str__(self):
        output = ""
        if self.head is None:
            output = "Empty LinkedList"
        else:
            current = self.head
            while(current):
                output += f'{{ {current.value} }} -> '
                current = current.next

            output += "NULL"
        return output

ll = LinkedList()

ll.insert(3)
ll.insert(5)
ll.insert(2)

print(ll) 

print( f"Is number 5 exist : {ll.includes(5)}") 
print(f"Is number 4 exist : {ll.includes(4)}") 