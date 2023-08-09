class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return log(n, 2).is_integer()


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        rem = log(n, 2)
        return abs(rem - int(rem)) < 0.0000000000001


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            rem = n / 2
            if abs(rem - int(rem)) > 0.0000000000001:
                return False
            n /= 2
        return True


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            if n & 1 == 1 and n != 1:
                return False
            n >>= 1
        return True


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0
