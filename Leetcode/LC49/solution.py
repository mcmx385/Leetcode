class Solution:
    def sortStr(self, string):
        return ''.join(sorted(string))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = {}
        for string in strs:
            sortedStr = self.sortStr(string)
            if sortedStr not in mapping:
                mapping[sortedStr] = [string]
            else:
                mapping[sortedStr].append(string)
        return mapping.values()
