class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        smallest = nums[0]
        ans = -1 
        for num in nums:
            if num > smallest:
                ans = max(ans,num-smallest)
            smallest = min(smallest,num)
        return ans 