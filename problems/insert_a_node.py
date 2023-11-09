class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def insertNodeAtPosition(llist, data, position):
    node = SinglyLinkedListNode(data)
    if position == 0:
        node.next = llist
        return llist
    current = llist
    for _ in range(position - 1):
        current = current.next
    node.next = current.next
    current.next = node
    return llist
