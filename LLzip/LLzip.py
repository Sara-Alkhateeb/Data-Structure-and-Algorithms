# from LLzip.node import Node

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

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
     
        #This method inorder to adds a new node with a specified value to the end of the list

    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

def zip_lists(list1, list2):
    if not list1.head:
        return list2.head
    if not list2.head:
        return list1.head

    result = LinkedList()
    current1 = list1.head
    current2 = list2.head

    while current1 and current2:
        result.append(current1.value)
        result.append(current2.value)

        current1 = current1.next
        current2 = current2.next

    # Add any remaining nodes from list1
    while current1:
        result.append(current1.value)
        current1 = current1.next

    # Add any remaining nodes from list2
    while current2:
        result.append(current2.value)
        current2 = current2.next

    return result.head

# Create two linked lists
list1 = LinkedList()
list1.append(1)
list1.append(3)
list1.append(5)

list2 = LinkedList()
list2.append(2)
list2.append(4)
list2.append(6)

# Zip the two lists together
result = LinkedList()
result.head = zip_lists(list1, list2)

# Print the result
print (result)



