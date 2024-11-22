# Name: Jaskaran Singh Sidhu
# OSU Email: jaskaran.sidhu@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: A4 - BST and AVL Tree Implementation
# Due Date: November 17, 2024
# Description: AVL tree implementation with self-balancing functionality.
#              Includes corrected methods for add() and remove().

from bst import BST, BSTNode


class AVLNode(BSTNode):
    def __init__(self, value: object) -> None:
        super().__init__(value)
        self.height = 1
        self.parent = None  # Parent pointer for AVL rebalancing


class AVL(BST):
    def add(self, value: object) -> None:
        """Adds a value to the AVL tree and rebalances it."""
        self._root = self._add_helper(self._root, value, None)

    def _add_helper(self, node: AVLNode, value: object, parent: AVLNode) -> AVLNode:
        if not node:
            new_node = AVLNode(value)
            new_node.parent = parent  # Set parent pointer
            return new_node

        if value < node.value:
            node.left = self._add_helper(node.left, value, node)
        else:
            node.right = self._add_helper(node.right, value, node)

        # Update height and rebalance
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        return self._rebalance(node)

    def remove(self, value: object) -> bool:
        """Removes a value from the AVL tree and rebalances it."""
        self._root, removed = self._remove_helper(self._root, value)
        return removed

    def _remove_helper(self, node: AVLNode, value: object) -> (AVLNode, bool):
        if not node:
            return None, False

        if value < node.value:
            node.left, removed = self._remove_helper(node.left, value)
        elif value > node.value:
            node.right, removed = self._remove_helper(node.right, value)
        else:
            removed = True
            # Node with one child or no child
            if not node.left:
                if node.right:
                    node.right.parent = node.parent  # Update parent pointer
                return node.right, removed
            elif not node.right:
                if node.left:
                    node.left.parent = node.parent  # Update parent pointer
                return node.left, removed
            # Node with two children: Get inorder successor
            min_larger_node = self._find_min(node.right)
            node.value = min_larger_node.value
            node.right, _ = self._remove_helper(node.right, min_larger_node.value)

        # Update height and rebalance
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        return self._rebalance(node), removed

    def _rebalance(self, node: AVLNode) -> AVLNode:
        """Rebalances the AVL tree."""
        balance = self._balance_factor(node)

        if balance > 1:
            if self._balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if balance < -1:
            if self._balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _rotate_left(self, z: AVLNode) -> AVLNode:
        y = z.right
        z.right = y.left
        if y.left:
            y.left.parent = z  # Update parent pointer
        y.left = z
        y.parent = z.parent  # Update parent pointer
        z.parent = y  # Update parent pointer

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _rotate_right(self, z: AVLNode) -> AVLNode:
        y = z.left
        z.left = y.right
        if y.right:
            y.right.parent = z  # Update parent pointer
        y.right = z
        y.parent = z.parent  # Update parent pointer
        z.parent = y  # Update parent pointer

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _balance_factor(self, node: AVLNode) -> int:
        return self._get_height(node.left) - self._get_height(node.right)

    def _get_height(self, node: AVLNode) -> int:
        return node.height if node else 0

    def _find_min(self, node: AVLNode) -> AVLNode:
        current = node
        while current.left:
            current = current.left
        return current
