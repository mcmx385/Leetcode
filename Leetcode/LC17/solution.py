class Solution:
    mapping = ["", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        digs = self.mapping[int(digits[0])-1]
        if len(digits) == 1:
            return [dig for dig in digs]
        arr = []
        results = self.letterCombinations(digits[1:])
        for dig in digs:
            for result in results:
                arr.append(dig+result)
        return arr


class Solution:
    mapping = ["", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        arr = []
        for digit in digits[::-1]:
            digs = self.mapping[int(digit)-1]
            if len(arr) == 0:
                for dig in digs:
                    arr.append(dig)
            else:
                arr = [dig+result for dig in digs for result in arr]
        return arr