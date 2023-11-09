class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

    def remove(self, val):
        current = self.root

        while current:
            if current.left and val == current.left.info:
                current.left = None
                break
            if current.right and val == current.right.info:
                current.right = None
                break
            if val < current.info:
                if current.left:
                    current = current.left
                else:
                    break
            elif val > current.info:
                if current.right:
                    current = current.right
                else:
                    break

    def min(self):
        current = self.root
        min = current.info

        while current:
            if min < current.info:
                if current.left:
                    current = current.left
                else:
                    return min
            elif min > current.info:
                if current.right:
                    current = current.right
                else:
                    return min


root = BinarySearchTree()

for i in [2, 4, 7, 1, 8, 99, 32, 23, 11]:
    root.create(i)

root.remove(23)


# q = int(input())
#
# heap = set()
#
# for i in range(q):
#     op = input().split()
#     op_0 = int(op[0])
#     if len(op) > 1:
#         op_1 = int(op[1])
#     else:
#         op_1 = None
#     if op_0 == 1:
#         heap.add(op_1)
#     elif op_0 == 2:
#         heap.remove(op_1)
#     elif op_0 == 3:
#         print(min(heap))
