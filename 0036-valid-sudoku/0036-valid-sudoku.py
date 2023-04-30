class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = { (0,0) : [] , (0,1) : [] , (0,2) : [] , (1,0) : [] , (1,1) : [] , (1,2) : [] , (2,0) : [] , (2,1) : [] , (2,2) : []  }
        row = { 0: [] , 1:[] , 2 : [] , 3:[] , 4:[] , 5:[] , 6:[] , 7:[] , 8:[] }
        col = { 0: [] , 1:[] , 2 : [] , 3:[] , 4:[] , 5:[] , 6:[] , 7:[] , 8:[] }
    

        for r in range(9):
            for c in range(9):
                if board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in boxes[(r//3 , c//3)] :
                    return False 
                if board[r][c] != "." :
                    row[r].append(board[r][c])
                    col[c].append(board[r][c])
                    boxes[(r//3 , c//3)].append( board[r][c])
                
        return True 
            
            
        