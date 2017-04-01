#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# © 2017 Syrian Programmer.
#
# Stack LIFO: Last In, First Out
#
# Coded in Date: 31/3/2017.
#


class Stack:
    """ Python implementation the stack """

    def __init__(self, items=None):
        if items is None:
            items = []
        self.__items = items

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        return self.__items.pop()

    def peek(self):
        return self.__items[-1]

    def clear(self):
        self.__items.clear()

    def is_empty(self):
        return self.__items == []

    def get_items(self):
        return self.__items

    def size(self):
        return len(self.__items)

    def __len__(self):
        return len(self.__items)

    def __getitem__(self, item):
        return self.__items[item]

# Sample inputs
if __name__ == '__main__':
    x = [10, 20, 30, 40, 50, 60]

    q = Stack(x)
    q.push(70)
    q.push(80)
    print(q.get_items())

    print(q.pop())
    print(q.pop())
    print(q.get_items())

    print(len(q))
    print(q.size())
    print(q.is_empty())
    print(q.get_items())

    q.clear()
    print(q.get_items())

    q.push(70)
    q.push(80)
    print(q.get_items())

    print(q.pop())
    print(q.peek())
    print(q.get_items())
