class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


class Solution:
    level = 0

    def bfs(self, root, level):
        if root == None:
            return
        self.level = max(self.level, level + 1)
        self.bfs(root.left, level + 1)
        self.bfs(root.right, level + 1)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.bfs(root, 0)
        return self.level
