class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class Stack:
    def __init__(self):
        """Initializes an empty stack."""
        self.top = None

    def push(self, value):
        """Adds a new node with the given value to the top of the stack."""
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """Removes the top node from the stack and returns its value."""
        if self.is_empty():
            raise Exception("Stack is empty")
        popped_node = self.top
        self.top = self.top.next
        popped_node.next = None
        return popped_node.value

    def peek(self):
        """Returns the value of the top node without modifying the stack."""
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.top.value

    def is_empty(self):
        """Returns True if the stack is empty and False otherwise."""
        return self.top is None


class PseudoQueue:
    def __init__(self):
        """Initializes an empty pseudo queue with two empty stacks."""
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
        """Adds a new value to the pseudo queue, using the push method of the first stack."""
        self.stack1.push(value)

    def dequeue(self):
        """Removes and returns the oldest value from the pseudo queue, using the pop method of the second stack. 
        If the second stack is empty, 
        all the values from the first stack are transferred to the second stack using the pop method of the first stack."""
        if self.stack1.is_empty() and self.stack2.is_empty():
            raise Exception("PseudoQueue is empty")
        elif self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    
    def __str__(self):
        # if self.stack1.is_empty():
        #     return "PseudoQueue is empty"
        items = []
        current = self.stack1.top
        while current:
            items.append(f"[{current.value}]")
            current = current.next
        return "->".join(items)
    

queue = PseudoQueue()
queue.enqueue(20)
queue.enqueue(15)
queue.enqueue(10)
print(queue)
queue.enqueue(5)
print(queue)
value1=queue.dequeue()
print(value1)
value2=queue.dequeue()
print(value2)






