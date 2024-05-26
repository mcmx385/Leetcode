class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        dictionary = {}
        total = len(pattern)
        if total != len(words):
            return False
        for i in range(total):
            if pattern[i] not in dictionary:
                if words[i] in dictionary.values():
                    return False
                dictionary[pattern[i]] = words[i]
            else:
                if dictionary[pattern[i]] != words[i]:
                    return False
        return True
