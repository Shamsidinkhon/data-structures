class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        if self.tail is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

    def dequeue(self):
        if not self.head:
            return None
        else:
            val = self.head.val
            self.head = self.head.next
            return val

    def empty(self):
        return not self.head and not self.tail


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
