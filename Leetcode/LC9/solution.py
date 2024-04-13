class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        return string == string[::-1]


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reverse = 0
        while x > reverse:
            reverse = reverse * 10 + x % 10
            x //= 10
        return x == reverse or x == reverse // 10


class Solution:
    def isPalindrome(self, x: int) -> bool:
        myString = str(x)
        for i in range(len(myString) // 2):
            if myString[i] == myString[~i]:
                continue
            else:
                return False
        return True


class Solution:
    def isPalindrome(self, x: int) -> bool:
        p = x
        q = 0
        while p >= 1:
            q = q * 10 + p % 10
            p = p // 10
        return q == x
