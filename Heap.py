class MaxHeap:
    def __init__(self):
        self.tree = []

    def insert(self, val):
        self.tree.append(val)
        self.sift_up(len(self.tree) - 1)

    def sift_up(self, index):
        parent = (index - 1) // 2
        if parent < 0:
            return
        if self.tree[parent] < self.tree[index]:
            self.tree[parent], self.tree[index] = self.tree[index], self.tree[parent]
        self.sift_up(parent)

    def get_max(self):
        return self.tree[0] if not self.is_empty() else None

    def get_size(self):
        return len(self.tree)

    def is_empty(self):
        return self.get_size() == 0

    def extract_max(self):
        if not self.is_empty():
            self.tree[0], self.tree[-1] = self.tree[-1], self.tree[0]
            el = self.tree.pop()
            self.sift_down(0)
            return el
        return None

    def sift_down(self, index):
        left_child = 2 * index + 1

        if left_child >= self.get_size():
            return

        if left_child + 1 < self.get_size() and self.tree[left_child] < self.tree[left_child + 1]:
            left_child += 1

        if self.tree[left_child] > self.tree[index]:
            self.tree[left_child], self.tree[index] = self.tree[index], self.tree[left_child]
            self.sift_down(left_child)

    def remove(self, index):
        if not self.is_empty() and 0 <= index < self.get_size():
            self.tree[index], self.tree[-1] = self.tree[-1], self.tree[index]
            self.tree.pop()
            self.sift_down(index)

    def heapify(self, input_array):
        self.tree = input_array
        for i in range(self.get_size() // 2, -1, -1):
            self.sift_down(i)

    def heap_sort(self, input_array):
        self.heapify(input_array)
        sorted_array = []
        while self.tree:
            sorted_array.append(self.extract_max())
        return sorted_array


h = MaxHeap()
# Checking the value at top
print("Value at top:", h.get_max())
# pushing elements into heap
h.insert(1)
h.insert(11)
print("Value at top:", h.get_max())
# Deleting the root node
print("Root popped:", h.extract_max())
h.insert(7)
h.insert(9)
h.insert(15)
print("Value at top:", h.get_max())
print("Root popped:", h.extract_max())
print("Value at top:", h.get_max())
print("Testing heapify and heap sorting by DESC: Array[54,1,84,2,8,54,77]")
print(h.heap_sort([54, 1, 84, 2, 8, 54, 77]))
