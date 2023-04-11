class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
            
            
        def search_matrix(matrix , target ):
            start = 0 
            end = len(matrix)-1
            while start <= end:
                mid = (start+end )//2
                if matrix[mid][0] > target :
                    end = mid - 1
                elif matrix[mid][-1] < target :
                    start = mid + 1
                else :
                    return mid 
                
            return mid
        
        def search_row(row , target):  
            print(row)
            left = 0 
            right = len(matrix[row] ) -1 
            while left <= right :
                mid = (left+right)//2
                if matrix[row][mid] == target :
                    return True 
                if matrix[row][mid] < target :
                    left = mid + 1
                else :
                    right = mid - 1
            
            return False 
        
        searched_row = search_matrix(matrix , target)
        answer = search_row(searched_row , target )
        return answer 