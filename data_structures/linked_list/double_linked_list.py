class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return str(self.value)


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_val):

        new_node = Node(new_val)
        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    def print_list(self):
        nodes = []
        cur_node = self.head
        while cur_node is not None:
            nodes.append(str(cur_node.value))
            cur_node = cur_node.next
        nodes.append('None')
        print(' <-> '.join(nodes))

    def insert(self, prev_val, new_val):
        new_node = Node(new_val)
        if prev_val is None:
            return
        cur_node = self.head
        while prev_val != cur_node.value:
            if cur_node.next is not None:
                cur_node = cur_node.next
            else:
                return
        new_node.next = cur_node.next
        new_node.prev = cur_node
        cur_node.next = new_node

    def append(self, new_val):
        new_node = Node(new_val)
        if self.head is None:
            self.head = new_node
            return
        prev_node = self.head
        cur_node = prev_node.next
        while cur_node is not None:
            prev_node = cur_node
            cur_node = cur_node.next
        prev_node.next = new_node
        new_node.prev = prev_node


if __name__ == '__main__':
    dll = DoubleLinkedList()
    dll.push('Fri')
    dll.push('Wen')
    dll.push('Tue')
    dll.push('Mon')
    dll.print_list()
    dll.insert('Wen', 'Thu')
    dll.append('Sat')
    dll.print_list()
