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


def has_cycle(head):
    slow = head
    fast = head.next

    while slow != fast:
        if fast is None or fast.next is None:
            return 0

        slow = slow.next
        fast = fast.next.next

    return 1
