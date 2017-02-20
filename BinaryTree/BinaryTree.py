# -*- coding: utf-8 -*-


class BinaryTree:
    """
    Builds a binary tree contening the given data
    """
    def __init__(self, data):
        self.__data = data
        self.__left = None
        self.__right = None
        self.__father = None

    def get_value(self):
        """
        Returs the value from the current node
        :return: the value from the current node
        """
        return self.__data

    def set_value(self, new_data):
        """
        set the data from the current node at the new value
        :param new_data: new value
        :return: None
        """
        self.__data = new_data

    def get_left(self):
        """
        Returns the left child. Can be None if no child.
        :return: a tree, the left child or None if its empty.
        """
        return self.__left

    def set_left(self, new_left):
        """

        :param new_left: set a new right child
        :return:
        """
        assert isinstance(new_left, BinaryTree) or None

        if self.__left is not None:
            self.__left.set_father(None)
        self.__left = new_left
        if self.__left is not None:
            self.__left.set_father(self)

    def get_right(self):
        """
        Returns the right child. Can be None if no child.
        :return: a tree, the right child or None if its empty.
        """
        return self.__right

    def set_right(self, new_right):
        """
        Add a right child at the current node
        :param new_right: set a new right child
        :return: None
        """

        print("type : ", new_right.__class__)
        assert isinstance(new_right, BinaryTree) or None
        if self.__right is not None:
            self.__right.set_father(None)
        self.__right = new_right
        if self.__right is not None:
            self.__right.set_father(self)

    def is_leaf(self):
        """
        Returns True if the current node is a leaf
        :return: True if the node is a leaf, False otherwise
        """
        return len(self) < 1

    def get_father(self):
        """
        Returns the father of the current node
        :return: the father of the current node
        """
        return self.__father

    def set_father(self, new_father):
        """
        Set the father of the current node
        :param new_father: the new node to be the father of the current node
        :return: None
        """
        self.__father = new_father

    def detach(self):
        """
        Cut the current tree from its father
        :return: None
        """
        self.__father = None

    def get_depth(self):
        """
        Returns the depth of the tree
        :return: integer, the depth of the whole tree
        """
        depth = 1
        depth += 0 if self.__left is None else self.__left.get_depth()
        depth += 0 if self.__right is None else self.__right.get_depth()
        return depth

    def __len__(self):
        """
        Returns the number of children. Can be 0, 1 or 2.
        :return: integer that is the number of children of the current node
        """
        return (0 if not self.__left else 1) + (0 if not self.__right else 1)

    def __str__(self):
        if self.is_leaf():
            return "BT(" + str(self.__data) + ")"
        return "BT(" + str(self.__data) + ", " + str(self.__left) + str(self.__right) + ")"

    def __repr__(self):
        return str(self)
