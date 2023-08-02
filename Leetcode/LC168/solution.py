class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ordd = ord("A")
        result = ""
        while columnNumber > 0:
            columnNumber -= 1
            rem = columnNumber % 26
            columnNumber //= 26
            result = chr(ordd + rem) + result
        return result
