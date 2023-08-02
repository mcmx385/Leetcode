class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n > 0:
            result += n % 2
            n //= 2
        return result


class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n > 0:
            result += n % 2
            n >>= 1
        return result


class Solution:
    def hammingWeight(self, n: int) -> int:
        if n < 1:
            return 0
        return n % 2 + self.hammingWeight(n >> 1)
