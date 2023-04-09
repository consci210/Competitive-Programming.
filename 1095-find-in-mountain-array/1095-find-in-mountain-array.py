# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        def find_peak(mountain_arr) :
            l = 0 
            r = mountain_arr.length() - 1
            peak = 0
            while l <= r :
                mid = (l+r)//2
                curr = mountain_arr.get(mid) 
                nxt =  mountain_arr.get(mid+1) 
                if curr > nxt :
                    if curr > mountain_arr.get(peak) :
                        peak = mid 
                    r = mid -1 
                else :
                    l = mid +1 

            return peak
        
        # if i get the peak then one side - inc and other - dec ...from 0 - peak inc then p+1 to end dec 
        def binary_search(target , l , r , arr , decreasing=False  ) :
            while l <= r :
                mid = (l+r)//2
                curr = arr.get(mid) 
                if curr == target :
                    return mid 
                elif (curr > target and decreasing) or (curr < target and not decreasing) :
                    l = mid + 1 
                else :
                    r = mid - 1 
                
            return -1 
    
        peak_idx = find_peak(mountain_arr)
        left_half = binary_search(target , 0 , peak_idx , mountain_arr , False )
        right_half = binary_search(target , (peak_idx + 1) , (mountain_arr.length() - 1) , mountain_arr  , True )
        
        if left_half == right_half : return left_half
        elif left_half == -1 and right_half != -1 : return right_half
        elif left_half != -1 and right_half == -1 : return left_half
        else : return(min(left_half , right_half))
                

            
        