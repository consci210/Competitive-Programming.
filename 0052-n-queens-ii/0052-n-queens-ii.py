class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        posD = set()
        negD = set()
        board = [ ["."]*n for i in range(n) ]
        self.answer = 0
        def backtrack(r=0):
            if r == n :
                self.answer+=1
            for c in range(n):
                if c in col or (r+c) in posD or (r-c) in negD :
                    continue 
                posD.add(r+c)
                negD.add(r-c)
                col.add(c)
                backtrack(r+1)
                posD.remove(r+c)
                negD.remove(r-c)
                col.remove(c)
        backtrack()
        return self.answer 
             
            