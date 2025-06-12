class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        difference = abs(nums[0] - nums[-1])
        for i in range(1,len(nums)):
            difference = max(abs(nums[i]-nums[i-1]) , difference)
        return difference 