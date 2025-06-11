class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cols , rows = len(grid[0]) , len(grid)
        isVisited = [[0 for i in range(cols)] for j in range(rows)]
        island = 0 
        
        def dfs(i,j):
            if i < 0 or j < 0 or i >=  rows or j>= cols or grid[i][j] == "0" or isVisited[i][j]== 1:
                return 
            isVisited[i][j] = 1
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1) 
            

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and isVisited[i][j] == 0 :
                    dfs(i,j)
                    island +=1 

        return island 
        

