class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def find_first(arr , val ) :
            res = -1
            l = 0 
            r = len(arr)-1
            
            while l <= r :
                mid = (l+r)//2
                if arr[mid] == val :
                    res = mid 
                    r = mid -1 
                elif arr[mid] < val :
                    l = mid + 1
                else :
                    r = mid - 1
            
            return res 
        
        def find_last(arr , val ) :
            res = -1
            l = 0 
            r = len(arr)-1
            
            while l <= r :
                mid = (l+r)//2
                if arr[mid] == val :
                    res = mid 
                    l = mid + 1 
                elif arr[mid] < val :
                    l = mid + 1
                else :
                    r = mid - 1
            
            return res 
        
        return([find_first(nums,target) ,find_last(nums , target) ])