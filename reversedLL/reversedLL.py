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
    
    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
        
    def reversed_LL(self):
        prev = None
        curr = self.head
        next = None
        
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        self.head = prev

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


# if __name__== "__main__":

ll = LinkedList()
ll.append(3)
ll.append(5)
ll.append(2)

print("Original Linked List: ", ll)

ll.reversed_LL()

print("Reversed Linked List: ", ll)
