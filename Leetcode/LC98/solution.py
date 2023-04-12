# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:  # invalid
    def lessThan(self, root):
        if root is None or root.left is None:
            return True
        queue = [root.left]
        while len(queue):
            item = queue.pop(0)
            if item.left:
                if item.left.val >= root.val:
                    print("left>val", item.left.val, root.val)
                    return False
                queue.append(item.left)
            if item.right:
                if item.right.val >= root.val:
                    print("right>val", item.right.val, root.val)
                    return False
                queue.append(item.right)
        return True

    def biggerThan(self, root):
        if root is None or root.right is None:
            return True
        queue = [root.right]
        while len(queue):
            item = queue.pop(0)
            if item.left:
                if item.left.val <= root.val:
                    print("left<val", item.left.val, root.val)
                    return False
                queue.append(item.left)
            if item.right:
                if item.right.val <= root.val:
                    print("right<val", item.right.val, root.val)
                    return False
                queue.append(item.right)
        return True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root.left:
            if root.left.val >= root.val:
                return False
        if root.right:
            if root.right.val <= root.val:
                return False
        return self.lessThan(root) and self.biggerThan(root)


class Solution:  # invalid
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        if root.left is None:
            if root.val < root.right.val:
                return self.isValidBST(root.right)
            else:
                return False
        if root.right is None:
            if root.val > root.left.val:
                return self.isValidBST(root.left)
            else:
                return False
        if root.val > root.left.val and root.val < root.right.val:
            return self.isValidBST(root.left) and self.isValidBST(root.right)
        else:
            return False


class Solution:  # invalid
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        cond = True
        if root.val > self.max:
            self.max = root.val
        if root.left and root.left.val >= root.val:
            cond = False
        if root.right and root.right.
        cond = False
        if not self.isValidBST(root.left) or not self.isValidBST(root.right):
            cond = False
        return cond


class Solution:
    def helper(self, root, min, max):
        if root is None:
            return True
        if min is not None and root.val <= min:
            return False
        if max is not None and root.val >= max:
            return False
        return self.helper(root.left, min, root.val) and self.helper(root.right, root.val, max)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, None, None)
