from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    def is_tree_bst(tree):
        def max_left(t):
            if not t:
                return float('-inf')
            return max(t.data, max_left(t.left), max_left(t.right))

        def min_right(t):
            if not t:
                return float('inf')
            return min(t.data, min_right(t.left), min_right(t.right))

        left = max_left(tree.left)
        right = min_right(tree.right)
        # print("tree.data:", tree.data, ', left:', left, ', right:', right)
        return left <= tree.data <= right

    def dfs(tree):
        if not tree:
            return True
        if is_tree_bst(tree):
            if not dfs(tree.left):
                return False
            if not dfs(tree.right):
                return False
        else:
            return False
        return True

    return dfs(tree)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
