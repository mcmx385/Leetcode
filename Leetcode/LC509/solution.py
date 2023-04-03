import functools


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n-1) + self.fib(n-2)


class Solution:
    def fib(self, n: int) -> int:
        return self.fib(n-1) + self.fib(n-2) if n > 1 else n


class Solution:
    def fib(self, n: int) -> int:
        @functools.lru_cache(None)
        def fib(n):
            return fib(n-1) + fib(n-2) if n > 1 else n
        return fib(n)


class Solution:
    matrix = [0, 1]

    def fib(self, n: int) -> int:
        if n < len(self.matrix):
            return self.matrix[n]
        else:
            sum = 0
            if n-1 >= len(self.matrix):
                sum += self.fib(n-1)
            else:
                sum += self.matrix[n-1]
            if n-2 >= len(self.matrix):
                sum += self.fib(n-2)
            else:
                sum += self.matrix[n-2]
            self.matrix.append(sum)
            return self.matrix[n]


class Solution:
    matrix = [0, 1]

    def fib(self, n: int) -> int:
        if n <= 0:
            return 0
        if n < len(self.matrix):
            return self.matrix[n]
        sum = 0
        if n-1 >= len(self.matrix):
            self.fib(n-1)
        sum += self.matrix[n-1]
        sum += self.matrix[n-2]
        self.matrix.append(sum)
        return self.matrix[n]
