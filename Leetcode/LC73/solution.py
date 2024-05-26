class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        columns = len(matrix[0])
        rowsMap = [False] * rows
        columnsMap = [False] * columns
        for row in range(rows):
            for column in range(columns):
                if matrix[row][column] == 0:
                    rowsMap[row] = True
                    columnsMap[column] = True
        for row in range(rows):
            if rowsMap[row]:
                matrix[row] = [0] * columns
        for column in range(columns):
            if columnsMap[column]:
                for row in range(rows):
                    matrix[row][column] = 0


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        columns = len(matrix[0])
        rowsMap = [False] * rows
        columnsMap = [False] * columns
        for row in range(rows):
            for column in range(columns):
                if matrix[row][column] == 0:
                    rowsMap[row] = True
                    columnsMap[column] = True
        for row in range(rows):
            for column in range(columns):
                if rowsMap[row] or columnsMap[column]:
                    matrix[row][column] = 0
