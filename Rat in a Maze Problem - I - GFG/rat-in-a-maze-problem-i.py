# User function template for Python 3

class Solution:
    def findPath(self, m, n):
        
        def is_valid_move(row, col):
            # Check if the move is within the matrix boundaries and the cell is not blocked
            if row >= 0 and row < n and col >= 0 and col < n and m[row][col] == 1:
                return True
            return False

        def backtrack(row, col, path):
            # If the destination is reached, add the current path to the list of paths
            if row == n - 1 and col == n - 1:
                paths.append(path)
                return
            
            if row == 0 and col == 0 and m[row][col] == 0 :
                return False 
            
            # Mark the current cell as visited
            m[row][col] = 0

            # Try moving in all four directions: Down, Right, Up, Left
            if is_valid_move(row + 1, col):
                backtrack(row + 1, col, path + 'D')
            if is_valid_move(row, col + 1):
                backtrack(row, col + 1, path + 'R')
            if is_valid_move(row - 1, col):
                backtrack(row - 1, col, path + 'U')
            if is_valid_move(row, col - 1):
                backtrack(row, col - 1, path + 'L')

            # Mark the current cell as unvisited before backtracking
            m[row][col] = 1

        # List to store the paths
        paths = []
        # Start the backtracking from the source cell (0, 0)
        backtrack(0, 0, '')
        # Sort the paths in lexicographic order
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