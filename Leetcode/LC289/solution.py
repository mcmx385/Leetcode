class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        length = len(board[0])
        height = len(board)
        original = [[x for x in y] for y in board]
        for h in range(height):
            for l in range(length):
                live = 0
                if l > 0:
                    live += original[h][l - 1]
                if l < length - 1:
                    live += original[h][l + 1]
                if h > 0:
                    live += original[h - 1][l]
                if h < height - 1:
                    live += original[h + 1][l]
                if l > 0 and h > 0:
                    live += original[h - 1][l - 1]
                if l < length - 1 and h > 0:
                    live += original[h - 1][l + 1]
                if l > 0 and h < height - 1:
                    live += original[h + 1][l - 1]
                if l < length - 1 and h < height - 1:
                    live += original[h + 1][l + 1]
                if live < 2 or live > 3:
                    board[h][l] = 0
                elif live == 3 and board[h][l] == 0 or board[h][l] == 1:
                    board[h][l] = 1
