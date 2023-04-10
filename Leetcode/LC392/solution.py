class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for sub in s:
            if sub not in t:
                return False
        return True


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for sub in s:
            while sub != t[i]:
                i += 1
                if i >= len(t):
                    return False
        return True


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        sLen = len(s)
        tLen = len(t)
        if sLen == 0 and tLen == 0:
            return True
        elif tLen == 0:
            return False
        for sub in s:
            if i >= tLen:
                return False
            while sub != t[i]:
                i += 1
                if i >= tLen:
                    return False
            if sub == t[i]:
                i += 1
        return True
