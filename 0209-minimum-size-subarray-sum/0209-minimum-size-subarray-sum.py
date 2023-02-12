
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums)==target:
            return len(nums)
        if sum(nums)<target:
            return 0
        left,right,tot=0,0,0
        m=len(nums)
        for right in range(len(nums)):
            tot+=nums[right]
            while tot>=target:
                m=min(m,right-left+1)  #storing minimum length of such subarrays 
                tot-=nums[left]
                left+=1
                
        return m
      