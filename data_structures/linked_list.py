class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


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

sll.print_list()
