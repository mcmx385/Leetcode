class Solution:
    arr = []
    n = 0

    def dfs(self, left, right, s):
        if len(s) == self.n*2:
            self.arr.append(s)
            return
        if left < self.n:
            self.dfs(left+1, right, s+'(')
        if right < left:
            self.dfs(left, right+1, s+')')

    def generateParenthesis(self, n: int) -> List[str]:
        self.arr = []
        self.n = n
        self.dfs(0, 0, '')
        return self.arr
