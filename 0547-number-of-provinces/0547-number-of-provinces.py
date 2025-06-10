class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        rows = len(isConnected)
        isVisited = [0 for i in range(rows)]
        province = 0 
        def dfs(city):
            isVisited[city] = 1 
            for neighbor in range(rows):
                if isConnected[city][neighbor] == 1 and isVisited[neighbor] != 1:
                    dfs(neighbor)
                   
        
        for city in range(rows):
            if isVisited[city] == 0 :
                dfs(city)
                province +=1 
        
        return province 

        
            