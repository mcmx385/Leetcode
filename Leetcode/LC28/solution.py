class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                if haystack[i : i + len(needle)] == needle:
                    return i
        return -1


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if all(haystack[i + j] == needle[j] for j in range(len(needle))):
                return i
        return -1


# built-in function
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        elif needle in haystack:
            return haystack.index(needle)
        else:
            return -1


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        new = haystack.replace(needle, "A")
        if new == haystack:
            return -1
        else:
            return new.index("A")


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
