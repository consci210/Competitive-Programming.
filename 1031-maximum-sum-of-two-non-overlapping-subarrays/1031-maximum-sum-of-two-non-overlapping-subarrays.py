class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        d1 = []
        d2 = []
        s = sum(nums[:firstLen])
        d1.append(s)
        for i in range(1,len(nums)-firstLen+1):
            s -= nums[i-1] - nums[i+firstLen-1]
            d1.append(s)
        s = sum(nums[len(nums)-secondLen:])
        d2.append(s)
        for i in range(len(nums)-secondLen-1,-1,-1):
            s -= nums[i+secondLen] - nums[i]
            d2.insert(0,s)
        a = 0
        for i in range(len(d1)):
            for j in range(i+firstLen,len(d2)):
                a = max(a,d1[i]+d2[j])
        b = 0
        for i in range(len(d2)):
            for j in range(i+secondLen,len(d1)):
                b = max(b,d2[i]+d1[j])
        return max(a,b)