from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def helper(self, root):
        if not root or not root.left and not root.right:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        count = 0
        if root.left:
            count += 1 + self.helper(root.left)
        if root.right:
            count += 1 + self.helper(root.right)
        return count


class Solution:
    def helper(self, root):
        if not root:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        self.res = max(self.res, left + right)
        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.helper(root)
        return self.res
