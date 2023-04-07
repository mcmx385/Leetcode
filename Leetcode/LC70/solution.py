class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1
        return self.climbStairs(n-1)+self.climbStairs(n-2)


class Solution:
    def helper(self, n):
        if n < 2:
            return 1
        if self.result[n] != 0:
            return self.result[n]
        self.result[n] = self.helper(n-1)+self.helper(n-2)
        return self.result[n]

    def climbStairs(self, n: int) -> int:
        self.result = [0]*(n+1)
        return self.helper(n)