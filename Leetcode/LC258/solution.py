class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) > 1:
            res = 0
            while num > 0:
                res += num % 10
                num //= 10
            num = res
        return num


class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9
