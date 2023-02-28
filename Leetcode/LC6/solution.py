class Solution:
    def convert(self, s: str, numRows: int) -> str:
        strings = ["" for i in range(numRows)]
        row = 0
        length = len(s)
        i = 0
        while i < length:
            if row == 0:
                for row in range(numRows):
                    if i < length:
                        strings[row] += s[i]
                        i += 1
                row = numRows-2
            else:
                strings[row] += s[i]
                row = (row-1) % numRows
                i += 1
        return "".join(strings)
