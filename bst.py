# Name: Jaskaran Singh Sidhu
# OSU Email: jaskaran.sidhu@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: A4 - BST and AVL Tree Implementation
# Due Date: November 17, 2024
# Description: This file contains the implementation of the Binary Search Tree (BST).
#              Includes methods for adding, removing, searching, traversing, and clearing
#              the tree. The class ensures correct structure and handling of nodes.

from queue_and_stack import Queue


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

    def get_root(self) -> BSTNode:
        """Return the root of the tree."""
        return self._root

    def add(self, value: object) -> None:
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
        return self._contains_helper(self._root, value)

    def _contains_helper(self, node: BSTNode, value: object) -> bool:
        if node is None:
            return False
        if value == node.value:
            return True
        if value < node.value:
            return self._contains_helper(node.left, value)
        return self._contains_helper(node.right, value)

    def remove(self, value: object) -> bool:
        """Remove a value from the tree."""
        self._root, removed = self._remove_helper(self._root, value)
        return removed

    def _remove_helper(self, node: BSTNode, value: object) -> (BSTNode, bool):
        if node is None:
            return None, False
        if value < node.value:
            node.left, removed = self._remove_helper(node.left, value)
        elif value > node.value:
            node.right, removed = self._remove_helper(node.right, value)
        else:
            if not node.left:
                return node.right, True
            if not node.right:
                return node.left, True
            min_larger_node = self._find_min(node.right)
            node.value = min_larger_node.value
            node.right, _ = self._remove_helper(node.right, node.value)
            return node, True
        return node, removed

    def inorder_traversal(self) -> Queue:
        result = Queue()
        self._inorder_helper(self._root, result)
        return result

    def _inorder_helper(self, node: BSTNode, result: Queue) -> None:
        if node:
            self._inorder_helper(node.left, result)
            result.enqueue(node.value)
            self._inorder_helper(node.right, result)

    def _find_min(self, node: BSTNode) -> BSTNode:
        current = node
        while current.left:
            current = current.left
        return current

    def find_min(self) -> object:
        if self._root is None:
            return None
        return self._find_min(self._root).value

    def find_max(self) -> object:
        if self._root is None:
            return None
        current = self._root
        while current.right:
            current = current.right
        return current.value

    def is_empty(self) -> bool:
        return self._root is None

    def make_empty(self) -> None:
        self._root = None
