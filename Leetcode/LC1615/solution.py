class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        maxRank = 0
        for i in range(n):
            for j in range(i + 1, n):
                tempRank = 0
                for road in roads:
                    if i in road or j in road:
                        tempRank += 1
                if tempRank > maxRank:
                    maxRank = tempRank
        return maxRank


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        dic = {}
        for i in range(n):
            dic[i] = set()
        for i, j in roads:
            dic[i].add(j)
            dic[j].add(i)
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                res = max(res, len(dic[i]) + len(dic[j]) - (j in dic[i]))
        return res
