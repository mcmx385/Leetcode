class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if targetSum == root.val and not root.left and not root.right:
            return True
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(
            root.right, targetSum - root.val
        )


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            node, val = stack.pop()
            if val == targetSum and not node.left and node.right:
                return True
            if node.left:
                stack.append((node.left, node.left.val + val))
            if node.right:
                stack.append((node.right, node.right.val + val))
        return False
