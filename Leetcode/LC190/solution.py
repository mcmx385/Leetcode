class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            rem = n % 2
            result += rem * 2 ** (31 - i)
            n //= 2
        return result


class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            result <<= 1
            result += n & 1
            n >>= 1
        return result


class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            result = result << 1 | n & 1
            if n < 1:
                return result << (32 - i)
            n >>= 1
        return result


class Solution:
    def reverseBits(self, n: int) -> int:
        return self.helper(n, 0, 0)

    def helper(self, n, i, result):
        if i == 32:
            return result
        result <<= 1
        result += n & 1
        n >>= 1
        return self.helper(n, i + 1, result)


class Solution:
    def reverseBits(self, n: int) -> int:
        return self.helper(n, 0, 0)

    def helper(self, n, i, result):
        if n < 1:
            return result << (32 - i)
        return self.helper(n >> 1, i + 1, (result << 1) | (n & 1))
