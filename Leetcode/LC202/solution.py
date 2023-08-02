class Solution:
    def isHappy(self, n: int) -> bool:
        used = []
        while n > 0:
            result = 0
            while n > 0:
                rem = n % 10
                result += rem**2
                n //= 10
            if result in used:
                return False
            used.append(result)
            if result == 1:
                return True
            n = result
        return False


class Solution:
    def isHappy(self, n: int) -> bool:
        sett = set()
        while n != 1:
            if n in sett:
                return False
            sett.add(n)
            n = sum([int(i) ** 2 for i in str(n)])
        return True
