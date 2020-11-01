class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [0] * capacity
        self.read = 0
        self.write = 0

    def enqueue(self, value):
        if (self.write + 1) % self.capacity == self.read:
            print('Queue is full')
            return

        self.data[(self.write + 1) % self.capacity] = value

    def dequeue(self):
        if self.empty():
            print('Queue is an empty')

        if self.read == self.write:
            return None

        val = self.data[self.read]
        self.read = (self.read + 1) % self.capacity
        return val

    def empty(self):
        return self.read == self.write

    def full(self):
        return self.write + 1 == self.read

