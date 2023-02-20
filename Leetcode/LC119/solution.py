class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]+[0]*rowIndex
        for level in range(0, rowIndex+1):  # time complexity: O(n^2), space complexity: O(n)
            for i in range(level, 0, -1):  # time complexity: O(n), space complexity: O(1)
                res[i] += res[i-1]
        return res


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]*(rowIndex+1)
        val = 1
        for i in range(1, rowIndex+1):  # time complexity: O(n), space complexity: O(1)
            val = val*(rowIndex-i+1)//i
            res[i] = val
        return res


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1]]
        for i in range(1, rowIndex):  # time complexity: O(n^2), space complexity: O(n)
            res.append([1]+[res[i-1][j]+res[i-1][j+1] for j in range(i-1)]+[1])  # time complexity: O(n), space complexity: O(n)
        return res[-1]

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        grid=[[1]*(i+1) for i in range(rowIndex+1)]
        for i in range(rowIndex):
            for j in range(1,i+1):
                grid[i+1][j]=grid[i][j-1]+grid[i][j]
        return grid[-1]