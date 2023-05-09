class Node:
    def __init__(self, value):
        """
        Initializes a new Node with the given value.

        Parameters:
        - value: The value to be stored in the Node.
        """
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        """
        Initializes a new empty Stack.
        """
        self.top = None

    def push(self, value):
        """
        Adds a new Node with the given value to the top of the Stack.

        Parameters:
        -value: The value to be added to the Stack.
        """
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """
        Removes and returns the value of the Node at the top of the Stack.

        Raises an Exception if the Stack is empty.
        """
        if self.is_empty():
            raise Exception("Stack is empty")
        popped_node = self.top
        self.top = self.top.next
        popped_node.next = None
        return popped_node.value

    def peek(self):
        """
        Returns the value of the Node at the top of the Stack without removing it.

        Raises an Exception if the Stack is empty.
        """
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.top.value

    def is_empty(self):
        """
        Returns True if the Stack is empty, and False otherwise.
        """
        return self.top is None

class Queue:
    def __init__(self):
        """
        Initializes a new empty Queue.
        """
        self.front = None
        self.back = None

    def enqueue(self, value):
        """
        Adds a new Node with the given value to the back of the Queue.

        Parameters:
        - value: The value to be added to the Queue.
        """
        new_node = Node(value)
        if self.is_empty():
            self.front = new_node
            self.back = new_node
        else:
            self.back.next = new_node
            self.back = new_node

    def dequeue(self):
        """
        Removes and returns the value of the Node at the front of the Queue.

        Raises an Exception if the Queue is empty.
        """
        if self.is_empty():
            raise Exception("Queue is empty")
        dequeued_node = self.front
        self.front = self.front.next
        dequeued_node.next = None
        if self.front is None:
            self.back = None
        return dequeued_node.value

    def peek(self):
        """
        Returns the value of the Node at the front of the Queue without removing it.

        Raises an Exception if the Queue is empty.
        """
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.front.value

    def is_empty(self):
        """
        Returns True if the Queue is empty, and False otherwise.
        """
        return self.front is None

