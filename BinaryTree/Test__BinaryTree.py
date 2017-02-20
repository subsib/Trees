import unittest
from BinaryTree import BinaryTree as bt


class Test__BinaryTree(unittest.TestCase):
    def setUp(self):
        self.tree = bt(1)

    def test_init_tree(self):
        """
        Checks the correctness of the intialization
        """
        tree = bt("a")
        tree = bt(1)
        tree = bt([2, 3])

    def test_init_tree_and_raises(self):
        """
        Checks the correctness of the initialization
        """
        with self.assertRaises(TypeError):
            bt()

    def test_add_right(self):
        assert len(self.tree) == 0
        self.tree.set_right(bt(2))
        assert len(self.tree) == 1

    def test_add_right_attribute_error(self):
        with self.assertRaises(AttributeError):
            self.tree.set_right(2)


if __name__ == "__main__":
    unittest.main()
