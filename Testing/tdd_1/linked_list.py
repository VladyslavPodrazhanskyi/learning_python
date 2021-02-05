class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


list_of_nodes = []
prev = None
for i in range(3):
    node = Node(data=i)
    if prev:

    node.next = node.data + 1
    list_of_nodes.append(node)

