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

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        popped_node = self.top
        self.top = self.top.next
        popped_node.next = None
        return popped_node.value

    def peek(self):

        if self.is_empty():
            raise Exception("Stack is empty")
        return self.top.value

    def is_empty(self):
        return self.top is None
class Queue:
    def __init__(self):
        self.front = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = new_node
            self.back = new_node
        else:
            self.back.next = new_node
            self.back = new_node

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        dequeued_node = self.front
        self.front = self.front.next
        dequeued_node.next = None
        if self.front is None:
            self.back = None
        return dequeued_node.value

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.front.value

    def is_empty(self):
        return self.front is None
