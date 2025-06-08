class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        counter = 0 
        for i in range(min(len(word1), len(word2))):
            res+=word1[i] 
            res+=word2[i]
            counter+=1 
        if len(word1)> counter:
            res+=word1[counter:]
        if len(word2)> counter:
            res+=word2[counter:]
        
        return res 
