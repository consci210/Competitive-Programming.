class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        r = 0 
        c = len(matrix[r])-1
        while r < len(matrix) and c > -1 :
            if matrix[r][c] == target :
                return True
            elif matrix[r][c] < target :
                r+=1
            elif matrix[r][c] > target :
                c-=1 
            
        return False 
            