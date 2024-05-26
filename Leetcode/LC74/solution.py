class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        if rows == 0:
            return False
        if rows == 1:
            return target in matrix[0]
        for row in range(rows - 1):
            if matrix[row][0] <= target and matrix[row + 1][0] > target:
                return target in matrix[row]
        return target in matrix[rows - 1]
