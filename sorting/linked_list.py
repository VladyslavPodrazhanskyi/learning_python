class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(nodes.pop(0))
            self.head = node
            for el in nodes:
                node.next = Node(el)
                node = node.next

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, added_node):
        added_node.next = self.head
        self.head = added_node

    def add_last(self, new_node):
        if self.head is None:
            self.head = new_node
            return
        for cur_node in self:
            pass
        cur_node.next = new_node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")
        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
        raise Exception(f"Node with data {target_node_data} not found")

    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception('The list is empty')

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev = self.head
        for node in self:
            if node.data == target_node_data:
                prev.next = new_node
                new_node.next = node
                return
            prev = node
        raise Exception(f"Node with data {target_node_data} not found")

    def remove(self, target_node_data):
        if self.head is None:
            raise Exception('The list is empty')
        if self.head.data == target_node_data:
            self.head = self.head.next
            return
        prev = self.head
        for node in self:
            if node.data == target_node_data:
                prev.next = node.next
                return
            prev = node
        raise Exception(f"Node with data {target_node_data} not found")

    def reverse(self):
        if self.head is None:
            return
        if self.head.next is None:
            return
        nodes = []
        for node in self:
            nodes.append(node)
            self.remove(node.data)
        for node in nodes:
            self.add_first(node)
        return

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append('None')
        return " -> ".join(nodes)


# first = Node('a')
# second= Node('b')
# third = Node(4)
#
llist = LinkedList(['a', 'b', 'c'])
#
# llist.head = first
#
# first.next = second
# second.next = third
#
# print(llist)

# for node in llist:
#     print(node)
#
# llist.add_first(Node('new_added'))
# llist.add_last(Node('last_added'))
# llist.add_after('a', Node('after_a'))
# llist.add_before('c', Node('before c'))
# try:
#     llist.add_before('f', Node('before f'))
# except Exception as e:
#     print(e)
#
# llist.remove('new_added')
# print(llist)
# llist.reverse()
print(llist)
