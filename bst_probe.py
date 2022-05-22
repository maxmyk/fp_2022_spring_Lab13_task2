"""
File: bst_probe.py

A tester program for binary search trees.
"""

from linkedbst import LinkedBST
import random


def main():

    tree = LinkedBST()
    print("Adding D B A C F E G")
    tree.add("D")
    tree.add("B")
    tree.add("A")
    tree.add("C")
    tree.add("F")
    tree.add("E")
    tree.add("G")

    print("\nExpect True for A in tree: ", "A" in tree)

    print("\nString:\n" + str(tree),'height iter:', tree.height(),'height recur:', tree.height_recursive())

    clone = LinkedBST(tree)
    print("\nClone:\n" + str(clone))

    print("Expect True for tree == clone: ", tree == clone)

    print("\nFor loop: ", end="")
    for item in tree:
        print(item, end=" ")

    print("\n\ninorder traversal: ", end="")
    for item in tree.inorder():
        print(item, end=" ")

    #print("\n\npreorder traversal: ", end="")
    #for item in tree.preorder(): print(item, end = " ")

    #print("\n\npostorder traversal: ", end="")
    #for item in tree.postorder(): print(item, end = " ")

    #print("\n\nlevelorder traversal: ", end="")
    #for item in tree.levelorder(): print(item, end = " ")

    print("\n\nRemoving all items:", end=" ")
    for item in "ABCDEFG":
        print(tree.remove(item), end=" ")

    print("\n\nExpect 0: ", len(tree),'height iter:', tree.height(),'height recur:', tree.height_recursive())

    tree = LinkedBST(range(1, 16))
    print("\nAdded 1..15:\n" + str(tree), len(tree),'height iter:', tree.height(),'height recur:', tree.height_recursive())

    lyst = list(range(1, 16))

    random.shuffle(lyst)
    tree = LinkedBST(lyst)
    print("\nAdded ", lyst, "\n" + str(tree),'height iter:', tree.height(),'height recur:', tree.height_recursive())

    lyst = [113,22,30,68,74,45,91,88]
    # lyst = [113, 30, 68, 74, 45, 91, 88]
    # lyst = [113]
    # random.shuffle(lyst)
    tree = LinkedBST(lyst)
    print(tree, tree.height(), len(tree),'height iter:', tree.height(),'height recur:', tree.height_recursive())
    print('\nTree:\n', tree,'height iter:', tree.height(),'height recur:', tree.height_recursive())
    print(tree.is_balanced())
    print(tree.range_find(30, 91))
    print(tree.successor(1132))
    print(tree.predecessor(91))
    # print(', '.join([str(elem) for elem in tree.preorder()]),'\n', ', '.join([str(elem) for elem in tree.inorder()]))
    tree.rebalance()
    # print(tree.is_balanced())
    # print(', '.join([str(elem) for elem in tree.preorder()]),'\n', ', '.join([str(elem) for elem in tree.inorder()]))
    print(tree, len(tree),'height iter:', tree.height(),'height recur:', tree.height_recursive())
    tree.rebalance()
    print(tree, len(tree),'height iter:', tree.height(),'height recur:', tree.height_recursive())
    # tree.demo_bst('lab/13/words.txt')
   #print("\nAdded ", lyst, "\n" + str(tree))
   # tree.remove(10)
    #print("\nAdded ", lyst, "\n" + str(tree))
    # tree.remove(12)
    #print("\nAdded ", lyst, "\n" + str(tree))


if __name__ == "__main__":
    main()
