
# from LLInsertion.node import Node
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
    
    def append(self, value):
        """
        This method inorder to adds a new node with a specified value to the end of the list
        
        """
        node = Node(value)
        if self.head is None:
         self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node


    def insert_before(self, value, new_value):
        if self.head is None:
            print(f"{value} not found in the list")
            return

        if self.head.value == value:
            self.insert_first(new_value)
            return

        current = self.head.next
        prev = self.head

        while current is not None:
            if current.value == value:
                node = Node(new_value)
                node.next = current
                prev.next = node
                return
            prev = current
            current = current.next

        print(f"{value} not found in the list")

    def insert_after(self, value, new_value):
        if self.head is None:
            print(f"{value} not found in the list")
            return

        current = self.head
        while current is not None:
            if current.value == value:
                node = Node(new_value)
                node.next = current.next
                current.next = node
                return
            current = current.next

        print(f"{value} not found in the list")

        

ll = LinkedList()

ll.insert(3)
ll.insert(5)
ll.insert(2)
ll.insert(1)
ll.insert(6)
ll.insert(9)

# print(ll.includes(9))
ll.append(0)
ll.insert(10)
ll.append(20)
ll.insert_before(0,1)

# ll.insert_before(7,1)
ll.insert_after(7,1)
ll.insert_after(20,30)
ll.append(20)

print(ll)  # "1 -> 2 -> 3 -> None"
# print(ll.includes(2))  # True
# print(ll.includes(4))  # False

# print(ll)