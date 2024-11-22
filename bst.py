# Name: Jaskaran Singh Sidhu
# OSU Email: sidhuja@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: A4 - BST and AVL Tree Implementation
# Due Date: November 17, 2024
# Description: This file contains the implementation of the Binary Search Tree (BST).
#              The BST class provides methods to add, remove, search, and traverse
#              nodes in a binary search tree. Additional methods include finding
#              the minimum and maximum values, checking if the tree is empty, and 
#              clearing the tree. The BSTNode class represents individual nodes in
#              the tree. This file also includes helper methods for tree management.

from queue_and_stack import Queue, Stack


class BSTNode:
    def __init__(self, value: object) -> None:
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self, start_tree=None) -> None:
        self._root = None
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def add(self, value: object) -> None:
        """Add a value to the BST."""
        if self._root is None:
            self._root = BSTNode(value)
        else:
            self._add_helper(self._root, value)

    def _add_helper(self, node: BSTNode, value: object) -> None:
        if value < node.value:
            if node.left is None:
                node.left = BSTNode(value)
            else:
                self._add_helper(node.left, value)
        else:
            if node.right is None:
                node.right = BSTNode(value)
            else:
                self._add_helper(node.right, value)

    def contains(self, value: object) -> bool:
        """Check if the BST contains a value."""
        return self._contains_helper(self._root, value)

    def _contains_helper(self, node: BSTNode, value: object) -> bool:
        if node is None:
            return False
        if value == node.value:
            return True
        if value < node.value:
            return self._contains_helper(node.left, value)
        return self._contains_helper(node.right, value)

    def inorder_traversal(self) -> Queue:
        """Return an inorder traversal as a Queue."""
        result = Queue()
        self._inorder_helper(self._root, result)
        return result

    def _inorder_helper(self, node: BSTNode, result: Queue) -> None:
        if node:
            self._inorder_helper(node.left, result)
            result.enqueue(node.value)
            self._inorder_helper(node.right, result)

    def find_min(self) -> object:
        """Return the minimum value in the BST."""
        if self._root is None:
            return None
        current = self._root
        while current.left:
            current = current.left
        return current.value

    def find_max(self) -> object:
        """Return the maximum value in the BST."""
        if self._root is None:
            return None
        current = self._root
        while current.right:
            current = current.right
        return current.value

    def is_empty(self) -> bool:
        """Check if the BST is empty."""
        return self._root is None

    def make_empty(self) -> None:
        """Clear the BST."""
        self._root = None
