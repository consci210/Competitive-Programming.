class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #neighbours are never equal  
        left = 0 
        right = len(nums)-1
        N =len(nums)
        while left < right :
            mid = (left + right)//2
            if nums[mid] > nums[(mid+1)%N] and nums[mid] > nums[(mid-1)%N]:
                return mid
            else :
                if nums[mid] <  nums[(mid+1)%N] :
                    left = mid + 1
                else :
                    right = mid - 1 
                    
        return right