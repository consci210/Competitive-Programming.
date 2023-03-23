class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            nums[i] = count 
        return nums 