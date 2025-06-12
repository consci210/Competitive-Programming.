class Solution:
    def dfs(self, i, j):
        if (i < 0 or j < 0 or 
            i >= len(self.image) or j >= len(self.image[0]) or 
            self.image[i][j] != self.original):
            return
        self.image[i][j] = self.color
        self.dfs(i+1, j)
        self.dfs(i-1, j)
        self.dfs(i, j+1)
        self.dfs(i, j-1)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.color = color
        self.image = image
        self.original = image[sr][sc]

        if self.original == self.color:
            return image  
        
        self.dfs(sr, sc)
        return self.image
