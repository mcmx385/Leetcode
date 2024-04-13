import math


class Solution:
    def mySqrt(self, x: int) -> int:
        return int(x**0.5)


class Solution:
    def mySqrt(self, x: int) -> int:
        return math.floor(math.sqrt(x))


class Solution:
    def mySqrt(self, x: int) -> int:
        return math.pow(x, 0.5)


class Solution:
    def mySqrt(self, x: int) -> int:
        guess = 1
        while guess * guess < x:  # O(logn)
            guess += 1
        return guess - 1 if guess * guess != x else guess


class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 0:
            return 0
        left = 1
        right = x
        while True:
            mid = left + (right - left) // 2  # O(logn)
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                right = mid
            else:
                if (mid + 1) * (mid + 1) > x:
                    return mid
                left = mid


class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 0:
            return 0
        left = 1
        right = x
        while True:
            mid = left + (right - left) // 2  # O(logn)
            if mid > x / mid:
                right = mid
            elif mid < x / mid:
                if (mid + 1) > x / (mid + 1):
                    return mid
                left = mid
            else:
                return mid


class Solution:
    def mySqrt(self, x: int) -> int:  # O(logn)
        root = x
        while root * root > x:
            root = int((root + x / root) / 2)
        return root


class Solution:
    def mySqrt(self, x: int) -> int:
        ans = 0
        mask = 1 << 16
        while mask > 0:  # O(1)
            ans |= mask
            if ans * ans > x:
                ans ^= mask
            mask >>= 1
        return ans


if __name__ == "__main__":
    x = 81
    print(Solution().mySqrt(x))
