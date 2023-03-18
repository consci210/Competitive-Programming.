class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if k == 1: return "0"
        if k == 2**(n-1): return "1"
        if k < 2**(n-1): return self.findKthBit(n-1, k)
        if k > 2**(n-1) : 
            answer = self.findKthBit(n-1 , 2**(n)- k)
            if answer == "0":
                return "1" 
            else :
                return "0"