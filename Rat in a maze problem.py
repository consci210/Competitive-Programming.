
# geeks for geeks problem 

# User function template for Python 3

class Solution:
    def findPath(self, m, n):
        
        def is_valid_move(row, col):
            if row >= 0 and row < n and col >= 0 and col < n and m[row][col] == 1:
                return True
            return False

        def backtrack(row, col, path):
            if row == n - 1 and col == n - 1:
                paths.append(path)
                return
            
            if row == 0 and col == 0 and m[row][col] == 0 :
                return False 
              
            m[row][col] = 0
          
            if is_valid_move(row + 1, col):
                backtrack(row + 1, col, path + 'D')
            if is_valid_move(row, col + 1):
                backtrack(row, col + 1, path + 'R')
            if is_valid_move(row - 1, col):
                backtrack(row - 1, col, path + 'U')
            if is_valid_move(row, col - 1):
                backtrack(row, col - 1, path + 'L')

            m[row][col] = 1

     
        paths = []
        backtrack(0, 0, '')
        paths.sort()

        return paths


       
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends
