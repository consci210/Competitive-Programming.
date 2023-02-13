class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        if not A:
            return 0
        A.sort()
        
        prev = A[0]
        outsum = 0
        for j in range(1,len(A)):
            if A[j] <= prev:
                outsum += prev - A[j] + 1
                prev += 1
            else:
                prev = A[j]
                
        return outsum