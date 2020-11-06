class LinkedList:

    def __init__(self):
        self._head = None

    def set_head(self, head):
        self._head = head

    def empty(self):
        return self._head is None

    def size(self):
        count = 0
        node = self._head
        while node:
            count += 1
            node = node.next
        return count

    def value_at(self, index):
        node = self._head
        while index > 0:
            node = node.next
            index -= 1
        return node.val

    def push_front(self, value):
        node = Node(value)
        node.next = self._head
        self._head = node

    def pop_front(self):
        node = self._head
        self._head = self._head.next
        return node.val

    def push_back(self, value):
        node = Node(value)
        head = self._head
        while head.next:
            head = head.next
        head.next = node

    def pop_back(self):
        head = self._head
        while head.next and head.next.next:
            head = head.next
        node = head.next
        head.next = None
        return node.val

    def front(self):
        return self._head.val

    def back(self):
        head = self._head
        while head.next:
            head = head.next
        return head.val

    def insert(self, index, value):
        node = Node(value)
        if index == 0:
            node.next = self._head
            self._head = node
        else:
            head = self._head
            while index > 1:
                head = head.next
                index -= 1
            node.next = head.next
            head.next = node

    def erase(self, index):
        if index == 0:
            self._head = self._head.next
        else:
            head = self._head
            while index > 1:
                head = head.next
                index -= 1
            head.next = head.next.next

    def reverse(self):
        prev = None
        node = self._head

        while node:
            _next = node.next
            node.next = prev
            prev = node
            node = _next

        self._head = prev

    def value_n_from_end(self, n):
        prev = None
        node = self._head

        while node:
            _next = node.next
            node.next = prev
            prev = node
            node = _next

        while n > 0 and prev:
            prev = prev.next
            n -= 1

        return prev.val

    def remove_value(self, value):
        head = self._head
        index = 0
        while head:
            if head.val == value:
                self.erase(index)
                break
            head = head.next


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


_list = LinkedList()
_list.set_head(Node(5))
_list.push_front(6)
_list.push_back(11)
_list.remove_value(99)
print(_list.front())
