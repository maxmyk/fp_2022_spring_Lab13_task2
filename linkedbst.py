"""
File: linkedbst.py
Author: Ken Lambert
"""

from abstractcollection import AbstractCollection
from bstnode import BSTNode
from linkedstack import LinkedStack
from linkedqueue import LinkedQueue
from math import log


class LinkedBST(AbstractCollection):
    """An link-based binary search tree implementation."""

    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._root = None
        self._nodes = 0
        AbstractCollection.__init__(self, sourceCollection)

    def __repr__(self) -> str:
        return super().__str__()
    # Accessor methods

    def __str__(self):
        """Returns a string representation with the tree rotated
        90 degrees counterclockwise."""

        def recurse(node, level):
            ans = ""
            if node != None:
                ans += recurse(node.right, level + 1)
                ans += "| " * level
                ans += str(node.data) + "\n"
                ans += recurse(node.left, level + 1)
            return ans

        return recurse(self._root, 0)

    def __iter__(self):
        """Supports a preorder traversal on a view of self."""
        if not self.isEmpty():
            stack = LinkedStack()
            stack.push(self._root)
            while not stack.isEmpty():
                node = stack.pop()
                yield node.data
                if node.right != None:
                    stack.push(node.right)
                if node.left != None:
                    stack.push(node.left)

    def inorder(self):
        """Supports an inorder traversal on a view of self."""
        lyst = list()
        pre = LinkedStack()
        node = self._root
        while not pre.isEmpty() or node is not None:
            if node != None:
                pre.push(node)
                node = node.left
            else:
                node = pre.pop()
                if node.data not in lyst:
                    lyst.append(node.data)
                node = node.right
        return iter(lyst)

    def postorder(self):
        """Supports a postorder traversal on a view of self."""
        return None

    def levelorder(self):
        """Supports a levelorder traversal on a view of self."""
        return None

    def __contains__(self, item):
        """Returns True if target is found or False otherwise."""
        return self.find(item) != None

    def find(self, item):
        """If item matches an item in self, returns the
        matched item, or None otherwise."""
        node_x = self._root
        while node_x != None:
            if item < node_x.data:
                node_x = node_x.left
            elif item > node_x.data:
                node_x = node_x.right
            else:
                return item
        return None

    def find_node(self, item):
        """If item matches an item in self, returns the
        matched item, or None otherwise."""

        def recurse(node):
            if node is None:
                return None
            elif item == node:
                return node
            elif item.data < node.data:
                return recurse(node.left)
            else:
                return recurse(node.right)

        return recurse(self._root)

    def children(self, item):
        """Finds children"""
        ans = []
        if item.left != None:
            ans.append(item.left)
        if item.right != None:
            ans.append(item.right)
        return ans

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._root = None
        self._size = 0

    def add(self, item):
        def helper(root, item):
            newnode = BSTNode(item)
            node_x = root
            node_y = None
            while node_x != None:
                node_y = node_x
                if (item < node_x.data):
                    node_x = node_x.left
                else:
                    node_x = node_x.right
            if (node_y == None):
                node_y = newnode
            elif (item < node_y.data):
                node_y.left = newnode
            else:
                node_y.right = newnode
        if self.isEmpty():
            self._root = BSTNode(item)
        else:
            helper(self._root, item)
        self._size += 1

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item is not in self.
        postcondition: item is removed from self."""
        if not item in self:
            raise KeyError("Item not in tree.""")

        # Helper funkeyction to adjust placement of an item
        def lift_max_in_left_subtree_to_top(top):
            # Replace top's datum with the maximum datum in the left subtree
            # Pre:  top has a left child
            # Post: the maximum node in top's left subtree
            #       has been removed
            # Post: top.data = maximum value in top's left subtree
            parent = top
            current_node = top.left
            while not current_node.right == None:
                parent = current_node
                current_node = current_node.right
            top.data = current_node.data
            if parent == top:
                top.left = current_node.left
            else:
                parent.right = current_node.left

        # Begin main part of the method
        if self.isEmpty():
            return None

        # Attempt to locate the node containing the item
        item_removed = None
        pre_root = BSTNode(None)
        pre_root.left = self._root
        parent = pre_root
        direction = 'L'
        current_node = self._root
        while not current_node == None:
            if current_node.data == item:
                item_removed = current_node.data
                break
            parent = current_node
            if current_node.data > item:
                direction = 'L'
                current_node = current_node.left
            else:
                direction = 'R'
                current_node = current_node.right

        # Return None if the item is absent
        if item_removed == None:
            return None

        # The item is present, so remove its node

        # Case 1: The node has a left and a right child
        #         Replace the node's value with the maximum value in the
        #         left subtree
        #         Delete the maximium node in the left subtree
        if not current_node.left == None \
                and not current_node.right == None:
            lift_max_in_left_subtree_to_top(current_node)
        else:

            # Case 2: The node has no left child
            if current_node.left == None:
                new_child = current_node.right

                # Case 3: The node has no right child
            else:
                new_child = current_node.left

                # Case 2 & 3: Tie the parent to the new child
            if direction == 'L':
                parent.left = new_child
            else:
                parent.right = new_child

        # All cases: Reset the root (if it hasn't changed no harm done)
        #            Decrement the collection's size counter
        #            Return the item
        self._size -= 1
        if self.isEmpty():
            self._root = None
        else:
            self._root = pre_root.left
        return item_removed

    def replace(self, item, new_item):
        """
        If item is in self, replaces it with new_item and
        returns the old item, or returns None otherwise."""
        probe = self._root
        while probe != None:
            if probe.data == item:
                old_data = probe.data
                probe.data = new_item
                return old_data
            elif probe.data > item:
                probe = probe.left
            else:
                probe = probe.right
        return None

    def height_recursive(self):
        '''
        Return the height of tree
        :return: int
        '''
        branch = None
        if branch is None:
            branch = self._root
        return self.height1(branch)

    def height1(self, top):
        '''
        Helper function
        :param top:
        :return:
        '''
        nde = self.find_node(top)
        if nde != None:
            if nde.left == None and nde.right == None:
                return 0
            else:
                return 1 + max(self.height1(child) for child in self.children(top))

    def height(self):
        q = LinkedQueue()
        q.add(self._root)
        height = 0
        while not q._size == 0:
            height += 1
            size = len(q)
            for _ in range(size):
                curr = q.pop()
                if curr != None:
                    if curr.left != None:
                        q.add(curr.left)
                    if curr.right != None:
                        q.add(curr.right)
        return height-1

    def is_balanced(self):
        '''
        Return True if tree is balanced
        :return:
        '''
        return self.height() < (2 * log(len(self)+1, 2) - 1)

    def range_find(self, low, high):
        '''
        Returns a list of the items in the tree, where low <= item <= high."""
        :param low:
        :param high:
        :return:
        '''
        pre = [elem for elem in self.inorder()]
        if high in pre and low in pre:
            pre1 = pre[pre.index(low):pre.index(high)+1]
            pre2 = pre[pre.index(high):pre.index(low)+1]
            return max(pre1, pre2)

    def rebalance(self):
        '''
        Rebalances the tree.
        :return:
        '''
        def recurse(data, vmin, vmax):
            if vmin <= vmax:
                cur = (vmin + vmax + 1) // 2
                self.add(data[cur])
                recurse(data, cur + 1, vmax)
                recurse(data, vmin, cur - 1)
        if not self.is_balanced():
            data = list(self.inorder())
            self.clear()
            recurse(data, 0, len(data) - 1)

    def successor(self, item):
        """
        Returns the smallest item that is larger than
        item, or None if there is no such item.
        :param item:
        :type item:
        :return:
        :rtype:
        """
        pre = [elem for elem in sorted(
            [elem for elem in self.inorder()]) if elem > item]
        if pre != []:
            return min(pre)
        else:
            return None

    def predecessor(self, item):
        """
        Returns the largest item that is smaller than
        item, or None if there is no such item.
        :param item:
        :type item:
        :return:
        :rtype:
        """
        pre = [elem for elem in sorted(
            [elem for elem in self.inorder()]) if elem < item]
        if pre != []:
            return max(pre)
        else:
            return None

    def demo_bst(self, path):
        """
        Demonstration of efficiency binary search tree for the search tasks.
        :param path:
        :type path:
        :return:
        :rtype:
        - search time for 10,000 random words in an alphabetically ordered
        dictionary (search in a list of words using built-in list methods).
        - search time 10,000 random words in the dictionary, which is
        represented as a binary search tree. The binary search tree is
        built on the basis of sequential addition to the tree of words
        from the dictionary, which is arranged alphabetically.
        - search time 10,000 random words in the dictionary, which is
        represented as a binary search tree. The binary search tree is
        based on the consistent addition to the tree of words from a
        dictionary that is not sorted alphabetically (words are added
        to the tree randomly).
        - search time of 10,000 random words in the dictionary, which
        is presented as a binary search tree after its balancing.
        """
        from random import randrange, shuffle
        import timeit
        # random.seed(4600)
        base_lst = []
        print('Reading file...')
        with open(path, 'r') as file:
            contents = file.read()
            for line in contents.split('\n'):
                if line.strip() != '':
                    base_lst.append(line)
        print('Success.\nCreating sample lst...')

        # Making a smaller list by including only every 10-th word.
        lst_example = [base_lst[_] for _ in range(0, len(base_lst), 10)]
        bst_example_first = LinkedBST()
        bst_example_second = LinkedBST()
        print('Success.\nCreating working lst...')
        # Picking random 10000 words
        rand_words = [base_lst.pop(randrange(0, len(base_lst)-1))
                      for _ in range(10000)]
        print('Success.\nCreating Trees...')
        for elem in lst_example:
            bst_example_first.add(elem)
        shuffle(lst_example)
        for elem in lst_example:
            bst_example_second.add(elem)
        print('Success.\nTesting time...')

        @staticmethod
        def test1(words, lst_example):
            test = [True if word in lst_example else False for word in words]
            print('\tTest1 found/unfound: ', test.count(True), test.count(False))

        @staticmethod
        def test2(words, bst_example_first):
            test = [True if bst_example_first.find(
                word) else False for word in words]
            print('\tTest2 found/unfound: ',
                  test.count(True),
                  test.count(False))

        @staticmethod
        def test3(words, bst_example_second):
            test = [True if bst_example_second.find(
                word) else False for word in words]
            print('\tTest3 found/unfound: ',
                  test.count(True),
                  test.count(False))

        @staticmethod
        def reb_test():
            print('\tRebalancing...')
            bst_example_second.rebalance()
            print('\tSuccess.')

        @staticmethod
        def test4(words, bst_example_second):
            test = [True if bst_example_second.find(
                word) else False for word in words]
            print('\tTest4 found/unfound: ',
                  test.count(True),
                  test.count(False))
        print("\ttime: ", timeit.timeit(
            lambda: test1(rand_words, lst_example), number=1))
        print("\ttime: ", timeit.timeit(
            lambda: test2(rand_words, bst_example_first), number=1))
        print("\ttime: ", timeit.timeit(
            lambda: test3(rand_words, bst_example_second), number=1))
        reb_test()
        print("\ttime: ", timeit.timeit(
            lambda: test4(rand_words, bst_example_second), number=1))
        print('Important information!\nIf all functions\' found/unfound values \
are the same, they are correct.\nTests represent search time for 10,000 random \
words in:\n\t\
1.(1-st test): standart list\n\t\
2.(2-nd test): BST using sequential addition\n\t\
3.(3-rd test): BST using random addition\n\t\
4.(4-th test): rebalanced BST using random addition\n')


if __name__ == "__main__":
    tree = LinkedBST()
    tree.demo_bst('words.txt')
