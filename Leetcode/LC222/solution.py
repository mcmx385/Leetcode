# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def helper(self, root):
        if not root:
            return 0
        count = 0
        if root.left:
            count += 1 + self.helper(root.left)
        if root.right:
            count += 1 + self.helper(root.right)
        return count

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + self.helper(root)


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = [root]
        levels = 0
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels += 1
        return 2 ** (levels - 1) + n - 1
