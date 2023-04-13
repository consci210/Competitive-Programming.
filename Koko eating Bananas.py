class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # rate = max in worst case 
        # time could be 1 
        r = max(piles)
        l = 1
        minimum = 0  
        while l <= r :
            m  = l + (r-l)//2
            total = 0 
            for p in piles :
                 total += math.ceil(p/m)
            if total <= h :
                minimum = m 
                r = m - 1
            if total > h :
                l = m + 1
        return minimum 
