from typing import List
from itertools import accumulate


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1
        n = len(gas)
        gascost = [gas[i] - cost[i] for i in range(n)]
        remain = 0
        for i in range(n):
            if gascost[i] >= 0:
                remain = 0
                good = True
                for j in range(n):
                    ii = (i + j) % n
                    remain += gascost[ii]
                    if remain < 0:
                        good = False
                        break
                if good:
                    return i
        return -1


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1
        balance = deficit = start = 0
        for i in range(len(gas)):
            balance += gas[i] - cost[i]
            if balance < 0:
                deficit += balance
                start = i + 1
                balance = 0
        return start if balance + deficit >= 0 else -1


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1
        balance = index = 0
        for i in range(len(gas)):
            balance += gas[i] - cost[i]
            if balance < 0:
                index = i + 1
                balance = 0
        return index


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = list(map(lambda x, y: x - y, gas, cost))
        if diff[-1] < 0:
            return -1
        return diff.index(min(diff))


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = list(accumulate([x - y for x, y in zip(gas, cost)]))
        return diff.index(min(diff)) if diff[-1] >= 0 else -1
