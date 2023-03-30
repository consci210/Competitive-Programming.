from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) == len(t):
            return s if (sorted(s) == sorted(t)) else ""
        if len(s) < len(t) or len(s)==0 :
            return ""
        seen = defaultdict(int)
        for letter in t :
            seen[letter] +=1 
            
        minimum = len(s)
        value = ""
        
        l = r = 0 
        while r < len(s) :
            seen[s[r]] -= 1
                
            while all(value <= 0 for value in seen.values()) :
                if (r-l+1) <= minimum :
                    minimum = r-l+1
                    value = s[l : r+1:]
               
                seen[s[l]] +=1 
                l+=1 
                    
            r+=1
        return value  