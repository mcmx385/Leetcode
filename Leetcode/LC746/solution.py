class Solution:
    def helper(self, cost, n):
        if n < 2:
            return cost[n]
        return cost[n]+min(self.helper(cost, n-1), self.helper(cost, n-2))

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        return min(self.helper(cost, n-1), self.helper(cost, n-2))


class Solution:
    def helper(self, cost, n):
        if n < 2:
            return cost[n]
        if self.result[n] != 0:
            return self.result[n]
        self.result[n] = cost[n]+min(self.helper(cost, n-1), self.helper(cost, n-2))
        return self.result[n]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        self.result = [0]*(n+1)
        return min(self.helper(cost, n-1), self.helper(cost, n-2))


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        result = [0]*(len(cost)+1)
        for i in range(2, len(cost)+1):
            result[i] = cost[i-1]+min(result[i-1], result[i-2])
        return min(result[-1], result[-2])


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        for i in range(2, n+1):
            cost[i] += min(cost[i-1], cost[i-2])
        return min(cost[n-1], cost[n-2])
