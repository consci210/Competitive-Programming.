class Solution:
    @lru_cache()
    def tribonacci(self, n: int) -> int:
        if n ==2 or n == 1 :
            return 1
        if n == 0 :
            return 0
        
        return self.tribonacci(n-3) +  self.tribonacci(n-2) +  self.tribonacci(n-1)