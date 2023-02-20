class Solution:
    def dfs(self, root):
        if not root:
            return
        self.dfs(root.left)
        self.dfs(root.right)
        self.res.append(root.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.dfs(root)
        return self.res


class Solution:
    def postorder(self, root):
        if not root:
            return
        stack = [root]
        while len(stack) > 0:
            node = stack.pop()
            self.res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.postorder(root)
        return self.res[::-1]
