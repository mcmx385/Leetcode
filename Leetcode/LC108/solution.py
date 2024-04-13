class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insert(self, root, nums):
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.insert(root.left, nums[:mid])
        root.right = self.insert(root.right, nums[mid + 1 :])
        return root

    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        return self.insert(None, nums)


class Solution:
    nums = []

    def insert(self, root, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        root = TreeNode(self.nums[mid])
        root.left = self.insert(root.left, start, mid - 1)
        root.right = self.insert(root.right, mid + 1, end)
        return root

    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        self.nums = nums
        return self.insert(None, 0, len(nums) - 1)


def printTree(root):
    queue = [root]
    while len(queue) > 0:
        size = len(queue)
        for i in range(size):
            node = queue.pop(0)
            print(node.val, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print("\n")


if __name__ == "__main__":
    nums = [-10, -3, 0, 5, 9]
    root = Solution().sortedArrayToBST(nums)
    printTree(root)
