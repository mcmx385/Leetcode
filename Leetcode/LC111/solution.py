import sys


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        if root.left != None and root.right != None:
            return 1+min(self.minDepth(root.left), self.minDepth(root.right))
        return 1+self.minDepth(root.left)+self.minDepth(root.right)


class Solution:
    minimum = 0

    def dfs(self, root, level):
        if root == None:
            return
        if root.left == None and root.right == None:
            self.minimum = min(self.minimum, level)
        self.dfs(root.left, level+1)
        self.dfs(root.right, level+1)

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        self.minimum = sys.maxsize
        self.dfs(root, 1)
        return self.minimum


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        queue = [root]
        minimum = 0
        while len(queue) > 0:
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                if node == None:
                    continue
                if node.left == None and node.right == None:
                    return minimum+1
                queue.append(node.left)
                queue.append(node.right)
            minimum += 1
        return minimum
