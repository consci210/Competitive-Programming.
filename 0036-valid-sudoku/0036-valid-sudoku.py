class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_column = { 0 : [],1 : [],2 : [],3 : [],4 : [], 5: [],6 : [],7 : [],8 : []}  
        seen_box = { (0,0) : [] ,(0,1) : [] , (0,2) : [], (1,0) : [] ,(1,1) : [], (1,2) : [], (2,0) : [] ,(2,1) : [] ,(2,2): []}  
        seen_row = { 0 : [],1 : [],2 : [],3 : [],4 : [], 5: [],6 : [],7 : [],8 : []}  
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue 
                if board[i][j] in seen_box[ (i//3,j//3)] or board[i][j] in seen_column[j] or board[i][j] in seen_row[i]  :
                    return False 
                seen_box[(i//3,j//3) ].append(board[i][j])
                seen_column[j].append(board[i][j])
                seen_row[i].append(board[i][j])
        return True 
                    