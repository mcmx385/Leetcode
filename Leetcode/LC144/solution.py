class Solution:
    def dfs(self, root):
        if not root:
            return
        self.res.append(root.val)
        self.dfs(root.left)
        self.dfs(root.right)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.dfs(root)
        return self.res


class Solution:
    res = []

    def preorder(self, root):
        if not root:
            return []
        queue = [root]
        while len(queue) > 0:
            node = queue.pop()
            self.res.append(node.val)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.preorder(root)
        return self.res


class Solution:
    res = []

    def morris(self, root):
        if not root:
            return []
        cur = root
        while cur:
            if not cur.left:
                self.res.append(cur.val)
                cur = cur.right
            else:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right
                if not pre.right:
                    self.res.append(cur.val)
                    pre.right = cur
                    cur = cur.left
                else:
                    pre.right = None
                    cur = cur.right

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.morris(root)
        return self.res
