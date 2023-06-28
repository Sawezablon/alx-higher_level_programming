#!/usr/bin/python3
"""Define classes for a singly-linked list."""


class Node:
    """Represent a singly-linked list."""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represent a singly-linked list."""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            zab = self.__head
            while (zab.next_node is not None and
                    zab.next_node.data < value):
                zab = zab.next_node
            new.next_node = zab.next_node
            zab.next_node = new

    def __str__(self):
        values = []
        zab = self.__head
        while zab is not None:
            values.append(str(zab.data))
            zab = zab.next_node
        return ('\n'.join(values))
