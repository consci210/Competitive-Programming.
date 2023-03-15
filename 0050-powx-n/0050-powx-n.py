class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0 :
            return 1
        if x == 0 :
            return 0
        
        def helper (x , n ) :
            if n == 1:
                return x 
            res = helper(x*x , n//2)
            res = res * x if n%2 else res 
            return res 
        return helper(x,abs(n)) if n > 0 else (1/helper(x,abs(n)))
            