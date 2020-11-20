class BST:
    def __init__(self):
        self.root = None

    def search(self, key):
        node = self.root

        while node:
            if node.val == key:
                return node
            elif node.val > key:
                node = node.left
            else:
                node = node.right

        return None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            current = self.root
            while current:
                if key <= current.val:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(key)
                        break
                else:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(key)
                        break

    def traverse_inorder(self, root):
        if root:
            self.traverse_inorder(root.left)
            print(root.val)
            self.traverse_inorder(root.right)
        return

    def traverse_preorder(self, root):
        if root:
            print(root.val)
            self.traverse_preorder(root.left)
            self.traverse_preorder(root.right)
        return

    def traverse_postorder(self, root):
        if root:
            self.traverse_postorder(root.left)
            self.traverse_postorder(root.right)
            print(root.val)
        return


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


elements = [5, 35, 7, 1, 144, 87, 11]
bst = BST()
for i in elements:
    bst.insert(i)
print('In-Order Traversal:')
bst.traverse_inorder(bst.root)
print('Pre-Order Traversal:')
bst.traverse_preorder(bst.root)
print('Post-Order Traversal:')
bst.traverse_postorder(bst.root)
print('Search: 1')
print(bst.search(1).val)
