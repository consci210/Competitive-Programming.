class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        value  = 0
        maxSub = nums[0]
        for i in nums :
            if value < 0 :
                value = 0 
            value += i
            maxSub = max(maxSub , value )
        return maxSub