"""
Create CustomList – the linked list of values of random type, which size changes dynamically and has an ability to index
elements.

The task requires implementation of the following functionality:
• Create the empty user list and the one based on enumeration of values separated by commas. The elements are stored
in form of unidirectional linked list. Nodes of this list must be implemented in class Item.
in form of unidirectional linked list. Nodes of this list must be implemented in class Item.
    Method name: __init__(self, *data) -> None;
• Add and remove elements.
    Method names: append(self, value) -> None - to add to the end,
                add_start(self, value) -> None - to add to the start,
                remove(self, value) -> None - to remove the first occurrence of given value;
• Operations with elements by index. Negative indexing is not necessary.
    Method names: __getitem__(self, index) -> Any,
                __setitem__(self, index, data) -> None,
                __delitem__(self, index) -> None;
• Receive index of predetermined value.
    Method name: find(self, value) -> Any;
• Clear the list.
    Method name: clear(self) -> None;
• Receive lists length.
    Method name: __len__(self) -> int;
• Make CustomList iterable to use in for-loops;
    Method name: __iter__(self);
• Raise exceptions when:
    find() or remove() don't find specific value
    index out of bound at methods __getitem__, __setitem__, __delitem__.


Notes:
    The class CustomList must not inherit from anything (except from the object, of course).
    Function names should be as described above. Additional functionality has no naming requirements.
    Indexation starts with 0.
    List length changes while adding and removing elements.
    Inside the list the elements are connected as in a linked list, starting with link to head.
"""
from typing import Any


class Item:
    """
    A node in a unidirectional linked list.
    """

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'Node {str(self.data)}'


class CustomList:
    """
    An unidirectional linked list.
    """

    def __init__(self, *data):
        self.head = None
        self._count = 0
        data = list(data)
        if data:
            node = Item(data=data.pop(0))
            self.head = node
            self._count += 1
            for elem in data:
                node.next = Item(elem)
                node = node.next
                self._count += 1

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def append(self, value) -> None:
        item = Item(data=value)
        if self.head is None:
            self.head = item
            self._count += 1
            return
        for node in self:
            pass
        node.next = item
        self._count += 1

    def add_start(self, value) -> None:
        item = Item(value)
        item.next = self.head
        self.head = item
        self._count += 1

    def remove(self, value) -> None:
        if self.head is None:
            raise Exception('List is empty')
        if self.head.data == value:
            self.head = self.head.next
            self._count -= 1
            return
        prev = self.head
        for node in self:
            if node.data == value:
                prev.next = node.next
                self._count -= 1
                return
            prev = node
        raise Exception(f"Value {value} not found.")

    def __getitem__(self, index) -> Any:
        if type(index) is not int:
            raise ValueError
        if index < 0 or index >= self._count:
            raise IndexError
        num = 0
        for node in self:
            if num == index:
                return node
            num += 1

    def __setitem__(self, index, value) -> None:
        if type(index) is not int:
            raise ValueError
        if index < 0 or index >= self._count:
            raise IndexError
        num = 0
        for el in self:
            if num == index:
                el.data = value
                return
            num += 1

    def __delitem__(self, index) -> None:
        if type(index) is not int:
            raise ValueError
        if index < 0 or index >= self._count:
            raise IndexError
        if index == 0:
            self.head.next = self.head
            self._count -= 1
            return
        cur_num = 0
        prev = self.head
        for node in self:
            if cur_num == index:
                prev.next = node.next
                self._count -= 1
                return
            prev = node
            cur_num += 1

    def len(self) -> int:
        return self._count

    def find(self, value):
        pass

    def clear(self):
        pass


    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


llist = CustomList()

llist[0] = "d"
print(llist)
