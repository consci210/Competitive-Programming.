class Solution:
    def partitionString(self, s: str) -> int:
        count = 0 
        r = 0 
        current = {}
        while r < len(s): 
            if s[r] in current  :
                count +=1
                current = {}
                
            else :
                current[s[r]] = 1
                r+=1 
        
        return count + 1 if current else count 