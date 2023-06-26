class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1
        res = 0
        if m > 1:
            res += self.uniquePaths(m - 1, n)
        if n > 1:
            res += self.uniquePaths(m, n - 1)
        return res


class Solution:
    def helper(self, m, n):
        if m == 1 and n == 1:
            return 1
        res = 0
        if m > 1:
            if self.matrix[m - 1 - 1][n - 1] != 0:
                res += self.matrix[m - 1 - 1][n - 1]
            else:
                val = self.helper(m - 1, n)
                self.matrix[m - 1 - 1][n - 1] = val
                res += val
        if n > 1:
            if self.matrix[m - 1][n - 1 - 1] != 0:
                res += self.matrix[m - 1][n - 1 - 1]
            else:
                val = self.helper(m, n - 1)
                self.matrix[m - 1][n - 1 - 1] = val
                res += val
        return res

    def uniquePaths(self, m: int, n: int) -> int:
        self.matrix = [[0 for _ in range(n)] for _ in range(m)]
        return self.helper(m, n)
