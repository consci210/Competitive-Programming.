class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums)-1
        n = len(nums)
        while l <= r :
            m = l + (r-l)//2  
            
            if nums[m] >= nums[l] :
                if nums[l] < nums[(l-1)%n] and nums[l] < nums[(l+1)%n] :
                    return nums[l]
                else :
                    l = m + 1
                    
            elif nums[m] < nums[r] :
                if nums[m] < nums[(m-1)%n] and nums[m] < nums[(m+1)%n] :
                    return nums[m]
                else :
                    r = m - 1
                    
                    
        return nums[r]