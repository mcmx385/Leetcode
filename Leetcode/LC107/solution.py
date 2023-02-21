class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return []
        queue = [root]
        k = 0
        sizes = [1]
        level = 0
        res = []
        still = True
        while still:
            still = False
            for i in range(sizes[level]):
                node = queue[k]
                k += 1
                if node.left != None:
                    queue.append(node.left)
                    still = True
                if node.right != None:
                    queue.append(node.right)
                    still = True
            level += 1
            sizes.append(len(queue)-sum(sizes))
        level -= 1
        sizes = sizes[:-1]
        while len(queue) > 0:
            for size in sizes:
                values = []
                for i in range(size):
                    values.append(queue.pop(0).val)
                res.append(values)
        res = res[::-1]
        return res



class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        queue = [root]
        res = []
        while len(queue) > 0:
            size = len(queue)
            values = []
            for i in range(size):
                node = queue.pop(0)
                values.append(node.val)
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            res.append(values)
        res=res[::-1]
        return res



class Solution:
    res = []

    def dfs(self, root, level):
        if not root:
            return
        if len(self.res) > level:
            self.res.append([])
        self.res[level].append(root.val)
        self.dfs(root.left, level+1)
        self.dfs(root.right, level+1)

    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.dfs(root, 0)
        return self.res[::-1]


class Solution:
    res = {}

    def dfs(self, root, level):
        if not root:
            return
        if level not in self.res:
            self.res[level] = [root.val]
        else:
            self.res[level].append(root.val)
        self.dfs(root.left, level+1)
        self.dfs(root.right, level+1)

    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.dfs(root, 0)
        return list(self.res.values())[::-1]