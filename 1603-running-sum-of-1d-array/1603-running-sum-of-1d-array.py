class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefixSum = [0 for i in range(len(nums))]
        summation = 0 
        for i in range(len(nums)):
            summation += nums[i]
            prefixSum[i] = summation 
        return prefixSum 