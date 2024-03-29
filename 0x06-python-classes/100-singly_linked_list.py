#!/usr/bin/python3
"""A class Node defines a node of a singly linked list"""


class Node:
    """class Node is singly linked list"""

    def __init__(self, data, next_node=None):
        """Instantiation with data and next_node"""
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = data
        if ((next_node is not None) and
                not (isinstance(next_node, Node))):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = next_node

    @property
    def data(self):
        """data retriver of the linked list"""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """the node pointer"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if (value is not None) and not (isinstance(value, Node)):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """class SinglyLinkedList is list of data"""

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
            tmp = self.__head
            while (tmp.next_node is not None and tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
