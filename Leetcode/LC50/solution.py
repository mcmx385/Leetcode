class Solution:
    def myPow(self, x: float, n: int) -> float:
        return pow(x, n)


class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        for i in range(abs(n)):
            res *= x
        return res if n >= 0 else 1 / res


class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        half = abs(n) // 2
        extra = abs(n) / 2 > half
        for i in range(half):
            res *= x
        res *= res
        if extra:
            res *= x
        return res if n >= 0 else 1 / res


class Solution:
    def helper(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        sub = self.helper(x, n // 2)
        res = sub * sub
        res *= x if n % 2 else 1
        return res

    def myPow(self, x: float, n: int) -> float:
        res = self.helper(x, abs(n))
        if n < 0:
            res = 1 / res
        return res


class Solution:
    def myPow(self, x: float, n: int) -> float:
        neg_exp = n < 0
        arr = []
        n = abs(n)
        while n:
            arr.append(n % 2)
            n //= 2
        res = 1
        for i in range(len(arr) - 1, -1, -1):
            res *= res
            res *= x if arr[i] else 1
        if neg_exp:
            res = 1 / res
        return res
