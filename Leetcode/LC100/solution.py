class Solution:
    def isSameTree(self, p, q):
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


class Solution:
    def isSameTree(self, p, q):
        queue1 = []
        queue1.append(p)
        queue2 = []
        queue2.append(q)
        while len(queue1) > 0 and len(queue2) > 0:
            node1 = queue1.pop(0)
            node2 = queue2.pop(0)
            if node1 == None and node2 == None:
                continue
            if node1 == None or node2 == None:
                return False
            if node1.val != node2.val:
                return False
            queue1.append(node1.left)
            queue1.append(node1.right)
            queue2.append(node2.left)
            queue2.append(node2.right)
        if len(queue1) == 0 and len(queue2) == 0:
            return True
        return False
