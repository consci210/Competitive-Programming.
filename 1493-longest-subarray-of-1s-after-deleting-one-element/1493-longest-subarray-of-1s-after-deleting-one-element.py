class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        left_count = 0
        right_count = 0
        max_ = 0
        i = 0
        # initial
        while i < len(nums) and nums[i] != 0:
            left_count = left_count +1
            i=i+1
        
        # No zeros found
        if i == len(nums):
            return left_count - 1
        while i < len(nums):
            print(left_count, right_count)
            i=i+1

            while i < len(nums) and nums[i]!=0:
                right_count = right_count + 1
                i=i+1
            max_ = max(max_, left_count + right_count)
            left_count = right_count
            right_count = 0
        return max_