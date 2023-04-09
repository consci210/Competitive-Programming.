class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        #it will increase then decrease so I'll find the index of the max elt 
        
        l = 0 
        r = len(arr)-1
        peak = 0
        while l <= r :
            mid = (l+r)//2
            if arr[mid] >= arr[mid+1]:
                if arr[mid] > arr[peak] :
                    peak = mid 
                r = mid - 1
            if arr[mid] < arr[mid+1]:
                l = mid + 1
            
        return peak 