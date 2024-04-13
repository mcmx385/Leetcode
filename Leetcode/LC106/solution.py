class TreeNode:
    def self(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
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
        return res


class Solution:
    res = []

    def dfs(self, root, level):
        if not root:
            return
        if len(self.res) > level:
            self.res.append([])
        self.res[level].append(root.val)
        self.dfs(root.left, level + 1)
        self.dfs(root.right, level + 1)

    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        self.dfs(root, 0)
        return self.res


class Solution:
    res = {}

    def dfs(self, root, level):
        if not root:
            return
        if level not in self.res:
            self.res[level] = [root.val]
        else:
            self.res[level].append(root.val)
        self.dfs(root.left, level + 1)
        self.dfs(root.right, level + 1)

    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        self.dfs(root, 0)
        return list(self.res.values())


if __name__ == "__main__":
    nodes = [1, 2, 2, None, 3, None, 3]
    s = Solution()
    root = constructTree(nodes)
    res = s.levelOrder(root)
    print(res)
