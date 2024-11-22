# Name: Jaskaran Singh Sidhu
# OSU Email: sidhuja@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: A4 - BST and AVL Tree Implementation
# Due Date: November 17, 2024
# Description: This file contains the implementation of the AVL tree, a self-balancing
#              binary search tree. The AVL class extends the BST class, adding methods
#              to maintain the AVL property (balance factor of -1, 0, or 1) after
#              additions and deletions. Rotations (left and right) and rebalancing
#              operations are implemented to ensure height balance.

from bst import BSTNode, BST


class AVLNode(BSTNode):
    def __init__(self, value: object) -> None:
        super().__init__(value)
        self.height = 1


class AVL(BST):
    def add(self, value: object) -> None:
        """Add a value to the AVL tree."""
        self._root = self._add_helper(self._root, value)

    def _add_helper(self, node: AVLNode, value: object) -> AVLNode:
        if not node:
            return AVLNode(value)
        if value < node.value:
            node.left = self._add_helper(node.left, value)
        else:
            node.right = self._add_helper(node.right, value)
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        return self._rebalance(node)

    def _rebalance(self, node: AVLNode) -> AVLNode:
        balance = self._balance_factor(node)
        if balance > 1:  # Left heavy
            if self._balance_factor(node.left) < 0:  # Left-Right case
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1:  # Right heavy
            if self._balance_factor(node.right) > 0:  # Right-Left case
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        return node

    def _rotate_left(self, z: AVLNode) -> AVLNode:
        y = z.right
        z.right = y.left
        y.left = z
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _rotate_right(self, z: AVLNode) -> AVLNode:
        y = z.left
        z.left = y.right
        y.right = z
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _balance_factor(self, node: AVLNode) -> int:
        return self._get_height(node.left) - self._get_height(node.right)

    def _get_height(self, node: AVLNode) -> int:
        return node.height if node else 0
