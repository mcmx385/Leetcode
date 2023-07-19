# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, string):
        if root is None:
            return
        if string != "":
            string += "->"
        string += str(root.val)
        if root.left == None and root.right == None:
            self.list.append(string)
        self.helper(root.left, string)
        self.helper(root.right, string)

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.list = []
        self.helper(root, "")
        return self.list
