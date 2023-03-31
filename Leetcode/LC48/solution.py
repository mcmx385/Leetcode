class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        start = 0
        end = len(matrix)-1
        while start <= end:
            for i in range(end-start):
                top = matrix[start][start+i]
                matrix[start][start+i] = matrix[end-i][start]
                matrix[end-i][start] = matrix[end][end-i]
                matrix[end][end-i] = matrix[start+i][end]
                matrix[start+i][end] = top
            start += 1
            end -= 1


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        start = 0
        end = length-1
        while start <= end:
            temp = matrix[start]
            matrix[start] = matrix[end]
            matrix[end] = temp
            start += 1
            end-=1
        for i in range(length):
            for j in range(i+1, length):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp