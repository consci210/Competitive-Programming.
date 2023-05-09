class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def is_valid(x, y, num):
            for i in range(9):
                if board[x][i] == str(num) or board[i][y] == str(num):
                    return False
            x_start = (x // 3) * 3
            y_start = (y // 3) * 3
            for i in range(3):
                for j in range(3):
                    if board[x_start + i][y_start + j] == str(num):
                        return False
            return True
        
        def dfs(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        for num in range(1, 10):
                            if is_valid(i, j, num):
                                board[i][j] = str(num)
                                if dfs(board):
                                    return True
                                board[i][j] = "."
                        return False
            return True
        
        dfs(board)