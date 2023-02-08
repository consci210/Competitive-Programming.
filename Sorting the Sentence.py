class Solution:
    def sortSentence(self, s: str) -> str:
        list1= s.split()
        lastvalue = lambda x : x[-1]
        list1.sort(key= lastvalue)
        return " ".join(x[:-1] for x in list1)
        
        
    
