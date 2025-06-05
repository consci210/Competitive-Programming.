class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst(nums, target,lookingLeft):
            i = -1 
            high = len(nums)- 1 
            low = 0 
 
            while low <= high: 
                mid =( high + low) //2 
                if nums[mid] == target and lookingLeft:
                    i = mid 
                    high = mid - 1
                elif nums[mid] == target and not lookingLeft:
                    i = mid 
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid -1 
                else:
                    low = mid+1
            return i 
        return([findFirst(nums,target,True),findFirst(nums,target,False)])