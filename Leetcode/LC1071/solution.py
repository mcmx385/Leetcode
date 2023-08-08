class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        size = gcd(len(str1), len(str2))
        return str1[:size]


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        return "" if str1 + str2 != str2 + str1 else str1[: gcd(len(str1), len(str2))]
