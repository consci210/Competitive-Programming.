class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binarySearch(nums,target,low,high):
            mid = (low + high) //2
            if nums[mid] == target :
                return mid 
            elif low > high:
                return -1
            elif nums[mid] > target:
                return binarySearch(nums, target, low, mid-1)
            else:
                return binarySearch(nums,target,mid+1,high)
        
        return(binarySearch(nums,target,0,len(nums)-1))
        # low = 0 
        # high = len(nums) - 1
        # while low<=high :
        #     mid = (low+high)//2 
        #     if nums[mid] == target:
        #         return mid 
        #     elif nums[mid] > target: 
        #         high = mid-1
        #     else:
        #         low = mid +1 
        # return -1 