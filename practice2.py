class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class LinkedList:
    def __init__(self, *data):
        self.head = None
        self._count = 0
        data =  list(data)
        if data:
            node = Node(data.pop(0))
            self.head = node
            for el in data:
                node.next = Node(el)
                node = node.next
                self._count += 1


    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, data):
        cur = Node(data)
        cur.next = self.head
        self.head = cur
        self._count += 1

    def add_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self._count += 1
            return
        for cur_node in self:
            pass
        cur_node.next = new_node





    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append('None')
        return ' -> '.join(nodes)



n1 = Node(100)
n2 = Node(23)
n3 = Node(11)
n4 = Node(100)



cur_list = LinkedList()

cur_list.head = n1
n1.next = n2
n2.next = n3
n3.next = n4

print(n1)

print(cur_list)