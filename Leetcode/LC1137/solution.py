class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 1
        return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)


class Solution:
    matrix = [0, 1, 1]

    def tribonacci(self, n: int) -> int:
        if n < 0:
            return 0
        if n < len(self.matrix):
            return self.matrix[n]
        sum = 0
        if n - 1 >= len(self.matrix):
            self.tribonacci(n - 1)
        sum += self.matrix[n - 1]
        sum += self.matrix[n - 2]
        sum += self.matrix[n - 3]
        self.matrix.append(sum)
        return self.matrix[n]
