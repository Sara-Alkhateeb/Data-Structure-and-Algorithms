class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        return new_node.value

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        popped_node = self.top
        self.top = self.top.next
        popped_node.next = None
        return popped_node.value
    
    def is_empty(self):
        return self.top is None
    
    def max_stack(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        max_item = self.top.value
        self.pop()

        while not self.is_empty():
            if self.top.value > max_item:
                max_item = self.top.value
            self.pop()
        
        return max_item

stack1 = Stack()
stack1.push(10)
stack1.push(20)
stack1.push(30)
print(stack1.max_stack())  # Output: 30
stack1.push(100)
stack1.push(20)
stack1.push(30)
print(stack1.max_stack()) 
stack1.push(100)
stack1.push(200)
stack1.push(30)
print(stack1.max_stack())  # Output: 100
stack1.max_stack()



