import re
import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(re.findall("[a-zA-Z0-9]+", s)).lower()
        return s == s[::-1]


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(re.findall("[a-zA-Z0-9]+", s)).lower()
        return s == s[::-1]


class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for c in s:
            if c.isalnum():
                res += c.lower()
        return res == res[::-1]


class Solution:
    def isPalindrome(self, s: str) -> bool:
        pattern = string.ascii_letters+string.digits
        res = ""
        for c in s:
            if c in pattern:
                res += c.lower()
        return res == res[::-1]


class Solution:
    def isPalindrome(self, s: str) -> bool:
        right = len(s)-1
        left = 0
        while left < right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
            elif not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
        return True
