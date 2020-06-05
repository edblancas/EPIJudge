from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from collections import namedtuple


def is_balanced_binary_tree_me(tree: BinaryTreeNode) -> bool:
    r = bal(tree)
    return False if r == -1 else True


def bal(tree: BinaryTreeNode) -> int:
    """
               4
           3         6
        2    5     .     7
      1  .  .  .       .  .
     . .

    """
    if tree is None:
        return 0

    height_left = bal(tree.left)
    height_right = bal(tree.right)

    if height_left == -1 or height_right == -1:
        return -1

    if abs(height_left - height_right) > 1:
        return -1

    return max(height_right + 1, height_left + 1)


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    return sol_book(tree)


def sol_book(tree: BinaryTreeNode):
    BalancedAndHeight = namedtuple('BalancedAndHeight', 'balanced, height')

    def sol(t: BinaryTreeNode) -> BalancedAndHeight:
        if not t:
            return BalancedAndHeight(True, 0)

        l = sol(t.left)
        if not l.balanced:
            return BalancedAndHeight(False, -1)

        r = sol(t.right)
        # WTF!!!
        # if not l.balanced:
        if not r.balanced:
            return BalancedAndHeight(False, -1)

        if abs(l.height - r.height) > 1:
            return BalancedAndHeight(False, -1)

        return BalancedAndHeight(True, max(r.height, l.height) + 1)

    return sol(tree).balanced


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
