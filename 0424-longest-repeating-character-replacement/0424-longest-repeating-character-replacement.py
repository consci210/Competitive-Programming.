class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {} 
        l= 0
        longest = 0 
        for r in range(len(s)) :
            if s[r] in counter :
                counter[s[r]] +=1   
            else :
                counter[s[r]] = 1
                
            
            while (r-l+1 -  max(counter.values())) > k :
                counter[s[l]] -= 1
                if counter[s[l]]== 0 :
                    del counter[s[l]]
                l+=1 
           
            longest = max((r-l+1) , longest )
        return longest 