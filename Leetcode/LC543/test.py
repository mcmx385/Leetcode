from solution import Solution

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

values = [4,-7,-3,None,None,-9,-3,9,-7,-4,None,6,None,-6,-6,None,None,0,6,5,None,9,None,None,-1,-4,None,None,None,-2]
# [4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]
root=TreeNode(values[0])
queue=[root]
i=1
while i<len(values):
    node=queue.pop(0)
    if values[i]:
        node.left=TreeNode(values[i])
        queue.append(node.left)
    i+=1
    if i<len(values) and values[i]:
        node.right=TreeNode(values[i])
        queue.append(node.right)
    i+=1
s=Solution()
print(s.diameterOfBinaryTree(root))