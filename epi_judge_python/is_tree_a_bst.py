from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack, inorder = [], float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # If next element in inorder traversal
            # is smaller than the previous one
            # that's not BST.
            if root.data < inorder:
                return False
            inorder = root.data
            root = root.right

        return True


class Solution2(object):
    def validBSTHelper(self, root):
        if not root:
            return True

        res = self.validBSTHelper(root.left)

        if not self.prev:
            self.prev = root
        else:
            if root.data < self.prev.data:
                res = False
            self.prev = root

        res = res and self.validBSTHelper(root.right)

        return res

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.prev = None
        return self.validBSTHelper(root)


class InOrderSol:
    @staticmethod
    def solution(tree):
        prev = float('-inf')

        def check_bst(root):
            nonlocal prev

            if not root:
                return True

            if not check_bst(root.left):
                return False
            if root.data < prev:
                return False
            prev = root.data
            return check_bst(root.right)

        return check_bst(tree)


def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    return InOrderSol.solution(tree)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
