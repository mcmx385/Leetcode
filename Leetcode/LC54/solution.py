class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        startRow = 0
        endRow = len(matrix)-1
        startCol = 0
        endCol = len(matrix[0])-1
        res = []
        switch = 0
        while startRow <= endRow and startCol <= endCol:
            if switch == 0:
                for col in range(startCol, endCol+1):
                    res.append(matrix[startRow][col])  # first row all cols
                startRow += 1
            elif switch == 1:
                for row in range(startRow, endRow+1):
                    res.append(matrix[row][endCol])  # last col all rows
                endCol -= 1
            elif switch == 2:
                for col in range(endCol, startCol-1, -1):
                    res.append(matrix[endRow][col])  # last row all cols
                endRow -= 1
            elif switch == 3:
                for row in range(endRow, startRow-1, -1):
                    res.append(matrix[row][startCol])  # first col all rows
                startCol += 1
            switch = (switch+1) % 4
        return res


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        startRow = 0
        endRow = len(matrix)-1
        startCol = 0
        endCol = len(matrix[0])-1
        res = []
        while startRow <= endRow and startCol <= endCol:
            for col in range(startCol, endCol+1):
                res.append(matrix[startRow][col])  # first row all cols
            startRow += 1
            if startRow > endRow:
                break
            for row in range(startRow, endRow+1):
                res.append(matrix[row][endCol])  # last col all rows
            endCol -= 1
            if startCol > endCol:
                break
            for col in range(endCol, startCol-1, -1):
                res.append(matrix[endRow][col])  # last row all cols
            endRow -= 1
            if startRow > endRow:
                break
            for row in range(endRow, startRow-1, -1):
                res.append(matrix[row][startCol])  # first col all rows
            startCol += 1
            if startCol > endCol:
                break
        return res
