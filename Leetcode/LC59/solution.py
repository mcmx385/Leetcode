class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for j in range(n)] for i in range(n)]
        startRow = 0
        endRow = len(matrix) - 1
        startCol = 0
        endCol = len(matrix[0]) - 1
        count = 1
        while startRow <= endRow and startCol <= endCol:
            for col in range(startCol, endCol + 1):
                matrix[startRow][col] = count  # first row all cols
                count += 1
            startRow += 1
            if startRow > endRow:
                break
            for row in range(startRow, endRow + 1):
                matrix[row][endCol] = count  # last col all rows
                count += 1
            endCol -= 1
            if startCol > endCol:
                break
            for col in range(endCol, startCol - 1, -1):
                matrix[endRow][col] = count  # last row all cols
                count += 1
            endRow -= 1
            if startRow > endRow:
                break
            for row in range(endRow, startRow - 1, -1):
                matrix[row][startCol] = count  # first col all rows
                count += 1
            startCol += 1
            if startCol > endCol:
                break
        return matrix
