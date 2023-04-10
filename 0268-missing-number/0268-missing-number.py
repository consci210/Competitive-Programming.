class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing_num = len(nums)
        for i, num in enumerate(nums):
            missing_num ^= i ^ num
        return missing_num