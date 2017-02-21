#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from BinaryTree.BinaryTree import BinaryTree

__author__ = "Arabella Brayer"
__date__ = "20 feb 2017"


class Test__BinaryTree(unittest.TestCase):
    def setUp(self):
        self.tree = BinaryTree(1)

    def test_init_tree(self):
        """
        Checks the correctness of the intialization
        """
        tree = BinaryTree("a")
        tree = BinaryTree(1)
        tree = BinaryTree([2, 3])

    def test_init_tree_and_raises(self):
        """
        Checks the correctness of the initialization
        """
        with self.assertRaises(TypeError):
            BinaryTree()

    def test_add_right(self):
        assert len(self.tree) == 0
        self.tree.set_right(BinaryTree(2))
        assert len(self.tree) == 1

    def test_add_right_attribute_error(self):
        with self.assertRaises(AttributeError):
            self.tree.set_right(2)

    def test_add_left(self):
        assert len(self.tree) == 0
        self.tree.set_left(None)
        assert len(self.tree) == 0
        self.tree.set_left(BinaryTree("là"))

    def test_add_left_attribute_error(self):
        with self.assertRaises(AttributeError):
            self.tree.set_left("machin")

    def test_display_tree(self):
        self.tree.set_left(BinaryTree(2))
        self.tree.set_right(BinaryTree(3))
        print(self.tree)

if __name__ == "__main__":
    unittest.main()
