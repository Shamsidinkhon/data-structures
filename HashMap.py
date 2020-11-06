class HashMap:
    def __init__(self):
        self._growth = 2
        self._shrink = 4
        self._capacity = self._growth
        self._storage = [None] * self._capacity
        self._length = 0

    def hash(self, k):
        if k is int:
            return k % self._capacity
        return sum(ord(c) for c in k) % self._capacity

    def add(self, key, value):
        if self._length == self._capacity:
            self._capacity = self._growth * self._capacity
            new_storage = [None] * self._capacity
            for i in range(self._length):
                new_storage[self.hash(key)] = self._storage[i]
            self._storage = new_storage

        self._storage[self.hash(key)] = value
        self._length += 1

    def exists(self, key):
        return not self._storage[self.hash(key)]

    def remove(self, key):
        self._storage[self.hash(key)] = None
        self._length -= 1
        if self._length == self._capacity / self._shrink:
            self._capacity = self._capacity / self._shrink
            new_storage = [None] * self._capacity
            for i in range(self._length):
                if not self._storage[i]:
                    new_storage[self.hash(key)] = self._storage[i]
                self._storage = new_storage



