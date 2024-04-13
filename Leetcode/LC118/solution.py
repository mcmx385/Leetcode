class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(
            0, numRows - 1
        ):  # time complexity: O(n^2), space complexity: O(n)
            row = [1]
            for j in range(
                len(res[i]) - 1
            ):  # time complexity: O(n), space complexity: O(1)
                row.append(res[i][j] + res[i][j + 1])
            row.append(1)
            res.append(row)
        return res


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows):  # time complexity: O(n^2), space complexity: O(n)
            res.append(
                list(map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1]))
            )  # time complexity: O(n), space complexity: O(n)
        return res


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows):  # time complexity: O(n^2), space complexity: O(n)
            res.append(
                [1] + [res[i - 1][j] + res[i - 1][j + 1] for j in range(i - 1)] + [1]
            )  # time complexity: O(n), space complexity: O(n)
        return res
