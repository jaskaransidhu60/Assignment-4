# Name: Jaskaran Singh Sidhu
# OSU Email: sidhuja@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: A4 - BST and AVL Tree Implementation
# Due Date: November 17, 2024
# Description: This file contains the implementations of the Queue and Stack
#              abstract data types (ADTs). These helper classes are used in 
#              the implementation of the BST and AVL trees. The Queue supports
#              enqueue, dequeue, and is_empty operations, while the Stack supports
#              push, pop, top, and is_empty operations. Both are essential for
#              traversal and management of tree nodes.

class Queue:
    """Class implementing QUEUE ADT. Supported methods are: enqueue, dequeue, is_empty"""
    def __init__(self):
        self._data = []

    def enqueue(self, value: object) -> None:
        self._data.append(value)

    def dequeue(self):
        return self._data.pop(0)

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def __str__(self) -> str:
        data_str = [str(item) for item in self._data]
        return "QUEUE { " + ", ".join(data_str) + " }"


class Stack:
    """Class implementing STACK ADT. Supported methods are: push, pop, top, is_empty"""
    def __init__(self):
        self._data = []

    def push(self, value: object) -> None:
        self._data.append(value)

    def pop(self):
        return self._data.pop()

    def top(self):
        return self._data[-1]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def __str__(self) -> str:
        data_str = [str(item) for item in self._data]
        return "STACK: { " + ", ".join(data_str) + " }"
