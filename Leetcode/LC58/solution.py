class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        j = len(s)-1
        while j >= 0 and s[j] == ' ':
            j -= 1
        i = j
        while i >= 0 and s[i] != ' ':
            i -= 1
        return j-i


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        start = False
        count = 0
        for c in s[::-1]:
            if c != ' ':
                start = True
                count += 1
            elif start:
                return count


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        ind = s.rindex(' ') if ' ' in s else -1
        return len(s)-ind-1
