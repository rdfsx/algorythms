class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None


def preOrder(root):
    if root == None:
        return
    print(root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
            return self.root
        root = self.root
        while root:
            if root.info > val:
                if root.left is None:
                    root.left = Node(val)
                    return root
                else:
                    root = root.left
                    continue
            elif root.info < val:
                if root.right is None:
                    root.right = Node(val)
                    return root
                else:
                    root = root.right
                    continue


tree = BinarySearchTree()

arr = [4, 2, 3, 1, 7, 6]

for i in range(len(arr)):
    tree.insert(arr[i])

preOrder(tree.root)
