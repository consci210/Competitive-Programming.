class Solution:
    def maxDifference(self, s: str) -> int:
        frequency = Counter(s) 
        se,lo = len(s) , 0 
        for num in frequency.values() :
            if num % 2 == 0 :
                se = num if num < se else se
            else:
                lo = num if num > lo else lo
                
        return (lo - se)