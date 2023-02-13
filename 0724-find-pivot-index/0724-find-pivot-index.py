class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        rightSum = sum(nums[1:])
        for index in range(len(nums)):
            if leftSum == rightSum:
                return index
            if index != len(nums)-1:
                leftSum += nums[index]
                rightSum -= nums[index+1]

        return -1