class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) > 1:
            res = 0
            while num > 0:
                res += num % 10
                num //= 10
            num = res
        return num
