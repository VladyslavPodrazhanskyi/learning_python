class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

    def __repr__(self):
        return str(self.dataval)


class SLinkedList:
    def __init__(self):
        self.headval = None

    def print_list(self):
        printel = self.headval
        while printel is not None:
            print(printel.dataval)
            printel = printel.nextval

    def insert_begin(self, new_val):
        second_node = self.headval
        self.headval = Node(new_val)
        self.headval.nextval = second_node

    def insert_end(self, new_val):
        new_node = Node(new_val)
        if self.headval is None:
            self.headval = new_node
            return
        cur_node = self.headval
        while cur_node.nextval:
            cur_node = cur_node.nextval
        cur_node.nextval = new_node

    def in_between(self, middle_val, new_val):
        new_node = Node(new_val)
        if self.headval is None:
            self.headval = new_node
            return
        cur_node = self.headval
        while cur_node.dataval != middle_val:
            cur_node = cur_node.nextval
            if cur_node is None:
                return
        next_node = cur_node.nextval
        cur_node.nextval = new_node
        new_node.nextval = next_node
        return

    def remove_node(self, remove_val):
        if self.headval is None:
            return
        if self.headval.dataval == remove_val:
            self.headval = self.headval.nextval
            return
        prev_node = self.headval
        cur_node = prev_node.nextval
        while cur_node.dataval != remove_val:
            prev_node = cur_node
            cur_node = prev_node.nextval
            if cur_node is None:
                return
        prev_node.nextval = cur_node.nextval

    def __repr__(self):
        if self.headval is None:
            return
        nodes = []
        cur_node = self.headval
        while cur_node is not None:
            nodes.append(cur_node)
            cur_node = cur_node.nextval
        nodes.append(None)
        return '->'.join([str(node) for node in nodes])


sll = SLinkedList()

e1 = Node('Mon')
e2 = Node('Tue')
e3 = Node('Wen')

sll.headval = e1
e1.nextval = e2
e2.nextval = e3

# sll.print_list()

sll.insert_begin('Sun')
sll.insert_end('Thu')
sll.in_between('Wen', 'Wen1')
sll.remove_node('Wen1')

sll.print_list()
print(sll)
